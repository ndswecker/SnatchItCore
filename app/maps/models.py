import datetime

from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator
from django.db import models
from django.utils import timezone

from common.models import BaseModel
from maps.choice_definitions import *  # noqa F403
from maps.maps_reference_data import *  # noqa F403
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
        null=True,
        blank=True,
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

    alula = models.CharField(
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

    capture_time = models.DateTimeField(
        default=timezone.now,
    )

    hold_time = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,
        blank=True,
        help_text="Time in minutes between capture and release.",
    )

    station = models.CharField(
        max_length=4,
        choices=STATION_CHOICES,
        default="MORS",
    )

    net = models.IntegerField(
        validators=[
            MinValueValidator(1, message="Net must be at least 1."),
            MaxValueValidator(21, message="Net must be less than 22."),
        ],
        null=False,
        blank=False,
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

    discrepancies = models.TextField(null=True, blank=True)
    # We will default to true. Since the validattion is done in the form
    # we will assume that the data is valid unless the user clicks on the
    # override validation button.
    is_validated = models.BooleanField(default=True)

    def __str__(self):
        common_name = SPECIES[self.species_number]["common_name"]
        return f"{common_name} - {self.band_number} - {self.capture_time.strftime('%Y-%m-%d %H:%M')}"
