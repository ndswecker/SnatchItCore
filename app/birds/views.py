
from django.views.generic.edit import FormView
from django.views.generic.detail import DetailView

from birds.forms import TaxonSelectForm
from birds.models import Taxon
from birds.models import BandAllocation


class TaxonView(FormView):
    template_name = "birds/taxons.html"
    form_class = TaxonSelectForm
    
    def form_valid(self, form: TaxonSelectForm):
        context = self.get_context_data()
        selected_taxon = form.cleaned_data["taxon"]
        context["selected_taxon"] = selected_taxon
        context["bands_by_sex"] = self.get_band_allocations_by_sex(selected_taxon)
        context["wing_chords"] = self.get_wing_chord_data(selected_taxon)
        context["sexing_criteria"] = self.get_sexing_criteria(selected_taxon)
        
        return self.render_to_response(context)
    
    def get_band_allocations_by_sex(self, taxon: Taxon):
        band_allocations = BandAllocation.objects.filter(bird=taxon).select_related('band').order_by('sex', 'priority')
        bands_by_sex = {
            "All": [],
            "Female": [],
            "Male": []
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

        return wing_chord_data
    
    def get_sexing_criteria(self, taxon):
        criteria = {
            "BP": taxon.sex_by_bp,
            "CP": taxon.sex_by_cp,
            "Plumage": taxon.sex_by_plumage,
            "Wing Chord": taxon.sex_by_wing,
        }
        formatted_criteria = {key: "YES" if value else "NO" if value is False else "N/A" for key, value in criteria.items()}
        return formatted_criteria
