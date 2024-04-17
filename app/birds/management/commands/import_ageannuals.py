from django.core.management.base import BaseCommand
from django.db import transaction
from birds.serializers import parse_ageannuals_from_csv
from birds.models import AgeAnnual

class Command(BaseCommand):
    help = "Loads the data from CSV into AgeAnnual model"

    def add_arguments(self, parser):
        parser.add_argument("csv_file", type=str, help="The CSV file to load data from")

    @transaction.atomic
    def handle(self, *args, **options):
        csv_file_path = options["csv_file"]
        try:
            AgeAnnual.objects.all().delete()
            age_annuals_data = parse_ageannuals_from_csv(csv_file_path)

            # Create AgeAnnual objects
            for data in age_annuals_data:
                AgeAnnual.objects.create(
                    number=data["number"],
                    alpha=data["alpha"],
                    description=data["description"],
                    explanation=data["explanation"],
                )

            self.stdout.write(self.style.SUCCESS(f"Successfully loaded {len(age_annuals_data)} AgeAnnual objects from {csv_file_path}"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"An error occurred: {e}"))