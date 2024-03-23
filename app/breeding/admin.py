import csv
import datetime

from django.contrib import admin
from django.http import HttpResponse
from django.utils import timezone

from breeding.models import Status
from breeding.serializers import StatusSerializer


class StatusAdmin(admin.ModelAdmin):
    pass


admin.site.register(Status, StatusAdmin)
