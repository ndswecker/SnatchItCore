from allauth.account.forms import SignupForm
from django import forms
from django.core.validators import MinLengthValidator


class FirstLastSignupForm(SignupForm):
    first_name = forms.CharField(
        required=True,
        max_length=30,
        validators=[MinLengthValidator(2)],
        widget=forms.TextInput(attrs={"placeholder": "First Name"}),
    )
    last_name = forms.CharField(
        required=True,
        max_length=30,
        validators=[MinLengthValidator(2)],
        widget=forms.TextInput(attrs={"placeholder": "Last Name"}),
    )
