from django.core.exceptions import ValidationError

from .base_import_command import BaseImportCommand
from birds.models import AgeAnnual
from birds.serializers import parse_ageannuals_from_csv


class Command(BaseImportCommand):
    help = "Loads the data from CSV into AgeAnnual model"

    def handle(self, *args, **options):
        AgeAnnual.objects.all().delete()

        csv_file_path = options["csv_file"]
        age_annuals_data = parse_ageannuals_from_csv(csv_file_path)

        age_annuals = [
            AgeAnnual(
                number=data["number"],
                alpha=data["alpha"],
                description=data["description"],
                explanation=data["explanation"],
            )
            for data in age_annuals_data
        ]

        try:
            AgeAnnual.objects.bulk_create(age_annuals)  # Bulk insert new data
            self.stdout.write(
                self.style.SUCCESS(f"Successfully loaded {len(age_annuals)} AgeAnnual objects from {csv_file_path}"),
            )
        except ValidationError as e:
            self.stdout.write(self.style.ERROR(f"A validation error occurred: {e}"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"An error occurred: {e}"))
