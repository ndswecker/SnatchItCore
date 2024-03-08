from django.contrib import admin

from breeding.models import BreedingRecord


class BreedingRecordAdmin(admin.ModelAdmin):
    pass


admin.site.register(BreedingRecord, BreedingRecordAdmin)
