from django.contrib import admin

from maps.models import CaptureRecord


class CaptureRecordAdmin(admin.ModelAdmin):
    list_display = ("band_number", "species_number", "date_time")
    list_filter = ("band_number", "species_number", "date_time")


admin.site.register(CaptureRecord, CaptureRecordAdmin)
