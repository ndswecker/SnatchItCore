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
    discrepancies = models.TextField(default=None)
    is_flagged_for_review = models.BooleanField(default=False)

    def clean(self):
        super().clean()

        self.validate_initials(self.bander_initials, "bander_initials", mandatory=True)

        # `scribe` is optional
        if self.scribe:  # Only validate if `scribe` is provided
            self.validate_initials(self.scribe, "scribe", mandatory=False)

        self.validate_species_to_wing()

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
