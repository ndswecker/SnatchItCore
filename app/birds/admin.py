from django.contrib import admin
from birds.models import Band
from birds.models import AgeAnnual
from birds.models import AgeWRP


class BandAdmin(admin.ModelAdmin):
    list_display = ("size", "comment")
    search_fields = ("band", "comment")
    list_filter = ("size",)
    ordering = ("size",)


class AgeAnnualAdmin(admin.ModelAdmin):
    list_display = ("number", "alpha", "description")
    search_fields = ("number", "alpha")
    ordering = ("number",)


class AgeWRPAdmin(admin.ModelAdmin):
    list_display = ("code", "description")
    search_fields = ("number", "alpha")
    ordering = ("sequence",)


admin.site.register(Band, BandAdmin)
admin.site.register(AgeAnnual, AgeAnnualAdmin)
admin.site.register(AgeWRP, AgeWRPAdmin)
