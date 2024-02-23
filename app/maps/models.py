from django.db import models
from common.models import BaseModel

# Create your models here.
class CaptureRecord(BaseModel): 
    bander_initials = models.CharField()
    record_code = models.CharField()
    band_number = models.IntegerField()
    species_name = models.CharField()
    alpha_code = models.CharField()
    age_annual = models.CharField()
    how_aged_1 = models.CharField()
    how_aged_2 = models.CharField()
    age_WRP = models.CharField()
    sex = models.CharField()
    how_sexed_1 = models.CharField()
    how_sexed_2 = models.CharField()
    skull = models.IntegerField()
    cloacal_protuberance = models.IntegerField()
    brood_patch = models.IntegerField()
    fat = models.IntegerField()
    body_molt = models.IntegerField()
    ff_molt = models.CharField()
    ff_wear = models.IntegerField()
    juv_body_plumage = models.IntegerField()
    primary_coverts = models.CharField()
    secondary_coverts = models.CharField()
    primaries = models.CharField()
    rectrices = models.CharField()
    secondaries = models.CharField()
    tertials = models.CharField()
    body_plumage = models.CharField()
    non_feather = models.CharField()
    wing_chord = models.IntegerField()
    body_mass = models.DecimalField()
    status = models.IntegerField()
    date_time = models.DateTimeField()
    station = models.CharField()
    net = models.CharField()
    disposition = models.CharField()
    note_number = models.IntegerField()
    note = models.TextField()
    band_size = models.CharField()
    scriber = models.CharField()
    location = models.CharField()
