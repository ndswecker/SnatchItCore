from django.db import models
from common.models import BaseModel

class Bird(BaseModel):
    common = models.CharField(max_length=255)
    scientific = models.CharField(max_length=255)
    number_bbl = models.IntegerField()
    number_aou = models.IntegerField()
    alpha_bbl = models.CharField(max_length=4)
    alpha_aou = models.CharField(max_length=4)
    bands = models.ManyToManyField("Band", related_name="birds")
    wrp_groups = models.ManyToManyField("WRPGroup", related_name="birds")
    page_number = models.IntegerField()
    wing_min = models.IntegerField(null=True, blank=True)
    wing_max = models.IntegerField(null=True, blank=True)
    wing_min_female = models.IntegerField(null=True, blank=True)
    wing_max_female = models.IntegerField(null=True, blank=True)
    wing_min_male = models.IntegerField(null=True, blank=True)
    wing_max_male = models.IntegerField(null=True, blank=True)

class Band(BaseModel):
    size = models.CharField(max_length=2)

class GroupWRP(BaseModel):
    number = models.IntegerField(unique=True)
    description = models.TextField()
    # age = models.ForeignKey("AgeWRP", related_name="wrp_groups", on_delete=models.CASCADE)
    applicable_ages = models.ManyToManyField("AgeWRP", related_name="wrp_groups")

class AgeWRP(BaseModel):
    code = models.CharField(max_length=4, unique=True)
    description = models.TextField()
    annual = models.ForeignKey("AgeAnnual", related_name="wrp_ages", on_delete=models.CASCADE)

class AgeAnnual(BaseModel):
    bbl = models.CharField(max_length=3, unique=True)
    maps = models.IntegerField()
    description = models.TextField()
