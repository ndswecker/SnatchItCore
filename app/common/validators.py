from django.core.exceptions import ValidationError

class FormValidator:
    def __init__(self, cleaned_data: dict):
        self.cleaned_data = cleaned_data
        self.validation_errors: list[str] = [] 
        self.validators = [] 

    def validate(self, raise_errors: bool):
        if raise_errors:
            self._raise_validation_errors()
        else:
            self._catch_validation_errors()

    def _raise_validation_errors(self):
        for validator in self.validators:
            validator(self.cleaned_data)

    def _catch_validation_errors(self):
        for validator in self.validators:
            try:
                validator(self.cleaned_data)
            except ValidationError as e:
                self.validation_errors.append(e.messages[0])
            
