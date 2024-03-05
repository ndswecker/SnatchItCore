from allauth.account.forms import SignupForm
from django import forms
from django.core.validators import MinLengthValidator

from users.models import User


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


class EmailChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "email",
        ]
        widgets = {
            "email": forms.EmailInput(
                attrs={
                    "placeholder": "New Email",
                    "class": "form-control",
                    "autocomplete": "email",
                    "autofocus": True,
                },
            ),
        }
