import json
from django.core.management.base import BaseCommand, CommandParser
from django.db import transaction
from birds.models import Taxon
from birds.models import GroupWRP


class Command(BaseCommand):
    help = "Set up the wrp group relationships for each taxon"

    def add_arguments(self, parser):
        parser.add_argument("data_file", type=str, help="The CSV file to load data from")

    def handle(self, *args, **options):
        data_file = options["data_file"]
        try:
            with open(data_file) as file:
                data = json.load(file)
                species_dict = data["SPECIES"]
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f"File not found: {data_file}"))
            return