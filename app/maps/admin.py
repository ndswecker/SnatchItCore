import csv
import datetime

from django.contrib import admin
from django.contrib import messages
from django.http import HttpResponse

from maps.models import CaptureRecord
from maps.serializers import USGSSerializer


class CaptureRecordAdmin(admin.ModelAdmin):
    list_display = ("band_number", "species_number", "date_time")
    list_filter = ("band_number", "species_number", "date_time")
    actions = [
        "export_csv_usgs",
    ]

    @admin.action(description="Export selected records to a USGS CSV")
    def export_csv_usgs(self, request, queryset):
        if queryset.count() > 1000:
            self.message_user(
                request=request,
                message="Exports capped at 1,000 records",
                level=messages.ERROR,
            )
            return False
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = f"attachment; filename={datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')}_USGS.csv"
        writer = csv.writer(response)
        writer.writerow(USGSSerializer(queryset.first()).serialize().keys())
        for obj in queryset:
            writer.writerow(USGSSerializer(obj).serialize().values())
        return response


admin.site.register(CaptureRecord, CaptureRecordAdmin)
