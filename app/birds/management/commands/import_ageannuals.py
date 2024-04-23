from django.db import transaction
from django.db.utils import IntegrityError
from django.db.utils import DataError
from birds.serializers import parse_ageannuals_from_csv
from birds.models import AgeAnnual
from .base_import_command import BaseImportCommand

class Command(BaseImportCommand):
    help = "Loads the data from CSV into AgeAnnual model"

    @transaction.atomic
    def handle(self, *args, **options):
        csv_file_path = options["csv_file"]

        AgeAnnual.objects.all().delete()
        age_annuals_data = parse_ageannuals_from_csv(csv_file_path)

        total_count = 0
        error_count = 0

        # Create AgeAnnual objects
        for data in age_annuals_data:
            try:
                AgeAnnual.objects.create(
                    number=data["number"],
                    alpha=data["alpha"],
                    description=data["description"],
                    explanation=data["explanation"],
                    )
                total_count += 1
            except IntegrityError as e:
                self.stdout.write(self.style.ERROR(f"Database integrity error for record {data['number']} - {data['alpha']}: {e}"))
                error_count += 1
            except DataError as e:
                self.stdout.write(self.style.ERROR(f"Data error for record {data['number']} - {data['alpha']}: {e}"))
                error_count += 1
            except Exception as e:
                self.stdout.write(self.style.ERROR(f"An error occurred for record {data['number']} - {data['alpha']}: {e}"))
                error_count += 1
        
        self.stdout.write(self.style.SUCCESS(f"Successfully loaded {total_count} AgeAnnual objects from {csv_file_path}"))

        if error_count > 0:
            self.stdout.write(self.style.ERROR(f"{error_count} errors occurred during data loading"))
        else:
            self.stdout.write(self.style.SUCCESS("No errors occurred during data loading"))