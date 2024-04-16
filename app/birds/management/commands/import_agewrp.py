import csv
from django.core.management.base import BaseCommand
from django.db import transaction
from birds.models import AgeWRP, AgeAnnual
from birds.serializers import parse_agewrps_from_csv

class Command(BaseCommand):
    help = "Loads data from CSV into AgeWRP model"

    def add_arguments(self, parser):
        parser.add_argument("csv_file", type=str, help="The CSV file to load data from")

    @transaction.atomic
    def handle(self, *args, **options):
        csv_file_path = options["csv_file"]
        age_wrps = parse_agewrps_from_csv(csv_file_path)
        AgeWRP.objects.bulk_create(age_wrps, ignore_conflicts=True) # Assume all AgeWRP objects are ready to be saved without annuals
        self.stdout.write(self.style.SUCCESS(f"Successfully loaded {len(age_wrps)} AgeWRP objects"))
