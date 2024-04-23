import logging
from django.core.management.base import BaseCommand
from django.db import transaction
from django.db.utils import IntegrityError
from django.db.utils import DataError
from birds.serializers import parse_ageannuals_from_csv
from birds.models import AgeAnnual

class Command(BaseCommand):
    help = "Loads the data from CSV into AgeAnnual model"

    def add_arguments(self, parser):
        parser.add_argument("csv_file", type=str, help="The CSV file to load data from")

    @transaction.atomic
    def handle(self, *args, **options):
        logger = logging.getLogger(__name__)
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
                logger.error(f"Database integrity error for record {data["number"]} - {data["alpha"]}: {e}")
                error_count += 1
            except DataError as e:
                logger.error(f"Data error for record {data["number"]} - {data["alpha"]}: {e}")
                error_count += 1
            except Exception as e:
                logger.error(f"An error occurred for record {data["number"]} - {data["alpha"]}: {e}")
                error_count += 1
        
        logger.info(f"Successfully loaded {total_count} AgeAnnual objects from {csv_file_path}")
        if error_count > 0:
            logger.error(f"{error_count} errors occurred during data loading. Check logs for details.")
        else:
            logger.info("No errors occurred during data loading")