from django.test import TestCase
from django.utils import timezone
from maps.forms import CaptureRecordForm


class CaptureRecordFormTest(TestCase):

    def test_valid_form_submission(self):
        form_data = {
            "input_time": timezone.now().strftime("%H:%M"),
            "capture_year_day": timezone.now().date(),
            "capture_code": "N",
            "species_number": 5810,
            "band_size": "1B",
            "band_number": 111156789,
            "age_annual": 2,
            "age_WRP": "FPF",
            "how_aged_1": "S",
            "how_aged_2": "J",
            "sex": "U",
            "skull": 3,
            "fat": 2,
            "body_molt": 2,
            "ff_molt": "N",
            "ff_wear": 2,
            "juv_body_plumage": 2,
            "primary_coverts": "J",
            "secondary_coverts": "L",
            "status": 300,
            "station": "MORS",
            "net": 15,
            "bander_initials": "BBB",
            "is_validated": True,
            # add other form fields as necessary
        }
        form = CaptureRecordForm(data=form_data)
        self.assertTrue(form.is_valid())
