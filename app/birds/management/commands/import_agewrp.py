import csv
from django.core.management.base import BaseCommand
from django.db import transaction
from birds.models import AgeWRP, AgeAnnual

class Command(BaseCommand):
    help = "Loads data from CSV into AgeWRP model"

    def add_arguments(self, parser):
        parser.add_argument("csv_file", type=str, help="The CSV file to load data from")

    @transaction.atomic
    def handle(self, *args, **options):
        csv_file = options["csv_file"]
        try:
            with open(csv_file, newline="", encoding="utf-8") as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    age_wrps = AgeWRP.objects.create(
                        code=row["code"],
                        sequence=int(row["sequence"]),
                        description=row["description"],
                        status=row["status"].lower()  # Assuming status in CSV is either 'current' or 'discontinued'
                    )

                    # Handle ManyToMany relation for `annuals`
                    annual_ids = row.get("annuals", "")
                    if annual_ids:  # Only process if annual_ids is not empty
                        for annual_id in annual_ids.split(","):
                            if annual_id.strip():
                                annual, _ = AgeAnnual.objects.get_or_create(number=int(annual_id.strip()))
                                age_wrps.annuals.add(annual)

            self.stdout.write(self.style.SUCCESS("Data loaded successfully"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Error loading data: {e}"))
            raise e
