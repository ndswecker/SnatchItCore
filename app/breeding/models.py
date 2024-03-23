from django.db import models

from common.models import BaseModel
from maps import maps_reference_data as REFERENCE_DATA
from users.models import User


class Status(BaseModel):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    species = models.CharField(max_length=4)
    period = models.IntegerField()
    status = models.CharField(max_length=2)
    station = models.CharField(
        max_length=4,
        choices=[(s, s) for s in REFERENCE_DATA.SITE_LOCATIONS.keys()],
        null=False,
        blank=False,
    )

    class Meta:
        verbose_name_plural = "Statuses"

    def __str__(self):
        return f"{self.species} - {self.period} - {self.station}"
