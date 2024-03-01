from django.core.exceptions import ValidationError

from maps.birds_info import REFERENCE_GUIDE
from maps.models import CaptureRecord


class MapsValidator:
    def __init__(self, capture_record: CaptureRecord):
        self.capture_record = capture_record

    def validate_species_to_wing(self):
        species_info = REFERENCE_GUIDE["species"].get(self.capture_record.species_number)
        if species_info and self.capture_record.wing_chord is not None:
            wing_chord_range = species_info.get("wing_chord_range", (0, 0))
            if not (wing_chord_range[0] <= self.capture_record.wing_chord <= wing_chord_range[1]):
                raise ValidationError(
                    {
                        "wing_chord": f"Wing chord for {species_info['common_name']} must be between {wing_chord_range[0]} and {wing_chord_range[1]}.",  # noqa: E501
                    },
                )

    def validate_initials(self, field_value, field_name, mandatory=True):
        """
        Validates that a field value is exactly 3 letters long and all characters are alphabetic for mandatory fields.
        For optional fields, it validates the condition only if a value is provided.
        Automatically converts to uppercase.
        :param field_value: The value of the field to validate.
        :param field_name: The name of the field (for error messages).
        :param mandatory: Boolean indicating if the field is mandatory.
        :raises: ValidationError if the field does not meet the criteria and is mandatory.
        """

        if mandatory:
            if not field_value or len(field_value) != 3 or not field_value.isalpha():
                raise ValidationError(
                    {
                        field_name: f'{field_name.replace("_", " ").capitalize()} must be exactly three letters long.',
                    },
                )
        else:
            if field_value and (len(field_value) != 3 or not field_value.isalpha()):
                raise ValidationError(
                    {
                        field_name: f'{field_name.replace("_", " ").capitalize()} must be exactly three letters long.',
                    },
                )

        if field_value:
            setattr(self, field_name, field_value.upper())

    def validate_wrp_to_species(self):
        """
        Validates the age_WRP input against allowed codes for the given species_number.
        This method checks if the provided age_WRP code is within the list of allowed codes for the species identified by species_number.
        The allowed codes are determined based on the WRP_groups the species belongs to, as defined in REFERENCE_GUIDE.
        Raises:
            ValidationError: If the age_WRP code is not allowed for the species,
            indicating either an invalid code or a mismatch between the species and its typical age classification codes.
        """

        target_species = REFERENCE_GUIDE["species"][self.capture_record.species_number]
        wrp_groups = target_species["WRP_groups"]

        allowed_codes = []
        for group_number in wrp_groups:
            allowed_codes.extend(REFERENCE_GUIDE["wrp_groups"][group_number]["codes_allowed"])

        if self.capture_record.age_WRP not in allowed_codes:
            raise ValidationError({
                "age_WRP": f"The age_WRP '{self.capture_record.age_WRP}' is not allowed for the species '{target_species['common_name']}' with WRP_groups {wrp_groups}."
            })

    def validate_how_sexed_order(self):
        """
        Automatically adjust how_sexed_1 and how_sexed_2 fields to ensure logical data consistency.
        """

        if not self.capture_record.how_sexed_1 and self.capture_record.how_sexed_2:
            self.capture_record.how_sexed_1 = self.capture_record.how_sexed_2
            self.capture_record.how_sexed_2 = None

    def validate_sex_how_sexed(self):
        """
        Validate that how_sexed_1 and how_sexed_2 are provided with legitimate options
        for the sex of the bird. Raises a ValidationError if the criteria are not met.
        """

        if self.capture_record.sex == "M":
            allowed_methods = {"C", "P", "W", "E", "O"}
        elif self.capture_record.sex == "F":
            allowed_methods = {"B", "P", "E", "W", "O"}
        else:
            return
        if not self.capture_record.how_sexed_1:
            raise ValidationError({
                "how_sexed_1": "A method of determination is required for birds with specified sex."
            })

        invalid_methods = []
        if self.capture_record.how_sexed_1 and self.capture_record.how_sexed_1 not in allowed_methods:
            invalid_methods.append("how_sexed_1")
        if self.capture_record.how_sexed_2 and self.capture_record.how_sexed_2 not in allowed_methods:
            invalid_methods.append("how_sexed_2")
        if invalid_methods:
            raise ValidationError({method: "Invalid method selected for the bird's sex." for method in invalid_methods})

    def validate_band_size_to_species(self):
        """
        Validates the band_size input against allowed sizes for the given species_number.
        This method checks if the provided band_size is within the list of allowed sizes for the species identified by species_number.
        The allowed sizes are determined based on the band_sizes the species belongs to, as defined in REFERENCE_GUIDE.
        Raises:
            ValidationError: If the band_size is not allowed for the species,
            indicating either an invalid size or a mismatch between the species and its typical band sizes.
        """

        target_species = REFERENCE_GUIDE["species"][self.capture_record.species_number]
        band_sizes = target_species["band_sizes"]
        if self.capture_record.band_size not in band_sizes:
            raise ValidationError({
                "band_size": f"The band_size '{self.capture_record.band_size}' is not allowed for the species '{target_species['common_name']}' with band_sizes {band_sizes}."
            })
