from django.db import models

from common.models import BaseModel
from users.models import User


class BreedingRecord(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    hawo = models.CharField("HAWO", max_length=100)
    acfl = models.CharField("ACFL", max_length=100)
    ytvi = models.CharField("YTVI", max_length=100)
    revi = models.CharField("REVI", max_length=100)
    tres = models.CharField("TRES", max_length=100)
    cach = models.CharField("CACH", max_length=100)
    woth = models.CharField("WOTH", max_length=100)
    gcth = models.CharField("GCTH", max_length=100)
    amro = models.CharField("AMRO", max_length=100)
    grca = models.CharField("GRCA", max_length=100)
    nopa = models.CharField("NOPA", max_length=100)
    ywar = models.CharField("YWAR", max_length=100)
    amre = models.CharField("AMRE", max_length=100)
    initials = models.CharField(max_length=100)
