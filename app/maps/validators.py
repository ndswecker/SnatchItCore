from django.core.validators import ValidationError

from common.validators import FormValidator


def validate_juv_aging(form_data: dict):
    # Validate that if age is 4 or 2, then how_aged_1 must not be P
    if form_data.get("age_annual") in [4, 2] and form_data.get("how_aged_1") == "P":
        raise ValidationError(
            {
                "age_annual": f"How aged cannot be P for HY or Local birds. Please choose J.",
            },
        )


class CaptureRecordFormValidator(FormValidator):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.validators = [
            validate_juv_aging,
        ]
