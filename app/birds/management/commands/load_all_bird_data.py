from django.core.management import call_command
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Loads all data from CSV files into the database"

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("Loading all band sizes..."))
        call_command("import_bands", "./data/Bands.csv")

        self.stdout.write(self.style.SUCCESS("Loading all Annual age options..."))
        call_command("import_ageannuals", "./data/AgeAnnuals.csv")

        self.stdout.write(self.style.SUCCESS("Loading WRP age options..."))
        call_command("import_agewrps", "./data/AgeWRPs.csv")

        self.stdout.write(self.style.SUCCESS("Loading all WRP Groups..."))
        call_command("import_groupwrps", "./data/GroupWRPs.csv")

        self.stdout.write(self.style.SUCCESS("Loading all species data from BBL..."))
        call_command("import_species", "./data/TaxonBBL.csv")

        self.stdout.write(self.style.SUCCESS("Loading all band allocations from BBL..."))
        call_command("import_band_allocations", "./data/BandAllocations.csv")

        self.stdout.write(self.style.SUCCESS("Set species to band relationships..."))
        call_command("setup_taxon_band_relationships")

        self.stdout.write(self.style.SUCCESS("Loading all morphometric data..."))
        call_command("import_morphometrics", "./data/Morphometrics.csv")

        self.stdout.write(self.style.SUCCESS("Set species details from reference data"))
        call_command("setup_taxon_relationships")

        self.stdout.write(self.style.SUCCESS("Successfully loaded all data"))
