from django.contrib import admin

from birds.models import AgeAnnual
from birds.models import AgeWRP
from birds.models import Band
from birds.models import BandAllocation
from birds.models import GroupWRP
from birds.models import Taxon


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


class BandAllocationAdmin(admin.ModelAdmin):
    list_display = ("bird", "sex", "band", "priority")
    search_fields = ("bird__alpha", "bird__common", "band__size")

    def get_taxon_alpha(self, obj):
        return obj.bird.alpha

    get_taxon_alpha.short_description = "Species Alpha"

    def get_taxon_common(self, obj):
        return obj.bird.common

    get_taxon_common.short_description = "Species Common Name"

    ordering = ("bird",)

    list_filter = ("bird__alpha", "band__size")


admin.site.register(Band, BandAdmin)
admin.site.register(AgeAnnual, AgeAnnualAdmin)
admin.site.register(AgeWRP, AgeWRPAdmin)
admin.site.register(GroupWRP, GroupWRPAdmin)
admin.site.register(Taxon, TaxonAdmin)
admin.site.register(BandAllocation, BandAllocationAdmin)
