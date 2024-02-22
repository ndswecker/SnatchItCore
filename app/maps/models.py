from django.db import models

# Create your models here.
class CaptureRecord(models.Model): 
    # make band_number an integer field that is always of length 9
    band_number = models.IntegerField()
