from django import forms

from .birds_info import REFERENCE_GUIDE
from .models import CaptureRecord


class CaptureRecordForm(forms.ModelForm):
    class Meta:
        model = CaptureRecord
        fields = "__all__"
        exclude = ["alpha_code", "discrepancies", "is_flagged_for_review"]
