from django import forms
from django_select2 import forms as s2forms

from maps.choice_definitions import SPECIES_CHOICES
from maps.models import CaptureRecord


class CaptureRecordForm(forms.ModelForm):
    species_number = forms.ChoiceField(
        choices=SPECIES_CHOICES,
        widget=s2forms.Select2Widget(
            attrs={
                "class": "form-control",
            },
        ),
    )

    class Meta:
        model = CaptureRecord
        fields = "__all__"
        exclude = [
            "user",
            "bander_initials",
            "alpha_code",
            "discrepancies",
            "is_flagged_for_review",
        ]
