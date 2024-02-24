from django.db import models
from common.models import BaseModel
from .banding_data_fields import CAPTURE_CODES



# Create your models here.
class CaptureRecord(BaseModel): 
    bander_initials = models.CharField(max_length=3)
    
    capture_code = models.CharField(
        max_length=1,
        choices=CAPTURE_CODES,
        default='N')
    
    band_number = models.IntegerField()
    species_name = models.CharField(max_length=50)
    alpha_code = models.CharField(max_length=4)
    age_annual = models.CharField(max_length=1)
    how_aged_1 = models.CharField(max_length=1)
    how_aged_2 = models.CharField(max_length=1)
    age_WRP = models.CharField(max_length=4)
    sex = models.CharField(max_length=1)
    how_sexed_1 = models.CharField(max_length=1)
    how_sexed_2 = models.CharField(max_length=1)
    skull = models.IntegerField()
    cloacal_protuberance = models.IntegerField()
    brood_patch = models.IntegerField()
    fat = models.IntegerField()
    body_molt = models.IntegerField()
    ff_molt = models.CharField(max_length=1)
    ff_wear = models.IntegerField()
    juv_body_plumage = models.IntegerField(null=True, blank=True)  # Allow null and blank
    primary_coverts = models.CharField(max_length=1, null=True, blank=True)  # Allow null and blank
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
