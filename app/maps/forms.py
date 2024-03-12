from django import forms
from django.core.exceptions import ValidationError
from django_select2 import forms as s2forms

from maps.maps_reference_data import SPECIES, WRP_GROUPS
from maps.choice_definitions import SPECIES_CHOICES
from maps.models import CaptureRecord


class CaptureRecordForm(forms.ModelForm):
    species_number = forms.ChoiceField(
        choices=SPECIES_CHOICES,
        widget=s2forms.Select2Widget(attrs={"class": "form-control"}),
    )
    # validation_override = forms.BooleanField(required=False, label='Override validation errors')
    is_validated = forms.BooleanField(
        required=False,  # Make the field not required
        label="Override Validation",  # Label for the field
        initial=False,  # Set the default value to False
        widget=forms.CheckboxInput(attrs={"class": "form-check-input"})  # Define the widget and its class
    )

    class Meta:
        model = CaptureRecord
        fields = "__all__"
        exclude = ["user", "bander_initials", "alpha_code", "discrepancies"]

    def clean(self):
        cleaned_data = super().clean()
        validation_override = cleaned_data.get("is_validated", False)
        discrepancies = []

        # Custom function to log discrepancies or raise validation errors
        def log_discrepancy(message):
            if validation_override:
                # Append the message directly if it's a validation override scenario
                discrepancies.append(message)
            else:
                # Otherwise, immediately raise a ValidationError
                raise ValidationError(message)

        try:
            # Validate skull to age, logging discrepancies or raising errors as needed
            self.validate_skull_to_age(cleaned_data, log_discrepancy)
        except ValidationError as e:
            if not validation_override:
                raise e

        if validation_override and discrepancies:
            # Join discrepancies into a single string, each on a new line
            discrepancy_text = "\n".join(discrepancies)
            # Append new discrepancies to any existing text in the instance's discrepancies field
            if self.instance.discrepancies:
                self.instance.discrepancies += "\n" + discrepancy_text
            else:
                self.instance.discrepancies = discrepancy_text

        return cleaned_data

        # if not validation_override:
            # self.fill_in_alpha_code(cleaned_data)

            # self.validate_how_aged_order(cleaned_data)
            # self.validate_juv_aging(cleaned_data)
            # self.validate_MLP_to_age(cleaned_data)
            # self.validate_skull_to_age(cleaned_data)

            # self.validate_status_disposition(cleaned_data)
            # self.validate_species_to_wing(cleaned_data)
            # self.validate_wrp_to_species(cleaned_data)

            # self.validate_how_sexed_order(cleaned_data)
            # self.validate_sex_how_sexed(cleaned_data)

            # self.validate_cloacal_protuberance(cleaned_data)
            # self.validate_cloacal_protuberance_sexing(cleaned_data)

            # self.validate_brood_patch(cleaned_data)
            # self.validate_brood_patch_sexing(cleaned_data)

            # self.validate_band_size_to_species(cleaned_data)
        # else:
            # run each validation and add the error to discrepancies
            # print("No validation")

        # try:
        #     self.fill_in_alpha_code(cleaned_data)

        #     self.validate_how_aged_order(cleaned_data)
        #     self.validate_juv_aging(cleaned_data)
        #     self.validate_MLP_to_age(cleaned_data)
        #     self.validate_skull_to_age(cleaned_data)

        #     self.validate_status_disposition(cleaned_data)
        #     self.validate_species_to_wing(cleaned_data)
        #     self.validate_wrp_to_species(cleaned_data)

        #     self.validate_how_sexed_order(cleaned_data)
        #     self.validate_sex_how_sexed(cleaned_data)

        #     self.validate_cloacal_protuberance(cleaned_data)
        #     self.validate_cloacal_protuberance_sexing(cleaned_data)

        #     self.validate_brood_patch(cleaned_data)
        #     self.validate_brood_patch_sexing(cleaned_data)

        #     self.validate_band_size_to_species(cleaned_data)

        # except ValidationError as e:
        #     # Raise errors to user if validation override is not engaged
        #     if not validation_override:
        #         errors.append(e)
        #         # Add the indented block of code here

        # if validation_override and errors:
        #     # Log the errors in discrepancies and flag for review
        #     discrepancies = "\n".join([str(e) for e in errors])
        #     # self.instance.is_flagged_for_review = True
        #     self.instance.discrepancies += f"Overridden validations: {discrepancies}\n"
        # elif errors:
        #     # If not overriding, raise the first validation error as usual
        #     raise errors[0]

    def save(self, commit=True):
        # If commit is False, the caller is responsible for saving the object.
        # This method returns a model instance whether or not commit==True.
        instance = super().save(commit=False)
        if not instance.is_validated:
            instance.is_validated = True
        else:
            instance.is_validated = False
        if commit:
            instance.save()
        return instance

    def fill_in_alpha_code(self, cleaned_data):
        # Accessing the species_number from cleaned_data
        species_number = cleaned_data.get('species_number')
        if species_number:
            # Assuming SPECIES is a dictionary where keys are species numbers
            alpha_code = SPECIES.get(species_number, {}).get('alpha_code', '')
            # Setting the alpha_code in cleaned_data
            self.cleaned_data['alpha_code'] = alpha_code


    def validate_species_to_wing(self, cleaned_data):
        wing_chord = cleaned_data.get('wing_chord')
        species_number = cleaned_data.get('species_number')

        if wing_chord is not None and species_number is not None:
            species_info = SPECIES.get(species_number)
            if species_info:
                wing_chord_range = species_info.get("wing_chord_range")
                if not (wing_chord_range[0] <= wing_chord <= wing_chord_range[1]):
                    self.add_error('wing_chord', ValidationError(
                        f"Wing chord for {species_info['common_name']} must be between {wing_chord_range[0]} and {wing_chord_range[1]}.",
                        code='invalid'
                    ))

        
    def validate_wrp_to_species(self, cleaned_data):
        """
        Validates the age_WRP input against allowed codes for the given species_number.
        Checks if the provided age_WRP code is within the list of allowed codes for the species.
        Allowed codes are based on the WRP_groups the species belongs to, as defined in REFERENCE_GUIDE.
        Raises ValidationError if the age_WRP code is not allowed, indicating an invalid code or a mismatch.
        """

        species_number = cleaned_data.get("species_number")
        age_WRP = cleaned_data.get("age_WRP")

        if species_number and age_WRP:
            target_species = SPECIES.get(species_number)
            if target_species:
                wrp_groups = target_species["WRP_groups"]

                allowed_codes = []
                for group_number in wrp_groups:
                    allowed_codes.extend(WRP_GROUPS[group_number]["codes_allowed"])

                if age_WRP not in allowed_codes:
                    raise ValidationError(
                        {
                            "age_WRP": f"The age_WRP '{age_WRP}' is not allowed for the species '{target_species['common_name']}' with WRP_groups {wrp_groups}.",
                        },
                    )


    def validate_how_aged_order(self, cleaned_data):
        how_aged_1 = cleaned_data.get("how_aged_1")
        how_aged_2 = cleaned_data.get("how_aged_2")

        if not how_aged_1 and how_aged_2:
            cleaned_data["how_aged_1"] = how_aged_2
            cleaned_data["how_aged_2"] = None

    def validate_how_sexed_order(self, cleaned_data):
        how_sexed_1 = cleaned_data.get("how_sexed_1")
        how_sexed_2 = cleaned_data.get("how_sexed_2")

        if not how_sexed_1 and how_sexed_2:
            how_sexed_1 = how_sexed_2
            how_sexed_2 = None

    def validate_sex_how_sexed(self, cleaned_data):
        sex = cleaned_data.get("sex")
        how_sexed_1 = cleaned_data.get("how_sexed_1")
        how_sexed_2 = cleaned_data.get("how_sexed_2")

        if sex in ["U", "X"]:
            return

        male_criteria = ["C", "W", "E", "O", "P"]
        female_criteria = ["B", "P", "E", "W", "O"]

        # Checking if criteria are met
        if sex == "M" and not any(
            how_sexed in male_criteria for how_sexed in [how_sexed_1, how_sexed_2]
        ):
            raise ValidationError("A bird sexed male must have how_sexed_1 or how_sexed_2 as 'C', 'W', 'E', or 'O'.")

        if sex == "F" and not any(
            how_sexed in female_criteria for how_sexed in [how_sexed_1, how_sexed_2]
        ):
            raise ValidationError(
                "A bird sexed female must have how_sexed_1 or how_sexed_2 as 'B', 'P', 'E', 'W', or 'O'.",
            )

    def validate_cloacal_protuberance(self, cleaned_data):
        how_sexed_1 = cleaned_data.get("how_sexed_1")
        how_sexed_2 = cleaned_data.get("how_sexed_2")
        cloacal_protuberance = cleaned_data.get("cloacal_protuberance")
        sex = cleaned_data.get("sex")

        if "C" in [how_sexed_1, how_sexed_2] and cloacal_protuberance in [None, 0]:
            raise ValidationError(
                {
                    "cloacal_protuberance": 
                    "Cloacal protuberance must be filled in for birds sexed by cloacal protuberance.",
                },
            )

        if sex == "F" and cloacal_protuberance not in [None, 0]:
            raise ValidationError(
                {
                    "cloacal_protuberance": "Cloacal protuberance must be None or 0 for female birds.",
                },
            )

    def validate_brood_patch(self, cleaned_data):
        how_sexed_1 = cleaned_data.get("how_sexed_1")
        how_sexed_2 = cleaned_data.get("how_sexed_2")
        brood_patch = cleaned_data.get("brood_patch")

        if "B" in [how_sexed_1, how_sexed_2] and (brood_patch is None or brood_patch <= 0):
            raise ValidationError(
                {
                    "brood_patch": "Brood patch must be greater than 0 for birds sexed by brood patch.",
                },
            )

    def validate_cloacal_protuberance_sexing(self, cleaned_data):
        how_sexed_1 = cleaned_data.get("how_sexed_1")
        how_sexed_2 = cleaned_data.get("how_sexed_2")

        if ("C" in [how_sexed_1, how_sexed_2]) and not (
            SPECIES[self.species_number]["sexing_criteria"]["male_by_CP"]
        ):
            raise ValidationError(
                {
                    "cloacal_protuberance": "This species cannot be reliably sexed by CP",
                },
            )

    def validate_brood_patch_sexing(self, cleaned_data):
        how_sexed_1 = cleaned_data.get("how_sexed_1")
        how_sexed_2 = cleaned_data.get("how_sexed_2")
        species_number = cleaned_data.get("species_number")
        brood_patch = cleaned_data.get("brood_patch")

        # If bird was sexed by brood patch...
        if "B" in [how_sexed_1, how_sexed_2]:
            sexing_criteria = SPECIES[species_number]["sexing_criteria"]

            # If the species does not exclusively use brood patch for sexing females...
            if not sexing_criteria["female_by_BP"]:
                # If males of the species may also develop brood patches...
                if brood_patch is None or brood_patch < 3:
                    # ...then a higher value is expected for brood patch development.
                    raise ValidationError(
                        {
                            "brood_patch": 
                            "Males of this species may also develop brood patches. A value of 3 or greater is required.",
                        },
                    )
                else:
                    # If the bird is not sexed by brood patch but has a brood patch value...
                    raise ValidationError(
                        {
                            "brood_patch": "Brood patch is not a reliable sexing method for this species.",
                        },
                    )

    def validate_band_size_to_species(self, cleaned_data):
        species_number = cleaned_data.get("species_number")
        band_size = cleaned_data.get("band_size")

        if species_number is not None:
            species_number = int(species_number)  # Convert species_number to integer
            target_species = SPECIES.get(species_number)  # Use .get() to safely access the dictionary
        
            if target_species:
                band_sizes = target_species.get("band_sizes", [])
                if band_size not in band_sizes:
                    error_msg = (
                        f"The band_size '{band_size}' is not allowed for the species "
                        f"'{target_species.get('common_name', 'Unknown')}' with band_sizes {band_sizes}."
                    )
                    raise ValidationError({"band_size": error_msg})
            else:
                # Handle the case where the species_number does not exist in SPECIES
                raise ValidationError({"species_number": f"Species number {species_number} not found in SPECIES dictionary."})


    def validate_status_disposition(self, cleaned_data):
        status = cleaned_data.get("status")
        disposition = cleaned_data.get("disposition")
        if status == 000 and disposition not in ["D", "P"]:
            raise ValidationError(
                {
                    "disposition": "Disposition must be D or P if status is 000.",
                },
            )

        if disposition in ["B", "L", "S", "T", "W"] and status == 300:
            raise ValidationError(
                {
                    "status": "Status cannot be 300 if disposition is B, L, S, T, or W. Chose 500",
                },
            )

    def validate_juv_aging(self, cleaned_data):
        age_annual = cleaned_data.get("age_annual")
        how_aged_1 = cleaned_data.get("how_aged_1")

        # validate that if age is 4 or 2, then how_aged_1 must not be P
        if age_annual in [4, 2] and how_aged_1 == "P":
            raise ValidationError(
                {
                    "how_aged_1": "How aged cannot be P for HY or Local birds. Please choose J.",
                },
            )

    def validate_MLP_to_age(self, cleaned_data):
        age_annual = cleaned_data.get("age_annual")
        how_aged_1 = cleaned_data.get("how_aged_1")
        how_aged_2 = cleaned_data.get("how_aged_2")

        # validate that if age is not 1, then how_aged_1 must be filled in
        if age_annual != 1 and not how_aged_1:
            raise ValidationError(
                {
                    "how_aged_1": "How aged must be filled in for birds not of age 1.",
                },
            )

        # validate that if age is 5, and how_aged_1 is L, then how_aged_2 must be filled in
        if age_annual == 5 and how_aged_1 == "L" and not how_aged_2:
            raise ValidationError(
                {
                    "how_aged_2": "How aged must further separate HY from SY birds. Please fill in how_aged_2.",
                },
            )

        # validate that if either how_aged_1 or how_aged_2 is L or P, then one of the following fields must be filled in
        # primary_coverts, secondary_coverts, primaries, rectrices, secondaries, tertials, body_plumage, non_feather
        if how_aged_1 in ["L", "P"] or how_aged_2 in ["L", "P"]:
            if not any(
                [
                    self.primary_coverts,
                    self.secondary_coverts,
                    self.primaries,
                    self.rectrices,
                    self.secondaries,
                    self.tertials,
                    self.body_plumage,
                    self.non_feather,
                ],
            ):
                raise ValidationError(
                    {
                        "age_annual": "At least one of the Molt Limits and Plumage fields must be filled in ",
                    },
                )

    def validate_skull_to_age(self, cleaned_data, log_discrepancy):
        how_aged_1 = cleaned_data.get("how_aged_1")
        how_aged_2 = cleaned_data.get("how_aged_2")
        skull = cleaned_data.get("skull")
        age_annual = cleaned_data.get("age_annual")
        
        # Check each condition and log a string message
        if (how_aged_1 == "S" or how_aged_2 == "S") and not skull:
            log_discrepancy("Skull must be filled in for birds aged by skull.")

        if skull and (skull < 5 and age_annual not in [2, 4]):
            log_discrepancy("Age must be HY or L for birds with skull score less than 5.")

        if skull in [5, 6] and age_annual in [2, 4]:
            log_discrepancy("Age must be SY or ASY for birds with skull score of 5 or 6.")
