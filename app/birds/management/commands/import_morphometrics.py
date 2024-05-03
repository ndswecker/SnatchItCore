from django.db import transaction
from django.db.utils import DataError
from django.db.utils import IntegrityError

from birds.management.commands.base_import_command import BaseImportCommand
from birds.models import Taxon
from birds.serializers import parse_morphometrics_from_csv

class Command(BaseImportCommand):
    help = "Loads data from CSV into Taxon model"

    def create_morphometric(self, morphometric_data):
        updated_count = 0
        failed_morphometrics = []
        for data in morphometric_data:
            try:
                taxon = Taxon.objects.get(number=data["number"])
                # Update all relevant fields
                taxon.wing_female_min = data["wing_female_min"]
                taxon.wing_female_max = data["wing_female_max"]
                taxon.wing_male_min = data["wing_male_min"]
                taxon.wing_male_max = data["wing_male_max"]
                taxon.tail_female_min = data["tail_female_min"]
                taxon.tail_female_max = data["tail_female_max"]
                taxon.tail_male_min = data["tail_male_min"]
                taxon.tail_male_max = data["tail_male_max"]
                taxon.save()
                updated_count += 1
            except Taxon.DoesNotExist:
                failed_morphometrics.append(data["alpha"])
            except IntegrityError as e:
                failed_morphometrics.append(f"Database error for Taxon number {data['number']}: {e}")
        return updated_count, failed_morphometrics
    
    def handle(self, *args, **options):
        csv_file_path = options['csv_file']
        morphometrics_data = parse_morphometrics_from_csv(csv_file_path)

        with transaction.atomic():
            updated_count, failed_morphometrics = self.create_morphometric(morphometrics_data)

        if updated_count:
            self.stdout.write(self.style.SUCCESS(f"Successfully updated {updated_count} Taxon objects"))

        if failed_morphometrics:
            self.stdout.write(self.style.ERROR(f"Failed to update the following Taxon objects: {', '.join(failed_morphometrics)}"))