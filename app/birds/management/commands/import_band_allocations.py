from birds.management.commands.base_import_command import BaseImportCommand
from birds.models import Band
from birds.models import BandAllocation
from birds.models import Taxon
from birds.serializers import parse_band_allocations_from_csv


class Command(BaseImportCommand):
    help = "Loads band allocation data from CSV"

    def handle(self, *args, **options):
        BandAllocation.objects.all().delete()

        csv_file_path = options["csv_file"]
        band_allocations = parse_band_allocations_from_csv(csv_file_path)

        # Prepare caches for Taxon and Band objects to avoid repeated queries
        taxon_cache = {taxon.number: taxon for taxon in Taxon.objects.all()}
        band_cache = {band.size: band for band in Band.objects.all()}

        new_band_allocations = []
        rejected_birds = set()
        rejected_bands = set()

        for allocation in band_allocations:
            taxon = taxon_cache.get(allocation["bird"])
            if not taxon:
                rejected_birds.add(allocation["common"])
                continue
            band = band_cache.get(allocation["band"])
            if not band:
                rejected_bands.add(allocation["band"])
                continue

            new_band_allocations.append(
                BandAllocation(
                    bird=taxon,
                    band=band,
                    sex=allocation["sex"],
                    priority=allocation["priority"],
                ),
            )

        BandAllocation.objects.bulk_create(new_band_allocations)

        if rejected_birds:
            self.stdout.write(
                self.style.WARNING(
                    f"Failed to load BandAllocation objects for the following birds:\n {', '.join(map(str, rejected_birds))}",  # noqa E501
                ),
            )

        if rejected_bands:
            self.stdout.write(
                self.style.WARNING(
                    f"Failed to load BandAllocation objects for the following bands: {', '.join(rejected_bands)}",
                ),
            )

        self.stdout.write(
            self.style.SUCCESS(
                f"Successfully loaded {len(new_band_allocations)} BandAllocation objects from {csv_file_path}",
            ),
        )
