from django.contrib import admin

from breeding.models import Status


class StatusAdmin(admin.ModelAdmin):
    list_display = (
        "__str__",
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


admin.site.register(Status, StatusAdmin)
