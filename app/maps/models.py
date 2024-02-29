import datetime

from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator
from django.db import models

from common.models import BaseModel
from maps.banding_data_fields import *
from maps.birds_info import REFERENCE_GUIDE


def rounded_down_datetime():
    now = datetime.datetime.now()
    rounding_down = (now.minute // 10) * 10
    rounded_minute = now.replace(minute=rounding_down, second=0, microsecond=0)
    return rounded_minute


class CaptureRecord(BaseModel):
    bander_initials = models.CharField(
        max_length=3,
        default="JSM",
    )

    capture_code = models.CharField(
        max_length=1,
        choices=CAPTURE_CODE_OPTIONS,
        default="N",
    )

    band_number = models.IntegerField(
        validators=[
            MinValueValidator(100000000, message="Band number must be at least 9 digits long."),
            MaxValueValidator(999999999, message="Band number must be less than 10 digits."),
        ],
        default=123456789,
    )

    species_number = models.IntegerField(
        validators=[
            MinValueValidator(1000, message="Species number must be at least 4 digits long."),
            MaxValueValidator(9999, message="Species number must be less than 5 digits."),
        ],
        choices=SPECIES_OPTIONS,
        default=5810,
    )

    alpha_code = models.CharField(max_length=4)

    age_annual = models.CharField(
        max_length=1,
        choices=AGE_ANNUAL_OPTIONS,
        default="1",
    )

    how_aged_1 = models.CharField(
        max_length=1,
        null=True,
        blank=True,
        choices=HOW_AGED_SEXED_OPTIONS,
    )

    how_aged_2 = models.CharField(
        max_length=1,
        null=True,
        blank=True,
        choices=HOW_AGED_SEXED_OPTIONS,
    )

    age_WRP = models.CharField(
        max_length=4,
        choices=AGE_WRP_OPTIONS,
        default="MFCF",
    )

    sex = models.CharField(
        max_length=1,
        choices=SEX_OPTIONS,
        default="U",
    )
    how_sexed_1 = models.CharField(
        max_length=1,
        null=True,
        blank=True,
        choices=HOW_AGED_SEXED_OPTIONS,
    )
    how_sexed_2 = models.CharField(
        max_length=1,
        null=True,
        blank=True,
        choices=HOW_AGED_SEXED_OPTIONS,
    )

    skull = models.IntegerField(
        choices=SKULL_SCORES,
        null=True,
        blank=True,
    )

    cloacal_protuberance = models.IntegerField(
        choices=CLOACAL_PROTUBERANCE_SCORES,
        null=True,
        blank=True,
    )

    brood_patch = models.IntegerField(
        choices=BROOD_PATCH_SCORES,
        null=True,
        blank=True,
    )

    fat = models.IntegerField(
        choices=FAT_SCORES,
        null=True,
        blank=True,
    )

    body_molt = models.IntegerField(
        choices=BODY_MOLT_OPTIONS,
        null=True,
        blank=True,
    )

    ff_molt = models.CharField(
        max_length=1,
        choices=FLIGHT_FEATHER_MOLT_OPTIONS,
        null=True,
        blank=True,
    )

    ff_wear = models.IntegerField(
        choices=FLIGHT_FEATHER_WEAR_SCORES,
        null=True,
        blank=True,
    )

    juv_body_plumage = models.IntegerField(
        choices=JUVENILE_BODY_PLUMAGE_OPTIONS,
        null=True,
        blank=True,
    )

    primary_coverts = models.CharField(
        choices=MOLT_LIMIT_PLUMAGE_OPTIONS,
        max_length=1,
        null=True,
        blank=True,
    )

    secondary_coverts = models.CharField(
        choices=MOLT_LIMIT_PLUMAGE_OPTIONS,
        max_length=1,
        null=True,
        blank=True,
    )

    primaries = models.CharField(
        max_length=1,
        choices=MOLT_LIMIT_PLUMAGE_OPTIONS,
        null=True,
        blank=True,
    )

    rectrices = models.CharField(
        max_length=1,
        choices=MOLT_LIMIT_PLUMAGE_OPTIONS,
        null=True,
        blank=True,
    )

    secondaries = models.CharField(
        max_length=1,
        choices=MOLT_LIMIT_PLUMAGE_OPTIONS,
        null=True,
        blank=True,
    )

    tertials = models.CharField(
        max_length=1,
        choices=MOLT_LIMIT_PLUMAGE_OPTIONS,
        null=True,
        blank=True,
    )

    body_plumage = models.CharField(
        max_length=1,
        choices=MOLT_LIMIT_PLUMAGE_OPTIONS,
        null=True,
        blank=True,
    )

    non_feather = models.CharField(
        max_length=1,
        choices=MOLT_LIMIT_PLUMAGE_OPTIONS,
        null=True,
        blank=True,
    )

    wing_chord = models.IntegerField(
        validators=[
            MinValueValidator(10, message="Wing chord must be at least 0."),
            MaxValueValidator(300, message="Wing chord must be less than 300."),
        ],
        null=True,
        blank=True,
    )

    body_mass = models.DecimalField(
        max_digits=4,
        decimal_places=1,
        validators=[
            MinValueValidator(0, message="Mass must be at least 0."),
            MaxValueValidator(999.9, message="Mass must be less than 10000."),
        ],
        null=True,
        blank=True,
    )

    status = models.IntegerField(
        validators=[
            MinValueValidator(0, message="Status must be at least 000."),
            MaxValueValidator(999, message="Status must be less than 1000."),
        ],
        default=300,
    )

    date_time = models.DateTimeField(
        default=rounded_down_datetime,
    )

    station = models.CharField(
        max_length=4,
        choices=STATION_OPTIONS,
        default="MORS",
    )

    net = models.CharField(
        max_length=4,
        default="15",
    )

    disposition = models.CharField(
        max_length=1,
        choices=DISPOSITION_OPTIONS,
        null=True,
        blank=True,
    )

    note_number = models.CharField(
        max_length=2,
        null=True,
        blank=True,
    )

    note = models.TextField(
        null=True,
        blank=True,
    )

    band_size = models.CharField(
        max_length=2,
        choices=BAND_SIZE_OPTIONS,
        default="1B",
    )

    scribe = models.CharField(
        max_length=3,
        null=True,
        blank=True,
    )

    location = models.CharField(
        max_length=4,
        null=True,
        blank=True,
    )

    # Fields not to be submitted by the user
    discrepancies = models.TextField(null=True, blank=True)
    is_flagged_for_review = models.BooleanField(default=False)

    def __str__(self):
        common_name = REFERENCE_GUIDE["species"][self.species_number]["common_name"]
        return f"{common_name} - {self.band_number} - {self.date_time.strftime('%Y-%m-%d %H:%M')}"

    def clean(self):
        super().clean()

        self.validate_initials(self.bander_initials, "bander_initials", mandatory=True)

        # `scribe` is optional
        if self.scribe:  # Only validate if `scribe` is provided
            self.validate_initials(self.scribe, "scribe", mandatory=False)

        self.validate_species_to_wing()

        self.validate_wrp_to_species()

        self.validate_how_sexed_order()
        self.validate_sex_how_sexed()
        self.validate_band_size_to_species()

    def validate_species_to_wing(self):
        # Adjusted to access species information under the "species" key
        species_info = REFERENCE_GUIDE["species"].get(self.species_number)

        if species_info and self.wing_chord is not None:
            wing_chord_range = species_info.get("wing_chord_range", (0, 0))
            if not (wing_chord_range[0] <= self.wing_chord <= wing_chord_range[1]):
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

        # Automatically convert to uppercase if validation passes
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
        # Retrieve species information from REFERENCE_GUIDE using the species_number.
        target_species = REFERENCE_GUIDE["species"][self.species_number]

        # Extract WRP_groups for the species, which define the valid age_WRP codes.
        wrp_groups = target_species["WRP_groups"]

        # Compile a list of all allowed codes for the species, based on its WRP_groups.
        allowed_codes = []
        for group_number in wrp_groups:
            # Append allowed codes from each relevant WRP_group to the allowed_codes list.
            allowed_codes.extend(REFERENCE_GUIDE["wrp_groups"][group_number]["codes_allowed"])

        # Validate if the provided age_WRP is in the list of allowed codes.
        if self.age_WRP not in allowed_codes:
            # If not, raise a ValidationError with a detailed error message.
            raise ValidationError({
                "age_WRP": f"The age_WRP '{self.age_WRP}' is not allowed for the species '{target_species['common_name']}' with WRP_groups {wrp_groups}."
            })

    def validate_how_sexed_order(self):
        """
        Automatically adjust how_sexed_1 and how_sexed_2 fields to ensure logical data consistency.
        """
        # If how_sexed_1 is blank but how_sexed_2 is not, assign how_sexed_2 to how_sexed_1 and clear how_sexed_2.
        if not self.how_sexed_1 and self.how_sexed_2:
            self.how_sexed_1 = self.how_sexed_2
            self.how_sexed_2 = None  # or '' if you prefer to set it to an empty string

    def validate_sex_how_sexed(self):
        """
        Validate that how_sexed_1 and how_sexed_2 are provided with legitimate options
        for the sex of the bird. Raises a ValidationError if the criteria are not met.
        """

        # Check if the bird is identified as male or female and validate the methods
        if self.sex == "M":
            allowed_methods = {"C", "P", "W", "E", "O"}
        elif self.sex == "F":
            allowed_methods = {"B", "P", "E", "W", "O"}
        else:
            # If sex is unknown or not attempted, skip further validation
            return

        # Ensure how_sexed_1 is filled for birds with specified sex
        if not self.how_sexed_1:
            raise ValidationError({
                "how_sexed_1": "A method of determination is required for birds with specified sex."
            })

        # Validate how_sexed_1 and how_sexed_2 against the allowed methods
        invalid_methods = []
        if self.how_sexed_1 and self.how_sexed_1 not in allowed_methods:
            invalid_methods.append("how_sexed_1")
        if self.how_sexed_2 and self.how_sexed_2 not in allowed_methods:
            invalid_methods.append("how_sexed_2")

        # Raise ValidationError if any method is invalid
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
        # Retrieve species information from REFERENCE_GUIDE using the species_number.
        target_species = REFERENCE_GUIDE["species"][self.species_number]

        # Extract band_sizes for the species, which define the valid band_size codes.
        band_sizes = target_species["band_sizes"]

        # Validate if the provided band_size is in the list of allowed sizes.
        if self.band_size not in band_sizes:
            # If not, raise a ValidationError with a detailed error message.
            raise ValidationError({
                "band_size": f"The band_size '{self.band_size}' is not allowed for the species '{target_species['common_name']}' with band_sizes {band_sizes}."
            })
    
    def get_usgs_condition_code(self):
        # Look up the capture_code in the REFERENCE_GUIDE's "dispositions" section
        target_disposition = REFERENCE_GUIDE["dispositions"][self.capture_code]
        
        # Get the "usgs" sub-dictionary
        return target_disposition["usgs"]["code"]
    
    def get_usgs_how_aged_code(self):
        # If how_aged_1 is not set, return a blank string
        if not self.how_aged_1:
            return ""
        
        # Look up the how_aged_1 code in the REFERENCE_GUIDE's "how_aged" section
        target_how_aged = REFERENCE_GUIDE["how_aged"][self.how_aged_1]
        
        # Get the "usgs" sub-dictionary
        return target_how_aged["usgs"]["code"]
        

    def serialize_usgs(self):
        # Your playground
        target_species_alpha = REFERENCE_GUIDE["species"][self.species_number]["alpha_code"]
        return dict(
            band_number=self.band_number,
            species=target_species_alpha,
            dispostion=self.get_usgs_condition_code(),
            year=self.date_time.year,
            month=self.date_time.month,
            day=self.date_time.day,
            age=self.age_annual,
            how_aged=self.get_usgs_how_aged_code(),
        )
