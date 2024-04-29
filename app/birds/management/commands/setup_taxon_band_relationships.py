from django.core.management.base import BaseCommand
from django.db import transaction

from birds.models import Band
from birds.models import BandAllocation
from birds.models import Taxon


class Command(BaseCommand):
    help = "Sets up the many-to-many relationship between Taxon and Band"

    def handle(self, *args, **options):
        with transaction.atomic():
            all_taxons = Taxon.objects.all()

            for taxon in all_taxons:
                # Clear existing bands to prevent duplication
                taxon.bands.clear()

                # Get distinct Band ids used in allocations for the current taxon
                band_ids = BandAllocation.objects.filter(bird=taxon).values_list("band", flat=True).distinct()

                # Fetch the Band instances directly
                bands = Band.objects.filter(id__in=band_ids)

                # Add all bands to the Taxon's bands relationship
                taxon.bands.add(*bands)  # Use unpacking to add all bands at once

        self.stdout.write(self.style.SUCCESS("All Taxon to Band relationships have been set up successfully."))
