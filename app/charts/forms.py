from django import forms

class DateForm(forms.Form):
    date_range = forms.CharField(
        widget=forms.TextInput(attrs={"type": "date"}),
        required=False,
    )
    
