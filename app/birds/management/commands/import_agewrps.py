from django.db import transaction

from birds.management.commands.base_import_command import BaseImportCommand
from birds.models import AgeAnnual
from birds.models import AgeWRP
from birds.serializers import parse_agewrps_from_csv


class Command(BaseImportCommand):
    help = "Loads data from CSV into AgeWRP model"

    def handle(self, *args, **options):
        csv_file_path = options["csv_file"]
        age_wrps_data = parse_agewrps_from_csv(csv_file_path)
        annuals = AgeAnnual.objects.all()
        annual_cache = {annual.number: annual for annual in annuals}

        with transaction.atomic():
            AgeWRP.objects.all().delete()
            new_age_wrps = [
                AgeWRP(
                    code=data["code"],
                    sequence=data["sequence"],
                    description=data["description"],
                    status=data["status"],
                )
                for data in age_wrps_data
            ]
            AgeWRP.objects.bulk_create(new_age_wrps)

            new_age_wrps = {wrp.code: wrp for wrp in AgeWRP.objects.all()}
            for data in age_wrps_data:
                age_wrp = new_age_wrps[data["code"]]
                annual_ids = data["annuals"]
                age_wrp.annuals.add(*[annual_cache[annual_id] for annual_id in annual_ids if annual_id in annual_cache])

        self.stdout.write(
            self.style.SUCCESS(f"Successfully loaded {len(new_age_wrps)} AgeWRP objects from {csv_file_path}"),
        )
