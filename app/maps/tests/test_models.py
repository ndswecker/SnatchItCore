import datetime
from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.contrib.auth import get_user_model

from maps.models import CaptureRecord


class TestModels(TestCase):

    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(
            username="user",
            password="pass",
            initials="ABC",
        )
        self.client = Client()

        self.capture_record = CaptureRecord.objects.create(
            user=self.user,
            capture_code="N",
            species_number=5810,
            age_annual=1,
            age_WRP="MFCF",
            status=300,
            capture_time=datetime.datetime.now(),
            station="MORS",
            band_size="1B",
            location="MORS",
        )

    def test_capture_record(self):
        self.assertEquals(self.capture_record.species_number, 5810)
