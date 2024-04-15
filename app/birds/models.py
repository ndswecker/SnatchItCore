from django.db import models
from common.models import BaseModel

class Bird(BaseModel):
    # Fields that are required for all birds
    common = models.CharField(
        max_length=255,
        help_text="The common name of the bird as determined by the AOU.",
    )
    scientific = models.CharField(
        max_length=255,
        help_text="The scientific name of the bird as determined by the AOU.",
    )
    number_bbl = models.IntegerField(
        help_text="The species number of the bird as determined by the BBL.",
    )
    number_aou = models.IntegerField(
        help_text="The species number of the bird as determined by the AOU.",
    )
    alpha_bbl = models.CharField(
        max_length=4,
        help_text="The alpha code of the bird as determined by the BBL.",
    )
    alpha_aou = models.CharField(
        max_length=4,
        help_text="The alpha code of the bird as determined by the AOU.",
    )
    page_number = models.IntegerField(
        help_text="The Second Edition Pyle page number of the bird. Could be part 1 or part 2.",
    )
    wrp_groups = models.ManyToManyField("GroupWRP", related_name="birds")

    # Fields that are required for all birds that are banded
    bands = models.ManyToManyField(
        "Band",
        related_name="birds",
        help_text="The acceptable band sizes for the bird listed in order of suitability.",
    )

    # Fields that are required for almost all birds that are banded
    wing_min = models.IntegerField(null=True, blank=True)
    wing_max = models.IntegerField(null=True, blank=True)

    # Fields that are required for birds that can be sexed by wing chord
    wing_female_min = models.IntegerField(null=True, blank=True)
    wing_female_max = models.IntegerField(null=True, blank=True)
    wing_male_min = models.IntegerField(null=True, blank=True)
    wing_male_max = models.IntegerField(null=True, blank=True)

    # Fields that are often listed in pyle for species and sex determination
    exp_culmen_min = models.FloatField(null=True, blank=True)
    exp_culmen_max = models.FloatField(null=True, blank=True)
    tarsus_min = models.FloatField(null=True, blank=True)
    tarsus_max = models.FloatField(null=True, blank=True)

    # Fields that tell users how a species can be sexed
    sex_by_bp = models.BooleanField(null=True, blank=True)
    sex_by_cp = models.BooleanField(null=True, blank=True)
    sex_by_plumage = models.BooleanField(null=True, blank=True)
    sex_by_wing = models.BooleanField(null=True, blank=True)
    sex_by_tail = models.BooleanField(null=True, blank=True)
    sex_by_exp_culmen = models.BooleanField(null=True, blank=True)
    sex_by_tarsus = models.BooleanField(null=True, blank=True)

class Band(BaseModel):
    size = models.CharField(max_length=2)

class BirdBandSize(BaseModel):
    """
    Represents he band sizes applicable to a bird, with specific preferences 
    based on species and sex. The model links birds to their possible 
    band sizes and orders the sizes by preference.
    """

    bird = models.ForeignKey("Bird", related_name="band_sizes", on_delete=models.CASCADE)
    band = models.ForeignKey("Band", related_name="bird_sizes", on_delete=models.CASCADE)
    sex = models.CharField(
        choices = [
            ("M", "Male"),
            ("F", "Female"),
            ("U", "Unisex"),
        ],
        default = 'U',
    ),
    order = models.IntegerField(
        help_text="A lower number means the band is more suitable for the bird.",
    )

    class Meta:
        unique_together = ("bird", "band", "sex", "order")
        ordering = ("bird", "order")

class GroupWRP(BaseModel):
    number = models.IntegerField(unique=True)
    description = models.TextField()
    ages = models.ManyToManyField("AgeWRP", related_name="wrp_groups")

class AgeWRP(BaseModel):
    code = models.CharField(max_length=4, unique=True)
    description = models.TextField()
    annual = models.ForeignKey("AgeAnnual", related_name="wrp_ages", on_delete=models.CASCADE)

class AgeAnnual(BaseModel):
    bbl = models.CharField(max_length=3, unique=True)
    maps = models.IntegerField()
    description = models.TextField()

# Specific to Flycatchers, and perhaps other birds
class MorphologyExtended(BaseModel):
    bird = models.OneToOneField("Bird", related_name="morphology", on_delete=models.CASCADE)
    upper_parts = models.CharField(max_length=255)
    wg_minus_tl_min = models.IntegerField(null=True, blank=True)
    wg_minus_tl_max = models.IntegerField(null=True, blank=True)
    bill_nares_min = models.FloatField(null=True, blank=True)
    bill_nares_max = models.FloatField(null=True, blank=True)
    bill_width_min = models.FloatField(null=True, blank=True)
    bill_width_max = models.FloatField(null=True, blank=True)
    p_minus_s_min = models.FloatField(null=True, blank=True)
    p_minus_s_max = models.FloatField(null=True, blank=True)
    p_minus_p6_min = models.FloatField(null=True, blank=True)
    p_minus_p6_max = models.FloatField(null=True, blank=True)
    p6_minus_p10_min = models.FloatField(null=True, blank=True)
    p6_minus_p10_max = models.FloatField(null=True, blank=True)
    p9_minus_p5_min = models.FloatField(null=True, blank=True)
    p9_minus_p5_max = models.FloatField(null=True, blank=True)
    p6_emarginated = models.BooleanField(null=True, blank=True)
