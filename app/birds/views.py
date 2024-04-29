from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy

from birds.forms import TaxonSelectForm

from birds.models import Taxon

class TaxonView(FormView):
    template_name = "birds/taxons.html"
    form_class = TaxonSelectForm
    
    def form_valid(self, form: TaxonSelectForm) -> Any:
        context = self.get_context_data()
        context["selected_taxon"] = form.cleaned_data["taxon"]
        return self.render_to_response(context)
