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
        validators=[
            MinValueValidator(0, "Skull must be at least 0."),
            MaxValueValidator(8, "Skull must be a single digit.")
        ]
    )

    cloacal_protuberance = models.IntegerField()
    brood_patch = models.IntegerField()
    fat = models.IntegerField()
    body_molt = models.IntegerField()
    ff_molt = models.CharField(max_length=1)
    ff_wear = models.IntegerField()
    juv_body_plumage = models.IntegerField(null=True, blank=True)  # Allow null and blank

    primary_coverts = models.CharField(
        max_length=1,
        null=True,
        blank=True)  # Allow null and blank
    
    secondary_coverts = models.CharField(max_length=1, null=True, blank=True)  # Allow null and blank
    primaries = models.CharField(max_length=1, null=True, blank=True)  # Allow null and blank
    rectrices = models.CharField(max_length=1, null=True, blank=True)  # Allow null and blank
    secondaries = models.CharField(max_length=1, null=True, blank=True)  # Allow null and blank
    tertials = models.CharField(max_length=1, null=True, blank=True)  # Allow null and blank
    body_plumage = models.CharField(max_length=1, null=True, blank=True)  # Allow null and blank
    non_feather = models.CharField(max_length=1, null=True, blank=True)  # Allow null and blank
    wing_chord = models.IntegerField()
    body_mass = models.DecimalField(max_digits=4, decimal_places=1)
    status = models.IntegerField()
    date_time = models.DateTimeField()
    station = models.CharField(max_length=4)
    net = models.CharField(max_length=4)
    disposition = models.CharField(max_length=1)
    note_number = models.CharField(max_length=2) # Allow use of NM for not MAPS record
    note = models.TextField()
    band_size = models.CharField(max_length=2)
    scribe = models.CharField(max_length=3)
    location = models.CharField(max_length=4)

    ## Fields not to be submitted by the user
    discrepancies = models.TextField()
    is_flagged_for_review = models.BooleanField(default=False)
