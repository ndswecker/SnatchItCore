from django.core.exceptions import ValidationError
from django.test import TestCase

from maps.validators import validate_band_number_to_size
from maps.validators import validate_juv_aging_plumage_not_p
from maps.validators import validate_wrp_allowed_for_species
from maps.validators import validate_age_annual_to_allowed_wrp
from maps.maps_reference_data import WRP_GROUPS
from maps.maps_reference_data import SPECIES
from maps.maps_reference_data import AGES_ANNUAL
from maps.maps_reference_data import AGES_WRP


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


class TestValidateBandNumberToSize(TestCase):

    def test_band_number_size_match_passes(self):
        # Test data mapping band numbers to expected band sizes
        test_data = {
            963050741: "0A",
            963150741: "1",
            963151741: "1A",
            963151841: "1B",
            963151941: "1D",
            963250741: "2",
            963350741: "3",
            963351741: "3A",
            963351841: "3B",
            963450741: "4",
            963052741: "R",  # Recap
            963052841: "U",  # Unbanded
        }

        for band_number, band_size in test_data.items():
            with self.subTest(band_number=band_number, band_size=band_size):
                input_data = {"band_number": band_number, "band_size": band_size}
                try:
                    validate_band_number_to_size(input_data)
                except ValidationError:
                    self.fail(f"Validation should have failed band number {band_number} and band size {band_size}")

    def test_band_number_size_mismatch_fails(self):
        # Test data where band numbers do not match the expected band sizes
        test_data = {
            963050741: "1",
            963150741: "0A",
            963151741: "2",
            963151841: "3A",
            963151941: "3B",
            963250741: "4",
            963950741: "1A",
            963351741: "1B",
            963351841: "1D",
            963450741: "2",
        }

        for band_number, band_size in test_data.items():
            with self.subTest(band_number=band_number, band_size=band_size):
                input_data = {"band_number": band_number, "band_size": band_size}
                with self.assertRaises(
                    ValidationError, msg=f"Validation should have passed {band_number} and band size {band_size}"
                ):
                    validate_band_number_to_size(input_data)

    def test_skipped_validation_with_special_band_size(self):
        input_data = {"band_number": 963852741, "band_size": "R"}
        try:
            validate_band_number_to_size(input_data)
        except ValidationError:
            self.fail("Validation should be skipped for special band sizes like 'R' or 'U'.")


class TestValidateWrpAllowedForSpecies(TestCase):

    def test_wrp_code_allowed(self):
        for species_number, data in SPECIES.items():
            wrp_groups = data["WRP_groups"]
            allowed_codes = set()
            for group in wrp_groups:
                allowed_codes.update(WRP_GROUPS[group]["codes_allowed"])

            for code in allowed_codes:
                form_data = {"species_number": species_number, "age_WRP": code}
                try:
                    validate_wrp_allowed_for_species(form_data)
                except ValidationError:
                    self.fail(
                        f"Validation failed for {form_data}. {code} should be allowed for species {species_number}."
                    )


class TestValidateAgeAnnualToAgeWRP(TestCase):
    def test_valid_age_annual_wrp_combinations(self):
        # Test valid combinations of age_annual and age_wrp
        for age_annual, data in AGES_ANNUAL.items():
            for age_wrp in data["allowed_wrp_codes"]:
                with self.subTest(age_annual=age_annual, age_wrp=age_wrp):
                    form_data = {"age_annual": age_annual, "age_WRP": age_wrp}
                    # Should not raise ValidationError
                    validate_age_annual_to_allowed_wrp(form_data)

    def test_invalid_age_annual_wrp_combinations(self):
        # Assuming "UCU" is a WRP code that is not valid for any of the ages except "0" and "9"
        invalid_wrp_code = "UCU"
        for age_annual in AGES_ANNUAL:
            if invalid_wrp_code not in AGES_ANNUAL[age_annual]["allowed_wrp_codes"]:
                with self.subTest(age_annual=age_annual, age_wrp=invalid_wrp_code):
                    form_data = {"age_annual": age_annual, "age_WRP": invalid_wrp_code}
                    # Should raise ValidationError
                    with self.assertRaises(ValidationError):
                        validate_age_annual_to_allowed_wrp(form_data)

    def test_age_4(self):
        age_annual = "4"
        valid_wrp_code = "FPJ"

        for wrp_code in AGES_WRP.keys():
            form_data = {"age_annual": age_annual, "age_WRP": wrp_code}
            if wrp_code == valid_wrp_code:
                try:
                    validate_age_annual_to_allowed_wrp(form_data)
                except ValidationError:
                    self.fail(f"Validation incorrectly failed for WRP code {wrp_code} with age annual {age_annual}")
            else:
                with self.assertRaises(ValidationError):
                    validate_age_annual_to_allowed_wrp(form_data)

    def test_age_2(self):
        age_annual = "2"
        valid_wrp_codes = AGES_ANNUAL[age_annual]["allowed_wrp_codes"]

        for wrp_code in AGES_WRP.keys():
            form_data = {"age_annual": age_annual, "age_WRP": wrp_code}
            if wrp_code in valid_wrp_codes:
                try:
                    validate_age_annual_to_allowed_wrp(form_data)
                except ValidationError:
                    self.fail(f"Validation incorrectly failed for WRP code {wrp_code} with age annual {age_annual}")
            else:
                with self.assertRaises(ValidationError):
                    validate_age_annual_to_allowed_wrp(form_data)
