import csv
import datetime

from django.contrib import admin
from django.http import HttpResponse
from django.utils import timezone

from breeding.models import Status
from breeding.serializers import StatusSerializer


class StatusAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
        "station",
        "species",
        "period",
        "status",
        "user",
    )
    list_filter = (
        "species",
        "period",
        "status",
        "station",
    )
    actions = [

    ]


admin.site.register(Status, StatusAdmin)
