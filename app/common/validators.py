from django.core.exceptions import ValidationError


class FormValidator:
    def __init__(self, cleaned_data: dict):
        self.cleaned_data = cleaned_data
        self.discrepancy_string = ""
        self.validation_errors = []
        self.validators = []

    def validate(self, override_validation: bool):
        if override_validation:
            return self._catch_validation_errors()
        else:
            return self._raise_validation_errors()

    def _raise_validation_errors(self):
        for validator in self.validators:
            validator(self.cleaned_data)

    def _catch_validation_errors(self):
        for validator in self.validators:
            try:
                validator(self.cleaned_data)
            except ValidationError as e:
                self.validation_errors.append(e.messages[0])
        self.discrepancy_string = "\n".join(err_str for err_str in self.validation_errors).strip("\n")
