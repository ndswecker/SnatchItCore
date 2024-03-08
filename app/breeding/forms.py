from django import forms

from breeding.models import BreedingRecord


class BreedingRecordForm(forms.ModelForm):
    class Meta:
        model = BreedingRecord
        fields = "__all__"
        exclude = [
            "user",
        ]
