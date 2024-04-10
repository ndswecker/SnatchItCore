import csv
import datetime
import pathlib

from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
from django.utils import timezone

from maps.models import CaptureRecord
from users.models import User

user = User.objects.get(id=1)

class IBPDataImporter:
    def __init__(self, csv_file):
        self.csv_file = csv_file

    def parse_csv(self):
        reader = csv.DictReader(self.csv_file.read().decode("utf-8").splitlines())
        for row in reader:
            print(row)
            self.create_capture_record(row)
    
    def create_capture_record(self, row):
        capture_record = CaptureRecord()

        # Map each csv column to the corresponding CaptureRecord field
        capture_record.station = row.get("LOC")
        capture_record.band_size = row.get("BS")
        capture_record.bander_initials = row.get("BI")
        capture_record.capture_code = row.get("CODE")
        capture_record.band_number = int(row.get("BAND#"))
        capture_record.alpha_code = row.get("SPECIES")
        capture_record.species_number = self.get_species_number(row.get("SPECIES"))
        capture_record.age_annual = int(row.get("AGE"))

        how_aged_1, how_aged_2 = self.set_how_aged(row.get("HA"))
        capture_record.how_aged_1 = how_aged_1
        capture_record.how_aged_2 = how_aged_2

        capture_record.age_WRP = row.get("WRP")
        capture_record.sex = row.get("SEX")

        how_sexed_1, how_sexed_2 = self.set_how_sexed(row.get("HS"))
        capture_record.how_sexed_1 = how_sexed_1
        capture_record.how_sexed_2 = how_sexed_2

        capture_record.skull = int(row.get("SK"))
        capture_record.cloacal_protuberance = int(row.get("CP"))
        capture_record.brood_patch = int(row.get("BP"))
        capture_record.fat = int(row.get("FAT"))
        capture_record.body_molt = int(row.get("BMOLT"))
        capture_record.ff_molt = row.get("FFMOLT")
        capture_record.ff_wear = int(row.get("FFWEAR"))
        capture_record.juv_body_plumage = int(row.get("J BDY PL"))
        capture_record.primary_coverts = row.get("PPC")
        capture_record.secondary_coverts = row.get("SSC")
        capture_record.primaries = row.get("PPF")
        capture_record.secondaries = row.get("SSF")
        capture_record.tertials = row.get("TT")
        capture_record.rectrices = row.get("RR")
        capture_record.body_plumage = row.get("BPL")
        capture_record.non_feather = row.get("NF")
        capture_record.wing_chord = int(row.get("WNG"))
        capture_record.status = row.get("STATUS")
        capture_date = self.parse_date(row.get("DATE"))
        capture_time = self.parse_time(row.get("TIME"))
        capture_record.capture_time = timezone.make_aware(
            datetime.datetime.combine(capture_date, capture_time)
        )
        capture_record.net = int(row.get("NET"))
        capture_record.disposition = row.get("DISP")
        capture_record.note_number = row.get("NOTE #")
        capture_record.note = row.get("NOTES")

        # Assume all imported IBP records have already undergone validation
        capture_record.is_validated = True
        # Assume for IBP imports that the bander is also the scribe
        capture_record.scribe_initials = row.get("BI")

class Command(BaseCommand):
    help = "Import IBP records from a CSV"

    def add_arguments(self, parser):
        parser.add_argument("path", type=str, help="full path to CSV file")
        parser.add_argument("--header", help="skip CSV header line", action="store_true")

    @transaction.atomic
    def handle(self, *args, **options):
        path = pathlib.Path(options['path'])
        if not path.exists() or not path.is_file():
            raise CommandError(f"Invalid path: {options['path']}")

        with path.open('r', encoding='utf-8') as csv_file:
            if options['header']:
                next(csv_file)  # Skip the header line if --header is specified

            importer = IBPDataImporter(csv_file)
            importer.parse_csv()

        self.stdout.write(self.style.SUCCESS(f"Successfully imported records from {path}"))