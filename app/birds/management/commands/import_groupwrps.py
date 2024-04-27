from django.core.management.base import BaseCommand
from birds.management.commands.base_import_command import BaseImportCommand
from django.db import transaction
from django.db.utils import DataError
from django.db.utils import IntegrityError

from birds.models import AgeWRP
from birds.models import GroupWRP
from birds.serializers import parse_groupwrps_from_csv


class Command(BaseImportCommand):
    help = "Loads data from CSV into GroupWRP model"

    def create_group_wrp(self, data):
        try:
            group_wrp = GroupWRP.objects.create(
                number=data["number"],
                explanation=data["explanation"],
            )
            return group_wrp, None
        except (IntegrityError, DataError) as e:
            return None, str(e)
        
    def link_ages_to_group_wrp(self, group_wrp, age_codes):
        failed_ages = []
        age_wrps = []
        for code in age_codes:
            try:
                age_wrp = AgeWRP.objects.get(code=code)
                age_wrps.append(age_wrp)
            except AgeWRP.DoesNotExist:
                failed_ages.append(code)
        group_wrp.ages.set(age_wrps)

        return failed_ages
    
    def report_results(self, success_count, failed_groups, failed_ages):
        if success_count:
            self.stdout.write(
                self.style.SUCCESS(f"Successfully loaded {success_count} GroupWRP objects"),
            )
        if failed_groups:
            self.stdout.write(self.style.WARNING(f"Failed to create the following GroupWRP objects: {failed_groups}"))
        if failed_ages:
            self.stdout.write(self.style.WARNING(f"Failed to recognize the following AgeWRP codes: {failed_ages}"))

    @transaction.atomic
    def handle(self, *args, **options):
        csv_file_path = options["csv_file"]
        group_wrps_data = parse_groupwrps_from_csv(csv_file_path)
        failed_groups = []
        failed_ages = []

        GroupWRP.objects.all().delete()

        for data in group_wrps_data:
            group_wrp, error = self.create_group_wrp(data)
            if group_wrp:
                failed_ages.extend(self.link_ages_to_group_wrp(group_wrp, data["ages"]))
            else:
                failed_groups.append(data["number"])

        self.report_results(len(group_wrps_data) - len(failed_groups), failed_groups, failed_ages)
