from django.db import models
from common.models import BaseModel
from django.core.validators import MinValueValidator, MaxValueValidator
from .  import banding_data_fields



# Create your models here.
class CaptureRecord(BaseModel): 
    bander_initials = models.CharField(max_length=3)
    
    capture_code = models.CharField(
        max_length=1,
        choices=banding_data_fields.CAPTURE_CODES,
        default='N')
    
    band_number = models.IntegerField(
        validators=[
            MinValueValidator(100000000, message="Band number must be at least 9 digits long."),
            MaxValueValidator(999999999, message="Band number must be less than 10 digits.")
        ]
    )

    species_name = models.CharField(
        max_length=50,
        choices=banding_data_fields.SPECIES_NAMES,
        default='AMCR')
    
    alpha_code = models.CharField(max_length=4)
    
    age_annual = models.CharField(
        max_length=1,
        choices=banding_data_fields.AGE_ANNUAL,
        default='1')
    
    how_aged_1 = models.CharField(
        max_length=1,
        null=True,
        blank=True,
        choices=banding_data_fields.HOW_AGED_SEXED)
    
    how_aged_2 = models.CharField(
        max_length=1,
        null=True,
        blank=True,
        choices=banding_data_fields.HOW_AGED_SEXED
    )

    age_WRP = models.CharField(
        max_length=4,
        choices=banding_data_fields.AGE_WRP,
        default='MFCF')
    
    sex = models.CharField(
        max_length=1,
        choices=banding_data_fields.SEX,
        default='U')
    
    how_sexed_1 = models.CharField(
        max_length=1,
        null=True,
        blank=True,
        choices=banding_data_fields.HOW_AGED_SEXED
    )
    how_sexed_2 = models.CharField(
        max_length=1,
        null=True,
        blank=True,
        choices=banding_data_fields.HOW_AGED_SEXED
    )
    skull = models.IntegerField(
        choices=banding_data_fields.SKULL,
        null=True,
        blank=True,
    )

    cloacal_protuberance = models.IntegerField(
        choices=banding_data_fields.CLOACAL_PROTUBERANCE,
        null=True,
        blank=True,
    )

    brood_patch = models.IntegerField(
        choices=banding_data_fields.BROOD_PATCH,
        null=True,
        blank=True,
    )

    fat = models.IntegerField(
        choices=banding_data_fields.FAT,
        null=True,
        blank=True,
    )

    body_molt = models.IntegerField(
        choices=banding_data_fields.BODY_MOLT,
        null=True,
        blank=True,
    )

    ff_molt = models.CharField(
        max_length=1,
        choices=banding_data_fields.FLIGHT_FEATHER_MOLT,
        null=True,
        blank=True,
    )

    ff_wear = models.IntegerField(
        choices=banding_data_fields.FLIGHT_FEATHER_WEAR,
        null=True,
        blank=True,
    )

    juv_body_plumage = models.IntegerField(
        choices=banding_data_fields.JUVENILE_BODY_PLUMAGE,
        null=True, 
        blank=True)

    primary_coverts = models.CharField(
        choices=banding_data_fields.MOLT_LIMITS_PLUMAGE,
        max_length=1,
        null=True,
        blank=True)  # Allow null and blank
    
    secondary_coverts = models.CharField(
        choices=banding_data_fields.MOLT_LIMITS_PLUMAGE,
        max_length=1,
        null=True,
        blank=True)
    
    primaries = models.CharField(
        max_length=1,
        choices=banding_data_fields.MOLT_LIMITS_PLUMAGE,
        null=True,
        blank=True
    )

    rectrices = models.CharField(
        max_length=1,
        choices=banding_data_fields.MOLT_LIMITS_PLUMAGE,
        null=True,
        blank=True
    )

    secondaries = models.CharField(
        max_length=1,
        choices=banding_data_fields.MOLT_LIMITS_PLUMAGE,
        null=True,
        blank=True
    )

    tertials = models.CharField(
        max_length=1,
        choices=banding_data_fields.MOLT_LIMITS_PLUMAGE,
        null=True,
        blank=True
    )

    body_plumage = models.CharField(
        max_length=1,
        choices=banding_data_fields.MOLT_LIMITS_PLUMAGE,
        null=True,
        blank=True
    )

    non_feather = models.CharField(
        max_length=1,
        choices=banding_data_fields.MOLT_LIMITS_PLUMAGE,
        null=True,
        blank=True
    )

    wing_chord = models.IntegerField()

    body_mass = models.DecimalField(max_digits=4, decimal_places=1)

    status = models.IntegerField()

    date_time = models.DateTimeField()

    station = models.CharField(
        max_length=4,
        choices=banding_data_fields.STATIONS,)

    net = models.CharField(max_length=4)

    disposition = models.CharField(max_length=1)

    note_number = models.CharField(
        max_length=2,
        null=True,
        blank=True
    )

    note = models.TextField()

    band_size = models.CharField(
        max_length=2,
        choices=banding_data_fields.BAND_SIZES
    )

    scribe = models.CharField(max_length=3)
    
    location = models.CharField(max_length=4)

    ## Fields not to be submitted by the user
    discrepancies = models.TextField()
    is_flagged_for_review = models.BooleanField(default=False)
