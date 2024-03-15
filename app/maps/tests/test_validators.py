from django.core.exceptions import ValidationError
from django.test import TestCase

from maps.validators import validate_juv_aging_plumage_not_p


class TestValidateJuvAging(TestCase):
    # python app\manage.py test maps.tests.test_validators.TestValidateJuvAging
    def test_passes(self):
        input_data = {
            "age_annual": 1,
            "how_aged_1": "P",
        }
        try:
            validate_juv_aging_plumage_not_p(input_data)
        except ValidationError:
            self.fail("validate_juv_aging incorrectly failed a passing case")

    def test_raises_validation_error(self):
        input_data = {
            "age_annual": 2,
            "how_aged_1": "P",
        }
        self.assertRaises(ValidationError, validate_juv_aging_plumage_not_p, input_data)

        input_data = {
            "age_annual": 4,
            "how_aged_1": "P",
        }
        self.assertRaises(ValidationError, validate_juv_aging_plumage_not_p, input_data)
