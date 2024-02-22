from django.db import models
from common.models import BaseModel

# Create your models here.
class CaptureRecord(BaseModel): 
    # make band_number an integer field that is always of length 9
    band_number = models.IntegerField()
