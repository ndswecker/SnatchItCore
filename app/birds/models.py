from django.db import models
from common.models import BaseModel

class Bird(BaseModel):
    common_name = models.CharField(max_length=255)
    scientific_name = models.CharField(max_length=255)
    bbl_species_number = models.IntegerField()
    aou_species_number = models.IntegerField()
    alpha_code = models.CharField(max_length=4)
    band_sizes = models.ManyToManyField("BandSize", related_name="birds")
    wrp_groups = models.ManyToManyField("WRPGroup", related_name="birds")
    page_number = models.IntegerField()

class WingchordRange(BaseModel):
    bird = models.ForeignKey(Bird, related_name="wing_chords", on_delete=models.CASCADE)
    species_min = models.IntegerField(null=True, blank=True)
    species_max = models.IntegerField(null=True, blank=True)
    female_min = models.IntegerField(null=True, blank=True)
    female_max = models.IntegerField(null=True, blank=True)
    male_min = models.IntegerField(null=True, blank=True)
    male_max = models.IntegerField(null=True, blank=True)

class BandSize(BaseModel):
    band_size = models.CharField(max_length=2)

class WRPGroup(BaseModel):
    group_number = models.IntegerField(unique=True)
    description = models.TextField()
    applicable_ages = models.ManyToManyField("WRPAge", related_name="wrp_groups")

class WRPAge(BaseModel):
    code = models.CharField(max_length=4, unique=True)
    description = models.TextField()
    age_annual = models.ForeignKey("AnnualAge", related_name="wrp_ages", on_delete=models.CASCADE)

class AnnualAge(BaseModel):
    BBL_code = models.CharField(max_length=3, unique=True)
    MAPS_code = models.IntegerField()
    description = models.TextField()
