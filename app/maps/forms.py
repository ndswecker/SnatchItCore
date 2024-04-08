import datetime

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Column
from crispy_forms.layout import Fieldset
from crispy_forms.layout import Layout
from crispy_forms.layout import Row
from crispy_forms.layout import Submit
from crispy_forms.layout import Button
from django import forms
from django.utils import timezone

from maps.choice_definitions import CAPTURE_CODE_CHOICES
from maps.choice_definitions import SPECIES_CHOICES
from maps.maps_reference_data import SPECIES
from maps.models import CaptureRecord
from maps.validators import CaptureRecordFormValidator


class CaptureRecordForm(forms.ModelForm):

    capture_year_day = forms.DateField(
        label="Date",
        widget=forms.DateInput(attrs={"type": "date"}),
        initial=timezone.now().date(),
    )

    capture_code = forms.ChoiceField(
        choices=CAPTURE_CODE_CHOICES,
        required=True,
    )

    species_number = forms.ChoiceField(
        label="Species",
        choices=SPECIES_CHOICES,
        required=True,
    )

    is_validated = forms.BooleanField(
        required=False,
        label="Validate this record?",
        initial=True,
        widget=forms.CheckboxInput(
            attrs={
                "class": "form-check-input",
            },
        ),
    )

    input_time = forms.TimeField(
        widget=forms.TimeInput(
            attrs={
                "class": "timepicker",
                "type": "time",
            },
        ),
        label="Time",
        required=True,
    )

    alpha_code = forms.CharField(widget=forms.HiddenInput(), required=False)
    discrepancies = forms.CharField(widget=forms.HiddenInput(), required=False)

    def __init__(self, *args, **kwargs):
        # Extract the instance from kwargs if it's there
        instance = kwargs.get("instance", None)

        super().__init__(*args, **kwargs)

        # Check if there's an instance to work with (i.e., we are editing an existing record)
        if instance:
            # Set the initial value for the input_time field based on the instance's capture_time
            self.fields["input_time"].initial = instance.capture_time.strftime("%H:%M")
            instance.discrepancies = ""

        self.fields["cloacal_protuberance"].label = "CP ℹ"
        self.fields["brood_patch"].label = "BP ℹ"
        self.fields["ff_wear"].label = "FF Wear ℹ"
        self.fields["fat"].label = "Fat ℹ"
        self.fields["juv_body_plumage"].label = "Juvenile Only"
        self.fields["body_plumage"].label = "Body Plum."
        self.fields["capture_year_day"].initial = timezone.now().date()
        self.fields["input_time"].initial = timezone.now().time().replace(second=0, microsecond=0)
        self.fields["capture_time"].initial = timezone.now()
        self.fields["alpha_code"].widget = forms.HiddenInput()
        self.fields["discrepancies"].widget = forms.HiddenInput()

        self.helper = FormHelper()
        self.helper.form_class = "my-3"
        self.helper.form_method = "post"
        self.helper.layout = Layout(
            Fieldset(
                "Location Date & Time",
                Row(
                    Column("net", css_class="col-3"),
                    Column("station", css_class="col-4"),
                    Column("bander_initials", css_class="col-5"),
                ),
                Row(
                    Column("capture_year_day", css_class="col-6"),
                    Column("input_time", css_class="col-6"),
                ),
                css_class="fieldset-container odd-set",
            ),
            Fieldset(
                "Species",
                Row(
                    Column("capture_code", css_class="col-8"),
                    Column("band_size", css_class="col-4"),
                ),
                Row(
                    Column("species_number", css_class="col-12"),
                ),
                Row(
                    Column("band_number", css_class="col-12"),
                ),
                css_class="fieldset-container even-set",
            ),
            Fieldset(
                "Sexing",
                Row(
                    Column("sex", css_class="col-6"),
                    Column("cloacal_direction", css_class="col-6"),
                ),
                Row(
                    Column("how_sexed_1", css_class="col-6"),
                    Column("how_sexed_2", css_class="col-6"),
                ),
                css_class="fieldset-container odd-set",
            ),
            Fieldset(
                "Morphometrics",
                Row(
                    Column("cloacal_protuberance", css_class="col-4"),
                    Column("brood_patch", css_class="col-4"),
                    Column("fat", css_class="col-4"),
                ),
                Row(
                    Column("body_molt", css_class="col-4"),
                    Column("ff_molt", css_class="col-4"),
                    Column("ff_wear", css_class="col-4"),
                ),
                Row(
                    Column("wing_chord", css_class="col-4"),
                    Column("skull", css_class="col-4"),
                    Column("juv_body_plumage", css_class="col-4"),
                ),
                css_class="fieldset-container even-set",
            ),
            Fieldset(
                "Molt Limits & Plumage",
                Row(
                    Column("primary_coverts", css_class="col-6"),
                    Column("secondary_coverts", css_class="col-6"),
                ),
                Row(
                    Column("primaries", css_class="col-3"),
                    Column("secondaries", css_class="col-3"),
                    Column("tertials", css_class="col-3"),
                    Column("rectrices", css_class="col-3"),
                ),
                Row(
                    Column("alula", css_class="col-4"),
                    Column("body_plumage", css_class="col-4"),
                    Column("non_feather", css_class="col-4"),
                ),
                css_class="fieldset-container odd-set",
            ),
            Fieldset(
                "Aging",
                Row(
                    Column("age_annual", css_class="col-6"),
                    Column("age_WRP", css_class="col-6"),
                ),
                Row(
                    Column("how_aged_1", css_class="col-6"),
                    Column("how_aged_2", css_class="col-6"),
                ),
                css_class="fieldset-container even-set",
            ),
            Fieldset(
                "Weight & Status",
                Row(
                    Column("body_mass", css_class="col-4"),
                    Column("status", css_class="col-4"),
                    Column("disposition", css_class="col-4"),
                ),
                css_class="fieldset-container odd-set",
            ),
            Fieldset(
                "",
                Row(
                    Column("note", css_class="col-12"),
                ),
                css_class="fieldset-container even-set",
            ),
            "is_validated",
            Submit("submit", "Submit", css_class="btn btn-lg btn-primary w-100"),
        )

    class Meta:
        model = CaptureRecord
        fields = "__all__"
        # The view will handle setting the user, scribe_initials, and hold_time fields
        exclude = [
            "user",
            "scribe_initials",
            "hold_time",
        ]

    # Users should not be filling in the alpha_code field, so we will fill it in for them
    def clean_alpha_code(self):
        species_number = int(self.cleaned_data.get("species_number"))
        alpha_code = SPECIES[species_number]["alpha_code"]
        self.cleaned_data["alpha_code"] = alpha_code
        return alpha_code

    # How aged and how sexed should always have the first option filled in if the second is filled in
    def _clean_how_aged_order(self):
        how_aged_1 = self.cleaned_data.get("how_aged_1")
        how_aged_2 = self.cleaned_data.get("how_aged_2")

        if not how_aged_1 and how_aged_2:
            self.cleaned_data["how_aged_1"] = how_aged_2
            self.cleaned_data["how_aged_2"] = None

    def _clean_how_sexed_order(self):
        how_sexed_1 = self.cleaned_data.get("how_sexed_1")
        how_sexed_2 = self.cleaned_data.get("how_sexed_2")

        if not how_sexed_1 and how_sexed_2:
            self.cleaned_data["how_sexed_1"] = how_sexed_2
            self.cleaned_data["how_sexed_2"] = None

    # Convert bander initials to all uppercase
    def clean_bander_initials(self):
        bander_initials = self.cleaned_data.get("bander_initials")
        if bander_initials:
            bander_initials = bander_initials.upper()
        return bander_initials

    def _clean_capture_time(self):
        year = int(self.cleaned_data.get("capture_year_day").year)
        month = int(self.cleaned_data.get("capture_year_day").month)
        day = int(self.cleaned_data.get("capture_year_day").day)
        hour = int(self.cleaned_data.get("input_time").strftime("%H"))
        minute = int(self.cleaned_data.get("input_time").strftime("%M"))

        # Combine the date and time to form the complete capture_time
        naive_datetime = datetime.datetime(
            year=year,
            month=month,
            day=day,
            hour=hour,
            minute=minute,
        )

        # Make the datetime object timezone-aware
        self.cleaned_data["capture_time"] = timezone.make_aware(naive_datetime)

    def clean(self):
        super().clean()

        self._clean_how_aged_order()
        self._clean_how_sexed_order()
        self._clean_capture_time()

        validator = CaptureRecordFormValidator(cleaned_data=self.cleaned_data)

        # Check if 'is_validated' is checked (True means validations are to be enforced)
        if self.cleaned_data.get("is_validated", True):
            validator.validate(raise_errors=True)
        else:
            validator.validate(raise_errors=False)
            discrepancy_string = "\n".join(validator.validation_errors).strip("\n")
            self.cleaned_data["discrepancies"] = discrepancy_string

        return self.cleaned_data
