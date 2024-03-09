from django.contrib import admin

from netting.models import NettingRecord


class NettingRecordAdmin(admin.ModelAdmin):
    pass


admin.site.register(NettingRecord, NettingRecordAdmin)
