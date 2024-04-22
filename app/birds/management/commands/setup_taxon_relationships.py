from django.core.management.base import BaseCommand
from django.db import transaction
from birds.models import Taxon
from birds.models import GroupWRP

from maps.maps_reference_data import SPECIES


class Command(BaseCommand):
    help = "Set up wrp relationships and various details for each taxon"

    def handle(self, *args, **options):
        with transaction.atomic():
            for species_id, data, in SPECIES.items():
                try:
                    taxon = Taxon.objects.get(number=data["species_number"])
                    taxon.wrp_groups.clear()
                    for group_number in data["WRP_groups"]:
                        group = GroupWRP.objects.get(number=group_number)
                        taxon.wrp_groups.add(group)
                    self.stdout.write(self.style.SUCCESS(f"Successfully updated WRP groups for {taxon.common} ({taxon.alpha})."))

                    # If a page number exists, add it to the Taxon's page_number
                    if "pyle_second_edition_page" in data and data["pyle_second_edition_page"] != None:
                        taxon.page_number = data["pyle_second_edition_page"]
                        taxon.save()
                    
                    # Asign unisex wing chord range
                    if "wing_chord_range" in data and len(data["wing_chord_range"]) == 2:
                        taxon.wing_min = data["wing_chord_range"][0]
                        taxon.wing_max = data["wing_chord_range"][1]
                        taxon.save()
                    
                    # Asign sex specific wing chord ranges 
                    if "wing_chord_range_by_sex" in data:
                        if "female" in data["wing_chord_range_by_sex"]:
                            taxon.wing_female_min = data["wing_chord_range_by_sex"]["female"][0]
                            taxon.wing_female_max = data["wing_chord_range_by_sex"]["female"][1]
                        if "male" in data["wing_chord_range_by_sex"]:
                            taxon.wing_male_min = data["wing_chord_range_by_sex"]["male"][0]
                            taxon.wing_male_max = data["wing_chord_range_by_sex"]["male"][1]

                    # Asign sexing criteria
                    if "sexing_criteria" in data:
                        taxon.sex_by_bp = data["sexing_criteria"]["female_by_BP"]
                        taxon.sex_by_cp = data["sexing_criteria"]["male_by_CP"]
                        taxon.sex_by_plumage = data["sexing_criteria"]["plumage_dimorphism"]

                    taxon.save()
                
                except Taxon.DoesNotExist:
                    self.stdout.write(self.style.ERROR(f"Taxon with number {species_id} not found"))
                except GroupWRP.DoesNotExist:
                    self.stdout.write(self.style.ERROR(f"Group with number {group_number} not found"))
        
        self.stdout.write(self.style.SUCCESS("All WRP group relationships have been set up successfully."))