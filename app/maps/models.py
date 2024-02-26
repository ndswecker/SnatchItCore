from django.db import models
from common.models import BaseModel
from django.core.validators import MinValueValidator, MaxValueValidator
from maps.banding_data_fields import *



# Create your models here.
class CaptureRecord(BaseModel): 
    bander_initials = models.CharField(
        max_length=3,
        default='JSM'
    )
    
    capture_code = models.CharField(
        max_length=1,
        choices=CAPTURE_CODES,
        default='N')
    
    band_number = models.IntegerField(
        validators=[
            MinValueValidator(100000000, message="Band number must be at least 9 digits long."),
            MaxValueValidator(999999999, message="Band number must be less than 10 digits.")
        ],
        default=123456789
    )

    species_name = models.CharField(
        max_length=50,
        choices=SPECIES_NAMES,
        default='SOSP'
    )

    alpha_code = models.CharField(max_length=4)
    
    age_annual = models.CharField(
        max_length=1,
        choices=AGE_ANNUAL_OPTIONS,
        default='1')
    
    how_aged_1 = models.CharField(
        max_length=1,
        null=True,
        blank=True,
        choices=HOW_AGED_SEXED_OPTIONS)
    
    how_aged_2 = models.CharField(
        max_length=1,
        null=True,
        blank=True,
        choices=HOW_AGED_SEXED_OPTIONS
    )

    age_WRP = models.CharField(
        max_length=4,
        choices=AGE_WRP_OPTIONS,
        default='MFCF')
    
    sex = models.CharField(
        max_length=1,
        choices=SEXES,
        default='U')
    
    how_sexed_1 = models.CharField(
        max_length=1,
        null=True,
        blank=True,
        choices=HOW_AGED_SEXED_OPTIONS
    )
    how_sexed_2 = models.CharField(
        max_length=1,
        null=True,
        blank=True,
        choices=HOW_AGED_SEXED_OPTIONS
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
        choices=BODY_MOLTS,
        null=True,
        blank=True,
    )

    ff_molt = models.CharField(
        max_length=1,
        choices=FLIGHT_FEATHER_MOLTS,
        null=True,
        blank=True,
    )

    ff_wear = models.IntegerField(
        choices=FLIGHT_FEATHER_WEARS,
        null=True,
        blank=True,
    )

    juv_body_plumage = models.IntegerField(
        choices=JUVENILE_BODY_PLUMAGES,
        null=True, 
        blank=True)

    primary_coverts = models.CharField(
        choices=MOLT_LIMITS_PLUMAGES,
        max_length=1,
        null=True,
        blank=True) 
    
    secondary_coverts = models.CharField(
        choices=MOLT_LIMITS_PLUMAGES,
        max_length=1,
        null=True,
        blank=True)
    
    primaries = models.CharField(
        max_length=1,
        choices=MOLT_LIMITS_PLUMAGES,
        null=True,
        blank=True
    )

    rectrices = models.CharField(
        max_length=1,
        choices=MOLT_LIMITS_PLUMAGES,
        null=True,
        blank=True
    )

    secondaries = models.CharField(
        max_length=1,
        choices=MOLT_LIMITS_PLUMAGES,
        null=True,
        blank=True
    )

    tertials = models.CharField(
        max_length=1,
        choices=MOLT_LIMITS_PLUMAGES,
        null=True,
        blank=True
    )

    body_plumage = models.CharField(
        max_length=1,
        choices=MOLT_LIMITS_PLUMAGES,
        null=True,
        blank=True
    )

    non_feather = models.CharField(
        max_length=1,
        choices=MOLT_LIMITS_PLUMAGES,
        null=True,
        blank=True
    )

    wing_chord = models.IntegerField(
        validators=[
            MinValueValidator(10, message="Wing chord must be at least 0."),
            MaxValueValidator(300, message="Wing chord must be less than 300.")
        ],
        null=True,
        blank=True
    )

    body_mass = models.DecimalField(
        max_digits=4,
        decimal_places=1,
        validators=[
            MinValueValidator(0, message="Mass must be at least 0."),
            MaxValueValidator(999.9, message="Mass must be less than 10000.")
        ],
        null=True,
        blank=True,
    )

    status = models.IntegerField(
        validators=[
            MinValueValidator(0, message="Status must be at least 000."),
            MaxValueValidator(999, message="Status must be less than 1000.")
        ],
        default=300
    )

    date_time = models.DateTimeField(
        default='2024-02-26 02:53:08',
    )

    station = models.CharField(
        max_length=4,
        choices=STATIONS,
        default='MORS'
    )

    net = models.CharField(
        max_length=4,
        default='15'
    )

    disposition = models.CharField(
        max_length=1,
        choices=DISPOSITIONS,
        null=True,
        blank=True,    
    )

    note_number = models.CharField(
        max_length=2,
        null=True,
        blank=True
    )

    note = models.TextField(
        null=True,
        blank=True
    )

    band_size = models.CharField(
        max_length=2,
        choices=BAND_SIZES,
        default='1B'
    )

    scribe = models.CharField(
        max_length=3,
        null=True,
        blank=True
    )
    
    location = models.CharField(
        max_length=4,
        null=True,
        blank=True,
    )

    ## Fields not to be submitted by the user
    discrepancies = models.TextField()
    is_flagged_for_review = models.BooleanField(default=False)
