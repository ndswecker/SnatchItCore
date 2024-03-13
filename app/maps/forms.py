from django import forms
from django_select2 import forms as s2forms

from maps.maps_reference_data import SPECIES, WRP_GROUPS
from maps.choice_definitions import SPECIES_CHOICES
from maps.models import CaptureRecord
from maps.validators import CaptureRecordFormValidator


class CaptureRecordForm(forms.ModelForm):
    species_number = forms.ChoiceField(
        choices=SPECIES_CHOICES,
        widget=s2forms.Select2Widget(attrs={"class": "form-control"}),
    )

    is_validated = forms.BooleanField(
        required=False,  # Make the field not required
        label="Override Validation",  # Label for the field
        initial=False,  # Set the default value to False
        widget=forms.CheckboxInput(attrs={"class": "form-check-input"})  # Define the widget and its class
    )

    class Meta:
        model = CaptureRecord
        fields = "__all__"
        exclude = ["user", "bander_initials", "alpha_code", "discrepancies"]

    # Users should not be filling in the alpha_code field, so we will fill it in for them
    def _clean_alpha_code(self):
        if self.instance.species_number:
            self.instance.alpha_code = SPECIES[self.instance.species_number]["alpha_code"]

    def _clean_how_aged_order(self):
        if self.instance.how_aged_2 and not self.instance.how_aged_1:
            self.instance.how_aged_1 = self.instance.how_aged_2
            self.instance.how_aged_2 = None

    def _clean_how_sexed_order(self):
        if self.instance.how_sexed_2 and not self.instance.how_sexed_1:
            self.instance.how_sexed_1 = self.instance.how_sexed_2
            self.instance.how_sexed_2 = None

    def clean(self) -> dict:
        cleaned_data = super().clean()
        self._clean_alpha_code()
        self._clean_how_aged_order()
        self._clean_how_sexed_order()

        validator = CaptureRecordFormValidator(cleaned_data=cleaned_data)
        validator.validate(override_validation=cleaned_data["is_validated"])
        self.instance.discrepancies = validator.discrepancy_string
        return cleaned_data
