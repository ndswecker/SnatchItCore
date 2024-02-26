from django import forms
from .models import CaptureRecord
from .birds_info import REFERENCE_GUIDE

class CaptureRecordForm(forms.ModelForm):
    class Meta:
        model = CaptureRecord
        fields = '__all__'
        exclude = ['alpha_code', 'discrepancies', 'is_flagged_for_review']
    
    def clean(self):
        cleaned_data = super().clean()
        species_name = cleaned_data.get('species_name')
        wing_chord = cleaned_data.get('wing_chord')

        species_info = REFERENCE_GUIDE.get(species_name)
        if species_info and wing_chord is not None:  # Check if wing_chord is not None
            wing_chord_range = species_info['wing_chord_range']
            if not (wing_chord_range[0] <= wing_chord <= wing_chord_range[1]):
                self.add_error('wing_chord', f'Wing chord for {species_info["common_name"]} must be between {wing_chord_range[0]} and {wing_chord_range[1]}.')

        return cleaned_data
