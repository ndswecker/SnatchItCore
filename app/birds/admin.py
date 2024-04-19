from django.contrib import admin
from birds.models import Band
from birds.models import Taxon
from birds.models import AgeAnnual
from birds.models import AgeWRP
from birds.models import GroupWRP


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

class GroupWRPAdmin(admin.ModelAdmin):
    list_display = ("number",)
    search_fields = ("number", "ages")
    ordering = ("number",)

class TaxonAdmin(admin.ModelAdmin):
    list_display = ("common", "alpha", "number")
    search_fields = ("common", "alpha")
    ordering = ("taxonomic_order",)


admin.site.register(Band, BandAdmin)
admin.site.register(AgeAnnual, AgeAnnualAdmin)
admin.site.register(AgeWRP, AgeWRPAdmin)
admin.site.register(GroupWRP, GroupWRPAdmin)
admin.site.register(Taxon, TaxonAdmin)
