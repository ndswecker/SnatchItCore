from django.core.exceptions import ObjectDoesNotExist
from django.core.management.base import BaseCommand
from django.db import transaction

from birds.models import Band
from birds.models import BandAllocation
from birds.models import Taxon
from birds.serializers import parse_band_allocations_from_csv


class Command(BaseCommand):
    help = "Loads band allocation data from CSV"

    def add_arguments(self, parser):
        parser.add_argument("csv_file", type=str, help="The CSV file to load data")

    def handle(self, *args, **options):
        csv_file_path = options["csv_file"]
        band_allocations = parse_band_allocations_from_csv(csv_file_path)

        rejected_birds = []
        rejected_bands = []

        with transaction.atomic():
            for bands in band_allocations:
                # Not all birds in this csv are appropriate for this dataset
                try:
                    taxon = Taxon.objects.get(number=bands["bird"])
                except ObjectDoesNotExist:
                    rejected_birds.append(bands["bird"])
                    continue
                try:
                    band = Band.objects.get(size=bands["band"])
                except ObjectDoesNotExist:
                    rejected_bands.append(bands["band"])
                    continue
                BandAllocation.objects.create(
                    bird=taxon,
                    band=band,
                    sex=bands["sex"],
                    priority=bands["priority"],
                )

        if rejected_birds:
            self.stdout.write(
                self.style.WARNING(f"Failed to load BandAllocation objects for the following birds: {rejected_birds}"),
            )
        if rejected_bands:
            self.stdout.write(
                self.style.WARNING(f"Failed to load BandAllocation objects for the following bands: {rejected_bands}"),
            )

        self.stdout.write(
            self.style.SUCCESS(
                f"Successfully loaded {len(band_allocations)} BandAllocation objects from {csv_file_path}",
            ),
        )
