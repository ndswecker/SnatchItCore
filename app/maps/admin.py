import csv
import datetime

from django.contrib import admin
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import path

from maps.data_importer import IBPDataImporter
from maps.forms import CSVUploadForm
from maps.models import CaptureRecord
from maps.serializers import IBPSerializer
from maps.serializers import USGSSerializer


class CaptureRecordAdmin(admin.ModelAdmin):
    list_display = (
        "capture_code",
        "band_number",
        "is_validated",
        "scribe_initials",
        "species_number",
        "capture_time",
    )
    list_filter = (
        "station",
        "is_validated",
        "capture_code",
        "scribe_initials",
        "species_number",
        "capture_time",
    )
    actions = [
        "export_csv_usgs",
        "export_csv_ibp",
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
        response["Content-Disposition"] = (
            f"attachment; filename={datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')}_USGS.csv"  # noqa
        )
        writer = csv.writer(response)
        writer.writerow(USGSSerializer(queryset.first()).serialize().keys())
        for obj in queryset:
            # Skip records with capture code "U" and "R"
            if obj.capture_code in ["U", "R"]:
                continue  # Skip this record and move on to the next one
            writer.writerow(USGSSerializer(obj).serialize().values())
        return response

    @admin.action(description="Export selected records to an IBP CSV")
    def export_csv_ibp(self, request, queryset):
        if queryset.count() > 1000:
            self.message_user(
                request=request,
                message="Exports capped at 1,000 records",
                level=messages.ERROR,
            )
            return False

        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = (
            f"attachment; filename={datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')}_IBP.csv"  # noqa
        )
        writer = csv.writer(response)

        if queryset.exists():
            writer.writerow(IBPSerializer(queryset.first()).serialize().keys())

        for obj in queryset:
            writer.writerow(IBPSerializer(obj).serialize().values())

        return response
    
    @admin.action(description="Import IBP CSV Data")
    def import_ibp_data(self, request, queryset):
        if 'apply' in request.POST:
            form = CSVUploadForm(request.POST, request.FILES)
            if form.is_valid():
                csv_file = request.FILES['csv_file']
                importer = IBPDataImporter(csv_file)
                importer.parse_csv()
                self.message_user(request, "Data imported successfully.")
                return HttpResponseRedirect(request.get_full_path())
        else:
            form = CSVUploadForm()
        
        return render(request, "admin/import_ibp_data.html", {"form": form})
    
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path(
                "import-ibp-data/",
                self.admin_site.admin_view(self.import_ibp_data),
                name="import_ibp_data",
            )
        ]
        return custom_urls + urls


admin.site.register(CaptureRecord, CaptureRecordAdmin)
