from django.core.management.base import BaseCommand
from django.db import transaction

from birds.models import GroupWRP
from birds.models import Taxon
from maps.maps_reference_data import SPECIES


class Command(BaseCommand):
    help = "Set up wrp relationships and various details for each taxon"

    def handle (self, *args, **options):
        rejected_taxons, rejected_groups = self.process_taxons()
        self.report_results(rejected_taxons, rejected_groups)

    def get_taxon(self, data):
        try:
            return Taxon.objects.get(number=data["species_number"])
        except Taxon.DoesNotExist:
            return None
        
    def get_group(self, number):
        try:
            return GroupWRP.objects.get(number=number)
        except GroupWRP.DoesNotExist:
            return None
        
    def process_taxon_groups(self, taxon, data, rejected_groups):
        taxon.wrp_groups.clear()
        for group_number in data["WRP_groups"]:
            group = self.get_group(group_number)
            if group:
                taxon.wrp_groups.add(group)
            else:
                rejected_groups.append(group_number)

    def update_taxon_details(self, taxon, data):
        self.update_page_number(taxon, data)
        self.update_wing_chords(taxon, data)
        self.update_sexing_criteria(taxon, data)
        taxon.save()

    def update_page_number(self, taxon, data):
        if "pyle_second_edition_page" in data:
            taxon.page_number = data["pyle_second_edition_page"]
    
    def update_wing_chords(self, taxon, data):
        # Unisexed wing chord range assignments
        wing_chord_range = data.get("wing_chord_range")
        if wing_chord_range and len(wing_chord_range) == 2:
            taxon.wing_min, taxon.wing_max = wing_chord_range
        # Sexed wing chord range assignments
        if "wing_chord_range_by_sex" in data:
            for sex, values in data["wing_chord_range_by_sex"].items():
                if len(values) == 2:
                    setattr(taxon, f"wing_{sex}_min", values[0])
                    setattr(taxon, f"wing_{sex}_max", values[1])

    def update_sexing_criteria(self, taxon, data):
        criteria = data.get("sexing_criteria")
        if "female_by_BP" in criteria:
            taxon.sex_by_bp = criteria["female_by_BP"]
        if "male_by_CP" in criteria:
            taxon.sex_by_cp = criteria["male_by_CP"]
        if "plumage_dimorphism" in criteria:
            taxon.sex_by_plumage = criteria["plumage_dimorphism"]
    
    def process_taxons(self):
        rejected_taxons = []
        rejected_groups = []
        with transaction.atomic():
            for value in SPECIES.values():
                taxon = self.get_taxon(value)
                if taxon:
                    self.process_taxon_groups(taxon, value, rejected_groups)
                    self.update_taxon_details(taxon, value)
                else:
                    rejected_taxons.append(value["common_name"])
        return rejected_taxons, rejected_groups

    def report_results(self, rejected_taxons, rejected_groups):
        if rejected_taxons:
            self.stdout.write(self.style.WARNING(f"Failed to set up taxon relationships for the following {rejected_taxons}"))
        if rejected_groups:
            self.stdout.write(self.style.WARNING(f"Failed to recognize WRP groups: {rejected_groups}"))
        self.stdout.write(self.style.SUCCESS("All WRP group relationships have been set up successfully."))   

