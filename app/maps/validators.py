from django.core.validators import ValidationError

from common.validators import FormValidator
from maps.maps_reference_data import SPECIES


def validate_juv_aging(form_data: dict):
    # Validate that if age is 4 or 2, then how_aged_1 must not be P
    if form_data.get("age_annual") in [4, 2] and form_data.get("how_aged_1") == "P":
        raise ValidationError(
            {
                "age_annual": f"How aged cannot be P for HY or Local birds. Please choose J.",
            },
        )

def validate_skull_to_age(form_data: dict):
    if (form_data.get("how_aged_1") == "S" or form_data.get("how_aged_2") == "S") and not form_data.get("skull"):
        raise ValidationError(
            {
                "age_annual": f"A skull score must be provided if how aged is by skull.",
            },
        )
    
    if form_data.get("skull") and (form_data.get("skull") < 5 and form_data.get("age_annual") not in [2, 4]):
        raise ValidationError(
            {
                "age_annual": f"A skull score of {form_data.get('skull')} is only valid for HY or Local birds.",
            },
        )
    
    if form_data.get("skull") in [5, 6] and form_data.get("age_annual") in [2, 4]:
        raise ValidationError(
            {
                "age_annual": f"A skull score of {form_data.get('skull')} is not valid for HY or Local birds.",
            },
        )


class CaptureRecordFormValidator(FormValidator):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.validators = [
            validate_juv_aging,
            validate_skull_to_age,
        ]
