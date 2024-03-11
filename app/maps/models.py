import datetime

from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator
from django.db import models

from common.models import BaseModel
from maps.choice_definitions import *
from maps.maps_reference_data import *
from users.models import User


def rounded_down_datetime():
    now = datetime.datetime.now()
    rounding_down = (now.minute // 10) * 10
    rounded_minute = now.replace(minute=rounding_down, second=0, microsecond=0)
    return rounded_minute


class CaptureRecord(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bander_initials = models.CharField(
        max_length=3,
    )

    capture_code = models.CharField(
        max_length=1,
        choices=CAPTURE_CODE_CHOICES,
        default="N",
    )

    species_number = models.IntegerField(
        validators=[
            MinValueValidator(1000, message="Species number must be at least 4 digits long."),
            MaxValueValidator(9999, message="Species number must be less than 5 digits."),
        ],
        choices=SPECIES_CHOICES,
        default=5810,
    )

    band_size = models.CharField(
        max_length=2,
        choices=BAND_SIZE_CHOICES,
        default="1B",
    )

    band_number = models.IntegerField(
        validators=[
            MinValueValidator(100000000, message="Band number must be at least 9 digits long."),
            MaxValueValidator(999999999, message="Band number must be less than 10 digits."),
        ],
        default=123456789,
    )

    alpha_code = models.CharField(max_length=4)

    age_annual = models.IntegerField(
        choices=AGE_ANNUAL_CHOICES,
        default=1,
    )

    how_aged_1 = models.CharField(
        max_length=1,
        null=True,
        blank=True,
        choices=HOW_AGED_SEXED_CHOICES,
    )

    how_aged_2 = models.CharField(
        max_length=1,
        null=True,
        blank=True,
        choices=HOW_AGED_SEXED_CHOICES,
    )

    age_WRP = models.CharField(
        max_length=4,
        choices=AGE_WRP_CHOICES,
        default="MFCF",
    )

    sex = models.CharField(
        max_length=1,
        choices=SEX_CHOICES,
        default="U",
    )
    how_sexed_1 = models.CharField(
        max_length=1,
        null=True,
        blank=True,
        choices=HOW_AGED_SEXED_CHOICES,
    )
    how_sexed_2 = models.CharField(
        max_length=1,
        null=True,
        blank=True,
        choices=HOW_AGED_SEXED_CHOICES,
    )

    skull = models.IntegerField(
        choices=SKULL_CHOICES,
        null=True,
        blank=True,
    )

    cloacal_protuberance = models.IntegerField(
        choices=CLOACAL_PROTUBERANCE_CHOICES,
        null=True,
        blank=True,
    )

    brood_patch = models.IntegerField(
        choices=BROOD_PATCH_CHOICES,
        null=True,
        blank=True,
    )

    fat = models.IntegerField(
        choices=FAT_CHOICES,
        null=True,
        blank=True,
    )

    body_molt = models.IntegerField(
        choices=BODY_MOLT_CHOICES,
        null=True,
        blank=True,
    )

    ff_molt = models.CharField(
        max_length=1,
        choices=FLIGHT_FEATHER_MOLT_CHOICES,
        null=True,
        blank=True,
    )

    ff_wear = models.IntegerField(
        choices=FLIGHT_FEATHER_WEAR_CHOICES,
        null=True,
        blank=True,
    )

    juv_body_plumage = models.IntegerField(
        choices=JUVENILE_BODY_PLUMAGE_CHOICES,
        null=True,
        blank=True,
    )

    primary_coverts = models.CharField(
        choices=MOLT_LIMIT_PLUMAGE_CHOICES,
        max_length=1,
        null=True,
        blank=True,
    )

    secondary_coverts = models.CharField(
        choices=MOLT_LIMIT_PLUMAGE_CHOICES,
        max_length=1,
        null=True,
        blank=True,
    )

    primaries = models.CharField(
        max_length=1,
        choices=MOLT_LIMIT_PLUMAGE_CHOICES,
        null=True,
        blank=True,
    )

    secondaries = models.CharField(
        max_length=1,
        choices=MOLT_LIMIT_PLUMAGE_CHOICES,
        null=True,
        blank=True,
    )

    tertials = models.CharField(
        max_length=1,
        choices=MOLT_LIMIT_PLUMAGE_CHOICES,
        null=True,
        blank=True,
    )

    rectrices = models.CharField(
        max_length=1,
        choices=MOLT_LIMIT_PLUMAGE_CHOICES,
        null=True,
        blank=True,
    )

    body_plumage = models.CharField(
        max_length=1,
        choices=MOLT_LIMIT_PLUMAGE_CHOICES,
        null=True,
        blank=True,
    )

    non_feather = models.CharField(
        max_length=1,
        choices=MOLT_LIMIT_PLUMAGE_CHOICES,
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
        choices=STATUS_CHOICES,
        default=300,
    )

    date_time = models.DateTimeField(
        default=rounded_down_datetime,
    )

    station = models.CharField(
        max_length=4,
        choices=STATION_CHOICES,
        default="MORS",
    )

    net = models.CharField(
        max_length=4,
        default="15",
    )

    disposition = models.CharField(
        max_length=1,
        choices=DISPOSITION_CHOICES,
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

    scribe = models.CharField(
        max_length=3,
        null=True,
        blank=True,
    )

    location = models.CharField(
        max_length=4,
        choices=STATION_CHOICES,
        default="MORS",
    )

    discrepancies = models.TextField(null=True, blank=True)
    is_flagged_for_review = models.BooleanField(default=False)

    def __str__(self):
        common_name = SPECIES[self.species_number]["common_name"]
        return f"{common_name} - {self.band_number} - {self.date_time.strftime('%Y-%m-%d %H:%M')}"

    def clean(self):
        super().clean()

        self.fill_in_alpha_code()

        self.validate_how_aged_order()
        self.validate_juv_aging()
        self.validate_MLP_to_age()
        self.validate_skull_to_age()

        self.validate_status_disposition()
        self.validate_species_to_wing()
        self.validate_wrp_to_species()

        self.validate_how_sexed_order()
        self.validate_sex_how_sexed()

        self.validate_cloacal_protuberance()
        self.validate_cloacal_protuberance_sexing()

        self.validate_brood_patch()
        self.validate_brood_patch_sexing()

        self.validate_band_size_to_species()

    def fill_in_alpha_code(self):
        self.alpha_code = SPECIES[self.species_number]["alpha_code"]

    def validate_species_to_wing(self):
        if self.wing_chord is None:
            return

        wing_chord_range = SPECIES[self.species_number]["wing_chord_range"]
        if not (wing_chord_range[0] <= self.wing_chord <= wing_chord_range[1]):
            raise ValidationError(
                {
                    "wing_chord": (
                        f"Wing chord for {SPECIES[self.species_number]['common_name']} "
                        f"must be between {range[0]} and {range[1]}."
                    ),
                },
            )

    def validate_wrp_to_species(self):
        """
        Validates the age_WRP input against allowed codes for the given species_number.
        Checks if the provided age_WRP code is within the list of allowed codes for the species.
        Allowed codes are based on the WRP_groups the species belongs to, as defined in REFERENCE_GUIDE.
        Raises ValidationError if the age_WRP code is not allowed, indicating an invalid code or a mismatch.
        """

        target_species = SPECIES[self.species_number]
        wrp_groups = target_species["WRP_groups"]

        allowed_codes = []
        for group_number in wrp_groups:
            allowed_codes.extend(WRP_GROUPS[group_number]["codes_allowed"])

        if self.age_WRP not in allowed_codes:
            raise ValidationError(
                {
                    "age_WRP": f"The age_WRP {self.age_WRP} is not allowed for the species {target_species['common_name']} with WRP_groups {wrp_groups}.",  # noqa E501
                },
            )

    def validate_how_aged_order(self):
        if not self.how_aged_1 and self.how_aged_2:
            self.how_aged_1 = self.how_aged_2
            self.how_aged_2 = None

    def validate_how_sexed_order(self):
        if not self.how_sexed_1 and self.how_sexed_2:
            self.how_sexed_1 = self.how_sexed_2
            self.how_sexed_2 = None

    def validate_sex_how_sexed(self):
        if self.sex in ["U", "X"]:
            return

        male_criteria = ["C", "W", "E", "O", "P"]
        female_criteria = ["B", "P", "E", "W", "O"]

        # Checking if criteria are met
        if self.sex == "M" and not any(
            how_sexed in male_criteria for how_sexed in [self.how_sexed_1, self.how_sexed_2]
        ):
            raise ValidationError("A bird sexed male must have how_sexed_1 or how_sexed_2 as 'C', 'W', 'E', or 'O'.")

        if self.sex == "F" and not any(
            how_sexed in female_criteria for how_sexed in [self.how_sexed_1, self.how_sexed_2]
        ):
            raise ValidationError(
                "A bird sexed female must have how_sexed_1 or how_sexed_2 as 'B', 'P', 'E', 'W', or 'O'.",
            )

    def validate_cloacal_protuberance(self):
        if "C" in [self.how_sexed_1, self.how_sexed_2] and self.cloacal_protuberance in [None, 0]:
            raise ValidationError(
                {
                    "cloacal_protuberance": 
                    "Cloacal protuberance must be filled in for birds sexed by cloacal protuberance.",
                },
            )

        if self.sex == "F" and self.cloacal_protuberance not in [None, 0]:
            raise ValidationError(
                {
                    "cloacal_protuberance": "Cloacal protuberance must be None or 0 for female birds.",
                },
            )

    def validate_brood_patch(self):

        if "B" in [self.how_sexed_1, self.how_sexed_2] and (self.brood_patch is None or self.brood_patch <= 0):
            raise ValidationError(
                {
                    "brood_patch": "Brood patch must be greater than 0 for birds sexed by brood patch.",
                },
            )

    def validate_cloacal_protuberance_sexing(self):
        if ("C" in [self.how_sexed_1, self.how_sexed_2]) and not (
            SPECIES[self.species_number]["sexing_criteria"]["male_by_CP"]
        ):
            raise ValidationError(
                {
                    "cloacal_protuberance": "This species cannot be reliably sexed by CP",
                },
            )

    def validate_brood_patch_sexing(self):
        # If bird was sexed by brood patch...
        if "B" in [self.how_sexed_1, self.how_sexed_2]:
            sexing_criteria = SPECIES[self.species_number]["sexing_criteria"]

            # If the species does not exclusively use brood patch for sexing females...
            if not sexing_criteria["female_by_BP"]:
                # If males of the species may also develop brood patches...
                if self.brood_patch is None or self.brood_patch < 3:
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

    def validate_band_size_to_species(self):
        """
        Validates the band_size input against allowed sizes for the given species_number.
        This method checks if the provided band_size is within the list of allowed
        sizes for the species identified by species_number.
        The allowed sizes are determined based on the band_sizes the species belongs to,
        as defined in REFERENCE_GUIDE.
        Raises:
            ValidationError: If the band_size is not allowed for the species,
            indicating either an invalid size or a mismatch between the species and
            its typical band sizes.
        """
        target_species = SPECIES[self.species_number]
        band_sizes = target_species["band_sizes"]
        if self.band_size not in band_sizes:
            error_msg = (
                f"The band_size '{self.band_size}' is not allowed for the species "
                f"'{target_species['common_name']}' with band_sizes {band_sizes}."
            )
            raise ValidationError({"band_size": error_msg})

    def validate_status_disposition(self):
        if self.status == 000 and self.disposition not in ["D", "P"]:
            raise ValidationError(
                {
                    "disposition": "Disposition must be D or P if status is 000.",
                },
            )

        if self.disposition in ["B", "L", "S", "T", "W"] and self.status == 300:
            raise ValidationError(
                {
                    "status": "Status cannot be 300 if disposition is B, L, S, T, or W. Chose 500",
                },
            )

    def validate_juv_aging(self):
        # validate that if age is 4 or 2, then how_aged_1 must not be P
        if self.age_annual in [4, 2] and self.how_aged_1 == "P":
            raise ValidationError(
                {
                    "how_aged_1": "How aged cannot be P for HY or Local birds. Please choose J.",
                },
            )

    def validate_MLP_to_age(self):
        # validate that if age is not 1, then how_aged_1 must be filled in
        if self.age_annual != 1 and not self.how_aged_1:
            raise ValidationError(
                {
                    "how_aged_1": "How aged must be filled in for birds not of age 1.",
                },
            )

        # validate that if age is 5, and how_aged_1 is L, then how_aged_2 must be filled in
        if self.age_annual == 5 and self.how_aged_1 == "L" and not self.how_aged_2:
            raise ValidationError(
                {
                    "how_aged_2": "How aged must further separate HY from SY birds. Please fill in how_aged_2.",
                },
            )

        # validate that if either how_aged_1 or how_aged_2 is L or P, then one of the following fields must be filled in
        # primary_coverts, secondary_coverts, primaries, rectrices, secondaries, tertials, body_plumage, non_feather
        if self.how_aged_1 in ["L", "P"] or self.how_aged_2 in ["L", "P"]:
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

    def validate_skull_to_age(self):
        # validate that if how_aged_1 or how_aged_2 is S, then skull must be filled in
        if (self.how_aged_1 == "S" or self.how_aged_2 == "S") and not self.skull:
            raise ValidationError(
                {
                    "skull": "Skull must be filled in for birds aged by skull.",
                },
            )

        # validate that if skull is less than 5, then age_annual must be 2 or 4
        if self.skull and (self.skull < 5 and self.age_annual not in [2, 4]):
            raise ValidationError(
                {
                    "age_annual": "Age must be HY or L for birds with skull score less than 5.",
                },
            )

        # validate that if skull is 5 or 6, then age_annual must not be 2 or 4
        if self.skull in [5, 6] and self.age_annual in [2, 4]:
            raise ValidationError(
                {
                    "age_annual": "Age must be SY or ASY for birds with skull score of 5 or 6.",
                },
            )
