from django.core.exceptions import ValidationError


class FormValidator:
    def __init__(self, cleaned_data: dict):
        self.cleaned_data = cleaned_data
        self.discrepancy_string = ""
        self.validation_errors = []
        self.validators = []

    def validate(self, override_validation: bool):
        for validator in self.validators:
            if override_validation:
                try:
                    validator(self.cleaned_data)
                except ValidationError as e:
                    self.validation_errors.append(e.messages[0])
            else:
                validator(self.cleaned_data)
        if override_validation:
            self.discrepancy_string = "\n".join(err_str for err_str in self.validation_errors).strip("\n")

