from django import forms
from birds.models import Taxon

class TaxonSelectForm(forms.Form):
    taxon = forms.ModelChoiceField(
        queryset=Taxon.objects.all().order_by("alpha"),
        empty_label="Select a taxon",
        label="Taxon",
        widget=forms.Select(attrs={"class": "form-control", "id": "id_taxon"}),
    )