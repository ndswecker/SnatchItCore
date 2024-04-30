
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
        # Fetch band allocations and group by sex
        band_allocations = BandAllocation.objects.filter(bird=selected_taxon).select_related('band').order_by('sex', 'priority')
        bands_by_sex = {
            "Unisex": [],
            "Female": [],
            "Male": []
        }
        
        for allocation in band_allocations:
            sex_label = {"m": "Male", "f": "Female", "u": "Unisex"}.get(allocation.sex, "Unisex")
            bands_by_sex[sex_label].append(allocation.band.size)

        context["bands_by_sex"] = bands_by_sex
        
        return self.render_to_response(context)
    