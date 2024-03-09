from django.db import models

from common.models import BaseModel
from users.models import User


class NettingRecord(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    period = models.IntegerField()
    date = models.DateField()
    numbers = models.CharField(max_length=255)
    open_time = models.TimeField()
    close_time = models.TimeField()
    hours = models.DecimalField(max_digits=5, decimal_places=2)
    period_net_hours = models.DecimalField(max_digits=5, decimal_places=2)
    note_number = models.IntegerField()
