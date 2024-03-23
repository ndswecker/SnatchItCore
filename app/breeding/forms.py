from django import forms

from breeding.models import Status


class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = "__all__"
