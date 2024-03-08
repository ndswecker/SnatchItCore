from django import forms

from netting.models import NettingRecord


class NettingRecordForm(forms.ModelForm):
    class Meta:
        model = NettingRecord
        fields = "__all__"
        exclude = [
            "user",
        ]
