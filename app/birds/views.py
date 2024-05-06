from typing import Dict
from typing import List

from django.views.generic.edit import FormView

from birds.forms import TaxonSelectForm
from birds.models import AgeWRP
from birds.models import BandAllocation
from birds.models import Taxon


class TaxonView(FormView):
    template_name = "birds/taxons.html"
    form_class = TaxonSelectForm

    def form_valid(self, form: TaxonSelectForm):
        context = self.get_context_data()
        selected_taxon = form.cleaned_data["taxon"]
        context["selected_taxon"] = selected_taxon
        context["bands_by_sex"] = self.get_band_allocations_by_sex(selected_taxon)
        # Temporarily remove wing chord datat in favor of morphometrics
        # context["wing_chords"] = self.get_wing_chord_data(selected_taxon)
        context["morphometrics"] = self.get_morphometrics(selected_taxon)
        context["sexing_criteria"] = self.get_sexing_criteria(selected_taxon)
        context["wrp_data"] = self.get_wrp_data(selected_taxon)
        context["sexes"] = ["All", "Female", "Male"]

        return self.render_to_response(context)

    def get_band_allocations_by_sex(self, taxon: Taxon) -> Dict[str, List[str]]:
        band_allocations = BandAllocation.objects.filter(bird=taxon).select_related("band").order_by("sex", "priority")
        bands_by_sex: Dict[str, List[str]] = {
            "All": [],
            "Female": [],
            "Male": [],
        }

        for allocation in band_allocations:
            sex_label = {"m": "Male", "f": "Female", "u": "All"}.get(allocation.sex, "All")
            bands_by_sex[sex_label].append(allocation.band.size)

        return bands_by_sex

    def get_wing_chord_data(self, taxon: Taxon):
        wing_chord_data = {}

        # Check if the general taxon wing chord data exists
        if taxon.wing_min and taxon.wing_max:
            wing_chord_data["All"] = (taxon.wing_min, taxon.wing_max)

        # Check if the female taxon wing chord data exists
        if taxon.wing_female_min and taxon.wing_female_max:
            wing_chord_data["Female"] = (taxon.wing_female_min, taxon.wing_female_max)

        # Check if the male taxon wing chord data exists
        if taxon.wing_male_min and taxon.wing_male_max:
            wing_chord_data["Male"] = (taxon.wing_male_min, taxon.wing_male_max)

        # Check if general taxon tail data exists

        return wing_chord_data

    def get_morphometrics(self, taxon):
        morphometrics = {
            "wing": {"All": {}, "Female": {}, "Male": {}},
            "tail": {"All": {}, "Female": {}, "Male": {}},
        }

        # Populate wing data
        if taxon.wing_min and taxon.wing_max:
            morphometrics["wing"]["All"] = {"min": taxon.wing_min, "max": taxon.wing_max}
        if taxon.wing_female_min and taxon.wing_female_max:
            morphometrics["wing"]["Female"] = {"min": taxon.wing_female_min, "max": taxon.wing_female_max}
        if taxon.wing_male_min and taxon.wing_male_max:
            morphometrics["wing"]["Male"] = {"min": taxon.wing_male_min, "max": taxon.wing_male_max}

        # Populate tail data
        if taxon.tail_min and taxon.tail_max:
            morphometrics["tail"]["All"] = {"min": taxon.tail_min, "max": taxon.tail_max}
        if taxon.tail_female_min and taxon.tail_female_max:
            morphometrics["tail"]["Female"] = {"min": taxon.tail_female_min, "max": taxon.tail_female_max}
        if taxon.tail_male_min and taxon.tail_male_max:
            morphometrics["tail"]["Male"] = {"min": taxon.tail_male_min, "max": taxon.tail_male_max}

        return morphometrics

    def get_sexing_criteria(self, taxon):
        criteria = {
            "BP": taxon.sex_by_bp,
            "CP": taxon.sex_by_cp,
            "Plumage": taxon.sex_by_plumage,
            "Wing Chord": taxon.sex_by_wing,
        }
        formatted_criteria = {
            key: "YES" if value else "NO" if value is False else "N/A" for key, value in criteria.items()
        }
        return formatted_criteria

    def get_wrp_data(self, taxon):
        # Get the GroupWRPs associated with the selected taxon
        wrp_groups = taxon.wrp_groups.all()
        group_numbers = wrp_groups.values_list("number", flat=True)

        # Get the unique AgeWRPs across all the groups, ordered by sequence
        wrp_ages = (
            AgeWRP.objects.filter(
                wrp_groups__in=wrp_groups,
            )
            .distinct()
            .order_by("sequence")
            .values_list("code", flat=True)
        )

        # Organize these into a dictionary to pass to the template
        return {
            "wrp_groups": list(group_numbers),
            "wrp_ages": list(wrp_ages),
        }
