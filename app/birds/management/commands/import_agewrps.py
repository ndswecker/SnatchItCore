from django.db.utils import DataError
from django.db.utils import IntegrityError

from birds.management.commands.base_import_command import BaseImportCommand
from birds.models import AgeAnnual
from birds.models import AgeWRP
from birds.serializers import parse_agewrps_from_csv


class Command(BaseImportCommand):
    help = "Loads data from CSV into AgeWRP model"

    def create_age_wrps(self, age_wrps_data):
        success_count = 0
        annual_cache = {}
        failed_wrps = []
        failed_annuals = []

        # For each AgeWRP data object, create an AgeWRP object
        for data in age_wrps_data:
            try:
                age_wrp = AgeWRP.objects.create(
                    code=data["code"],
                    sequence=data["sequence"],
                    description=data["description"],
                    status=data["status"],
                )
                success_count += 1
                # If successful, add the annuals to the AgeWRP object
                failed_annuals.extend(self.link_annuals_to_wrp(age_wrp, data["annuals"], annual_cache))
            except (IntegrityError, DataError):
                failed_wrps.append(data["code"])

        return success_count, failed_wrps, failed_annuals

    def link_annuals_to_wrp(self, age_wrp, annual_ids, cache):
        failed_annuals = []
        annual_ages = []
        # For each annual id, get the AgeAnnual object from the cache
        for number in annual_ids:
            if number not in cache:
                try:
                    cache[number] = AgeAnnual.objects.get(number=number)
                except AgeAnnual.DoesNotExist:
                    failed_annuals.append(number)
                    continue
            annual_ages.append(cache[number])
        age_wrp.annuals.set(annual_ages)
        return failed_annuals

    def report_results(self, csv_file_path, success_count, failed_wrps, failed_annuals):
        self.stdout.write(
            self.style.SUCCESS(f"Successfully loaded {success_count} AgeWRP objects from {csv_file_path}"),
        )
        if failed_wrps:
            self.stdout.write(
                self.style.WARNING(f"Failed to load AgeWRP objects for the following WRP codes: {failed_wrps}"),
            )

        if failed_annuals:
            self.stdout.write(
                self.style.WARNING(f"Failed to load AgeWRP objects for the following annuals: {failed_annuals}"),
            )

    def handle(self, *args, **options):
        csv_file_path = options["csv_file"]
        AgeWRP.objects.all().delete()
        age_wrps_data = parse_agewrps_from_csv(csv_file_path)

        success_count, failed_wrps, failed_annuals = self.create_age_wrps(age_wrps_data)

        self.report_results(csv_file_path, success_count, failed_wrps, failed_annuals)
