from django import forms
from birds.models import Taxon

class CustomLabelModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return f"{obj.alpha} - {obj.common}"

class TaxonSelectForm(forms.Form):
    taxon = CustomLabelModelChoiceField(
        queryset=Taxon.objects.all().order_by("alpha"),
        empty_label="Select a taxon",
        label="Taxon",
        widget=forms.Select(attrs={"class": "form-control", "id": "id_taxon"}),
    )