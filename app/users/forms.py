from allauth.account.forms import SignupForm
from django import forms
from django.core.validators import MinLengthValidator
from django.db import IntegrityError
from django.db import transaction

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
    initials = forms.CharField(
        required=True,
        max_length=3,
        validators=[MinLengthValidator(3)],
        widget=forms.TextInput(attrs={"placeholder": "Initials"}),
    )

    def clean_initials(self):
        initials = self.cleaned_data["initials"].upper()

        if User.objects.filter(initials=initials).exists():
            raise forms.ValidationError("Initials already in use. Please choose another.")

        return initials
    
    def save(self, request):
        user = super(FirstLastSignupForm, self).save(request)
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.initials = self.cleaned_data["initials"]
        
        try:
            with transaction.atomic():
                user.save()
        except IntegrityError:
            self.add_error('initials', 'Initials already in use. Please choose another.')
            return None
        
        return user


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
