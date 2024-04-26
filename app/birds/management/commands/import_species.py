from django.core.management.base import BaseCommand
from django.core.management.base import CommandParser
from django.db import transaction

from birds.models import Taxon
from birds.serializers import parse_band_allocations_from_csv
from birds.serializers import parse_species_from_csv


class Command(BaseCommand):
    help = "Loads the data from BBL CSV into Species model"

    def add_arguments(self, parser):
        parser.add_argument("csv_file", type=str, help="The CSV file to load data from")

    @transaction.atomic
    def handle(self, *args, **options):
        csv_file_path = options["csv_file"]
        try:
            Taxon.objects.all().delete()
            species_data = parse_species_from_csv(csv_file_path)

            # Create Species objects
            for data in species_data:
                Taxon.objects.create(
                    common=data["common"],
                    scientific=data["scientific"],
                    alpha=data["alpha"],
                    alpha_bbl=data["alpha"],
                    number=data["number"],
                    number_bbl=data["number"],
                    taxonomic_order=data["taxonomic_order"],
                )

            self.stdout.write(
                self.style.SUCCESS(f"Successfully loaded {len(species_data)} Species objects from {csv_file_path}"),
            )
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"An error occurred: {e}"))
