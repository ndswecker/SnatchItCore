from django.core.management.base import BaseCommand, CommandParser
from django.db import transaction

from birds.serializers import parse_band_allocations_from_csv
from birds.models import BandAllocation
from birds.models import Band
from birds.models import Taxon

class Command(BaseCommand):
    help = "Loads band allocation data from CSV"

    def add_arguments(self, parser):
        parser.add_argument("csv_file", type=str, help="The CSV file to load data")
    
    def handle(self, *args, **options):
        csv_file_path = options["csv_file"]
        band_allocations = parse_band_allocations_from_csv(csv_file_path)

        with transaction.atomic():
            for bands in band_allocations:
                taxon = Taxon.objects.filter(number=bands["bird"]).first()
                if not taxon:
                    self.stdout.write(self.style.ERROR(f"Taxon with number {bands['bird']} not found"))
                    continue
                
                band, created = Band.objects.get_or_create(size=bands["band"])

                BandAllocation.objects.create(
                    bird=taxon,
                    band=band,
                    sex=bands["sex"],
                    priority=bands["priority"],
                )
        self.stdout.write(self.style.SUCCESS(f"Successfully loaded {len(band_allocations)} BandAllocation objects from {csv_file_path}"))