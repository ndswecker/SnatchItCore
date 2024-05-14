from django.db import transaction
from django.db.utils import IntegrityError
from django.db.utils import DataError

from birds.models import Taxon
from birds.serializers import parse_species_from_csv
from birds.management.commands.base_import_command import BaseImportCommand


class Command(BaseImportCommand):
    help = "Loads the data from BBL CSV into Species model"

    @transaction.atomic
    def handle(self, *args, **options):
        Taxon.objects.all().delete()

        csv_file_path = options["csv_file"]
        species_data = parse_species_from_csv(csv_file_path)

        new_taxa = [
            Taxon(
                common=data["common"],
                scientific=data["scientific"],
                alpha=data["alpha"],
                alpha_bbl=data["alpha"],
                number=data["number"],
                number_bbl=data["number"],
                taxonomic_order=data["taxonomic_order"],
            )
            for data in species_data
        ]

        try:
            Taxon.objects.bulk_create(new_taxa)
            self.stdout.write(
                self.style.SUCCESS(f"Successfully loaded {len(species_data)} Species objects from {csv_file_path}"),
            )
        except IntegrityError as e:
            self.stdout.write(self.style.ERROR(f"An error occurred while attempting to load a Species object: {e}"))
        except DataError as e:
            self.stdout.write(self.style.ERROR(f"An error occurred while attempting to load a Species object: {e}"))
