from django.db import models

from common.models import BaseModel
from users.models import User


class Station(BaseModel):
    name = models.CharField(max_length=256)


class Report(BaseModel):
    station = models.ForeignKey(Station, on_delete=models.CASCADE)
    year = models.IntegerField()


class Status(BaseModel):
    #  TODO: associate status with specific report
    # report = models.ForeignKey(Report, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    species = models.CharField(max_length=4)  # TODO: use species number
    period = models.IntegerField()
    status = models.CharField(max_length=2)

    class Meta:
        verbose_name_plural = "Statuses"

    def __str__(self):
        return f"{self.species} - {self.period} - {self.status}"
