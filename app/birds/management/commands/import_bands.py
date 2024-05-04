from django.db import transaction
from django.db.utils import DataError
from django.db.utils import IntegrityError

from birds.models import Band
from birds.serializers import parse_bands_from_csv
from birds.management.commands.base_import_command import BaseImportCommand


class Command(BaseImportCommand):
    help = "Loads the data from CSV into Band model"

    @transaction.atomic
    def handle(self, *args, **options):
        csv_file_path = options["csv_file"]
        Band.objects.all().delete()
        bands_data = parse_bands_from_csv(csv_file_path)

        bands = [
            Band(
                size=data["size"],
                comment=data["comment"],
            )
            for data in bands_data
        ]

        try:
            Band.objects.bulk_create(bands)
            self.stdout.write(
                self.style.SUCCESS(f"Successfully loaded {len(bands_data)} Band objects from {csv_file_path}"),
            )
        except IntegrityError as e:
            self.stdout.write(self.style.ERROR(f"An error occurred while attempting to load a Band object: {e}"))
        except DataError as e:
            self.stdout.write(self.style.ERROR(f"An error occurred while attempting to load a Band object: {e}"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"An error occurred while attempting to load a Band object: {e}"))
