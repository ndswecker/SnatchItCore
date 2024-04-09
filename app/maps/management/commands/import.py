import csv
import datetime
import pathlib

from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
from django.utils import timezone
from pydantic import BaseModel

from maps.models import CaptureRecord
from users.models import User

user = User.objects.get(id=1)


class Record(BaseModel):
    user: None
    scribe_initials: str
    capture_code: str
    species_number: int
    band_size: str
    band_number: int
    alpha_code: str
    age_annual: int
    how_aged_1: str
    how_aged_2: str
    age_WRP: str
    sex: str
    how_sexed_1: str
    how_sexed_2: str
    cloacal_direction: str
    skull: int
    cloacal_protuberance: int
    brood_patch: int
    fat: int
    body_molt: int
    ff_molt: str
    ff_wear: int
    juv_body_plumage: int
    primary_coverts: str
    secondary_coverts: str
    primaries: str
    secondaries: str
    tertials: str
    rectrices: str
    body_plumage: str
    alula: str
    non_feather: str
    wing_chord: int
    body_mass: float
    status: int
    capture_time: datetime.datetime
    hold_time: float
    station: str
    net: int
    disposition: str
    note_number: str
    note: str
    bander_initials: str
    discrepancies: str
    is_validated: bool

HEADER = [
    "station",
    "band_size",
    "PG",
    "bander_initials",
    "capture_code",
    "band_number",
    "alpha_code",
    "age_annual",
    "HA",
    "age_WRP",
    "sex",
    "HS",
    "skull",
    "cloacal_protuberance",
    "brood_patch",
    "fat",
    "body_molt",
    "ff_molt",
    "ff_wear",
    "juv_body_plumage",
    "primary_coverts",
    "secondary_coverts",
    "primaries",
    "secondaries",
    "tertials",
    "rectrices",
    "body_plumage",
    "non_feather",
    "wing_chord",
    "body_mass",
    "status",
    "DATE",
    "TIME",
    "STATION",
    "net",
    "disposition",
    "note_number",
    "FTHR PULL",
    "note",
]


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
                data = dict(zip(HEADER, line))
                record = self.format_data(data)
                records.append(CaptureRecord(**record.dict()))
                break
        # CaptureRecord.objects.bulk_create(records)
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

    def format_data(self, data: dict):
        self._format_how_aged(data)
        self._format_how_sexed(data)
        self._format_how_capture_date(data)

        del data["PG"]
        del data["HA"]
        del data["HS"]
        del data["DATE"]
        del data["TIME"]
        del data["STATION"]
        del data["FTHR PULL"]

        record = Record(**data)
        record.user = user
        return record
