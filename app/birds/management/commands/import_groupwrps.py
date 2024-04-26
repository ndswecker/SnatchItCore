from django.core.management.base import BaseCommand
from django.db import transaction
from django.db.utils import DataError
from django.db.utils import IntegrityError

from birds.models import AgeWRP
from birds.models import GroupWRP
from birds.serializers import parse_groupwrps_from_csv


class Command(BaseCommand):
    help = "Loads data from CSV into GroupWRP model"

    def add_arguments(self, parser):
        parser.add_argument("csv_file", type=str, help="The CSV file to load data from")

    @transaction.atomic
    def handle(self, *args, **options):
        csv_file_path = options["csv_file"]
        try:
            GroupWRP.objects.all().delete()
            group_wrps_data = parse_groupwrps_from_csv(csv_file_path)

            # Create GroupWRP objects and link age wrps atomically
            for data in group_wrps_data:
                group_wrp = GroupWRP.objects.create(
                    number=data["number"],
                    explanation=data["explanation"],
                )
                group_wrp.ages.set(data["ages"])  # Set many-to-many field

            self.stdout.write(
                self.style.SUCCESS(f"Successfully loaded {len(group_wrps_data)} GroupWRP objects from {csv_file_path}")
            )
        except IntegrityError as e:
            self.stdout.write(self.style.ERROR(f"An error occurred while attempting ito import WRP groups: {e}"))
        except DataError as e:
            self.stdout.write(self.style.ERROR(f"An error occurred while attempting to import WRP groups: {e}"))
        except AgeWRP.DoesNotExist as e:
            self.stdout.write(self.style.ERROR(f"No such WRP age code: {e}"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"An error occurred: {e}"))
