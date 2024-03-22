import csv
import datetime

from django.contrib import admin
from django.http import HttpResponse
from django.utils import timezone

from breeding.models import Report
from breeding.models import Station
from breeding.models import Status
from breeding.serializers import StatusSerializer


class StationAdmin(admin.ModelAdmin):
    pass


admin.site.register(Station, StationAdmin)


class ReportAdmin(admin.ModelAdmin):
    pass

    # @admin.action(description="Export report CSV")
    # def export_csv(self, request, queryset):
    #     response = HttpResponse(content_type="text/csv")
    #     response["Content-Disposition"] = (
    #         f"attachment; filename={timezone.now().strftime('%Y-%m-%d %H:%M:%S')}_USGS.csv"  # noqa
    #     )
    #     writer = csv.writer(response)
    #     writer.writerow(ReportSerializer(queryset.first()).serialize().keys())
    #     for obj in queryset:
    #         writer.writerow(StatusSerializer(obj).serialize().values())
    #     return response


admin.site.register(Report, ReportAdmin)


class StatusAdmin(admin.ModelAdmin):
    pass


admin.site.register(Status, StatusAdmin)
