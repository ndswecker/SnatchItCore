import csv
import datetime
import pathlib

from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
from django.utils import timezone

from maps.models import CaptureRecord
from maps.maps_reference_data import SPECIES
from users.models import User

user = User.objects.get(pk=1)

species_alpha_codes = {s["alpha_code"]: s["species_number"] for s in SPECIES.values()}

csv_columns = {
    "station": str,
    "band_size": str,
    "PG": str,
    "bander_initials": str,
    "capture_code": str,
    "band_number": int,
    "alpha_code": str,
    "age_annual": int,
    "HA": str,
    "age_WRP": str,
    "sex": str,
    "HS": str,
    "skull": int,
    "cloacal_protuberance": int,
    "brood_patch": int,
    "fat": int,
    "body_molt": int,
    "ff_molt": str,
    "ff_wear": int,
    "juv_body_plumage": int,
    "primary_coverts": str,
    "secondary_coverts": str,
    "primaries": str,
    "secondaries": str,
    "tertials": str,
    "rectrices": str,
    "body_plumage": str,
    "non_feather": str,
    "wing_chord": int,
    "body_mass": float,
    "status": int,
    "DATE": str,
    "TIME": str,
    "STATION": str,
    "net": int,
    "disposition": str,
    "note_number": str,
    "FTHR PULL": str,
    "note": str,
}

model_fields = {
    "scribe_initials": str,
    "species_number": int,
    "how_aged_1": str,
    "how_aged_2": str,
    "how_sexed_1": str,
    "how_sexed_2": str,
    "cloacal_direction": str,
    "alula": str,
    "discrepancies": str,
    "is_validated": bool,
    "hold_time": float,
}

fields = csv_columns.copy()
fields.update(model_fields)


class Command(BaseCommand):
    help = "Import IBP records from a CSV"

    def add_arguments(self, parser):
        parser.add_argument("path", type=str, help="full path to CSV file")
        parser.add_argument("--header", help="skip CSV header line", action="store_true")

    @transaction.atomic
    def handle(self, *args, **options):
        path = pathlib.Path(options["path"])
        if not path.exists():
            raise CommandError(f"Invalid path: {options['path']}")

        records = []
        with path.open("r", encoding="utf-8") as file:
            reader = csv.reader(file)
            if options["header"]:
                next(reader)  # skip header
            for line in reader:
                data = dict(zip(csv_columns.keys(), line))
                self.format_data(data)
                records.append(CaptureRecord(**data))
        CaptureRecord.objects.bulk_create(records)
        self.stdout.write(self.style.SUCCESS(f"Imported {len(records)} records"))

    def _format_how_aged(self, data):
        if data["HA"]:
            if len(data["HA"]) == 2:
                data["how_aged_1"] = data["HA"][0]
                data["how_aged_2"] = data["HA"][1]
            else:
                data["how_aged_1"] = data["HA"]

    def _format_how_sexed(self, data):
        if data["HS"]:
            if len(data["HS"]) == 2:
                data["how_sexed_1"] = data["HS"][0]
                data["how_sexed_2"] = data["HS"][1]
            else:
                data["how_sexed_1"] = data["HS"]

    def _format_how_capture_date(self, data):
        month, day, year = data["DATE"].split("/")
        date = datetime.date(int(year), int(month), int(day))

        time_str = data["TIME"].zfill(4)
        hour = int(time_str[:2])
        minute = int(time_str[2:4])
        time = datetime.time(hour, minute)

        data["capture_time"] = timezone.make_aware(
            datetime.datetime.combine(date, time)
        )

    def _format_species_number(self, data):
        alpha_code = data["alpha_code"]
        data["species_number"] = species_alpha_codes[alpha_code]

    def _cast_types(self, data: dict):
        for key, value in data.items():
            if key in fields:
                data_type = fields[key]
                try:
                    data[key] = data_type(value)
                except ValueError:
                    data[key] = None

    def format_data(self, data: dict):
        self._format_how_aged(data)
        self._format_how_sexed(data)
        self._format_how_capture_date(data)
        self._format_species_number(data)

        del data["PG"]
        del data["HA"]
        del data["HS"]
        del data["DATE"]
        del data["TIME"]
        del data["STATION"]
        del data["FTHR PULL"]

        self._cast_types(data)

        data["user"] = user
