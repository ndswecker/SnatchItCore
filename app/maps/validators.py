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
    
def validate_skull_provided_if_aged_by_skull(form_data: dict):
    if ("S" in [form_data.get("how_aged_1"), form_data.get("how_aged_2")]) and not form_data.get("skull"):
        raise ValidationError(
            {
                "skull": "A skull score must be provided if how aged is by skull."
            }
        )
    
def validate_skull_score_for_hy_or_local_birds(form_data: dict):
    skull = form_data.get("skull")
    age_annual = form_data.get("age_annual")
    if skull and skull < 5 and age_annual not in [2, 4]:
        raise ValidationError(
            {
                "skull": f"A skull score of {skull} is only valid for HY or Local birds."
            }
        )
    
def validate_skull_score_not_valid_for_hy_or_local(form_data: dict):
    skull = form_data.get("skull")
    age_annual = form_data.get("age_annual")
    if skull in [5, 6] and age_annual in [2, 4]:
        raise ValidationError(
            {
                "skull": f"A skull score of {skull} is not valid for HY or Local birds."
            }
        )



class CaptureRecordFormValidator(FormValidator):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.validators = [
            validate_juv_aging,
            validate_skull_provided_if_aged_by_skull,
            validate_skull_score_for_hy_or_local_birds,
            validate_skull_score_not_valid_for_hy_or_local,
        ]
