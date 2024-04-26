from django.core.management.base import BaseCommand
from django.db import transaction
from django.db.utils import DataError
from django.db.utils import IntegrityError

from birds.models import Band
from birds.serializers import parse_bands_from_csv


class Command(BaseCommand):
    help = "Loads the data from CSV into Band model"

    def add_arguments(self, parser):
        parser.add_argument("csv_file", type=str, help="The CSV file to load data from")

    @transaction.atomic
    def handle(self, *args, **options):
        csv_file_path = options["csv_file"]
        try:
            Band.objects.all().delete()
            bands_data = parse_bands_from_csv(csv_file_path)

            # Create Band objects
            for data in bands_data:
                Band.objects.create(
                    size=data["size"],
                    comment=data["comment"],
                )

            self.stdout.write(
                self.style.SUCCESS(f"Successfully loaded {len(bands_data)} Band objects from {csv_file_path}"),
            )
        except IntegrityError as e:
            self.stdout.write(self.style.ERROR(f"An error occurred while attempting to load a Band object: {e}"))
        except DataError as e:
            self.stdout.write(self.style.ERROR(f"An error occurred while attempting to load a Band object: {e}"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"An error occurred while attempting to laod a Band object: {e}"))
