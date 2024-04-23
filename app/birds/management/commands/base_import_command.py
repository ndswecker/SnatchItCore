import logging
from django.core.management.base import BaseCommand, CommandParser

class BaseImportCommand(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("csv_file", type=str, help="The CSV file to load data from")
    
    def handle(self, *args, **options):
        raise NotImplementedError("Subclasses must implement this method")