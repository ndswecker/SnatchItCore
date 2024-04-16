from django.core.management.base import BaseCommand
from django.db import transaction
from birds.models import AgeWRP
from birds.serializers import parse_agewrps_from_csv

class Command(BaseCommand):
    help = "Loads data from CSV into AgeWRP model"

    def add_arguments(self, parser):
        parser.add_argument("csv_file", type=str, help="The CSV file to load data from")

    @transaction.atomic
    def handle(self, *args, **options):
        csv_file_path = options["csv_file"]
        try:
            AgeWRP.objects.all().delete()
            age_wrps_data = parse_agewrps_from_csv(csv_file_path)
            
            # Create AgeWRP objects and link annuals atomically
            for data in age_wrps_data:
                age_wrp = AgeWRP.objects.create(
                    code=data["code"],
                    sequence=data["sequence"],
                    description=data["description"],
                    status=data["status"],
                )
                for annual in data["annuals"]:
                    age_wrp.annuals.add(annual)

            self.stdout.write(self.style.SUCCESS(f"Successfully loaded {len(age_wrps_data)} AgeWRP objects from {csv_file_path}"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"An error occurred: {e}"))