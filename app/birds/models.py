from django.db import models

class Taxon(models.Model):
    # Fields applicable to all birds
    common = models.CharField(
        max_length=255,
        help_text="The common name of the bird as determined by the AOU.",
    )

    scientific = models.CharField(
        max_length=255,
        help_text="The scientific name of the bird as determined by the AOU.",
    )

    number = models.IntegerField(
        default=0,
        help_text="The species number of the bird as determined by SnatchItCore (BBL preferenced).",
    )

    number_bbl = models.IntegerField(
        null=True,
        blank=True,
        help_text="The species number of the bird as determined by the BBL.",
    )

    number_aou = models.IntegerField(
        null=True,
        blank=True,
        help_text="The species number of the bird as determined by the AOU.",
    )

    alpha = models.CharField(
        default="TEMP",
        max_length=4,
        help_text="The alpha code of the bird used by SnatchItCore (BBL preferenced).",
    )

    alpha_bbl = models.CharField(
        null=True,
        blank=True,
        max_length=4,
        help_text="The alpha code of the bird as determined by the BBL.",
    )

    alpha_aou = models.CharField(
        null=True,
        blank=True,
        max_length=4,
        help_text="The alpha code of the bird as determined by the AOU.",
    )

    taxonomic_order = models.IntegerField(
        null=True,
        blank=True,
        help_text="The taxonomic order of the bird as determined by the BBL.",
    )

    page_number = models.IntegerField(
        null=True,
        blank=True,
        help_text="The Second Edition Pyle page number of the bird. Could be part 1 or part 2.",
    )

    wrp_groups = models.ManyToManyField(
        "GroupWRP", 
        blank=True,
        related_name="birds"
    )

    # Fields that are required for all birds that are banded
    bands = models.ManyToManyField(
        "Band",
        blank=True,
        related_name="taxa",
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

    # Fields for extended morphology (Flycatchers and a few other species)
    upper_parts = models.CharField(
        null=True,
        blank=True,
        max_length=255
    )
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

    class Meta:
        ordering = ("number_aou",)

    def __str__(self):
        return self.alpha
    

class Band(models.Model):
    size = models.CharField(max_length=2)
    comment = models.CharField(
        null=True,
        blank=True,
        max_length=255,
    )

    class Meta:
        ordering = ("size",)

    def __str__(self):
        return self.size


class BandAllocation(models.Model):
    """
    Represents the band sizes applicable to a bird, with specific preferences 
    based on species and sex. The model links birds to their possible 
    band sizes and orders the sizes by preference.
    """

    bird = models.ForeignKey(
        "Taxon", 
        on_delete=models.CASCADE,
        related_name="band_sizes", 
    )

    band = models.ForeignKey(
        "Band", 
        on_delete=models.CASCADE,
        related_name="allocations", 
    )

    sex = models.CharField(
        choices = [
            ("M", "Male"),
            ("F", "Female"),
            ("U", "Unisex"),
        ],
        default = 'U',
        max_length = 10,
    )

    priority = models.IntegerField(
        help_text="A lower number means the band is more suitable for the bird.",
    )

    class Meta:
        unique_together = ("bird", "band", "sex", "priority")
        ordering = ("bird", "priority")

    def __str__(self):
        return f"{self.bird} {self.band}"


class GroupWRP(models.Model):
    """
    Wolfe-Ryder-Pyle (WRP) groups are a way to group birds by similar molt strategies.
    Within each group there are a set of acceptable ages that can be assigned to a bird of that group.
    """
    number = models.IntegerField(unique=True)

    explanation = models.TextField(
        help_text="A longer explanation of the molt sequence.",
    )

    ages = models.ManyToManyField(
        "AgeWRP", 
        related_name="wrp_groups",
        help_text="The set of acceptable ages for a bird of this group.",
    )

    class Meta:
        ordering = ("number",)


class AgeWRP(models.Model):
    STATUS_CHOICES = [
        ("current", "Current"),
        ("discontinued", "Discontinued"),
    ]
    code = models.CharField(
        unique=True,
        max_length=4, 
        help_text="The 3 or 4 letter WRP age code of the bird.",
    )

    sequence = models.IntegerField(
        help_text="The order progression by life cycle stage. Lower numbers are younger birds.",
    )

    description = models.CharField(
        max_length=255,
        help_text="A 3 to 4 word description for the the 3 to 4 letter WRP group code.",
    )

    explanation = models.TextField(
        null=True,
        blank=True,
        help_text="A longer explanation of the WRP group code, its meaning, and examples.",
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="current",
        help_text="The current usage of the age code.",
    )

    annuals = models.ManyToManyField(
        "AgeAnnual", 
        related_name="wrp_ages",
        help_text="The set of annual ages that can be assigned to a bird of this WRP age code.",
    )

    class Meta:
        ordering = ("sequence",)

    def __str__(self):
        return self.code


class AgeAnnual(models.Model):
    number = models.IntegerField(
        help_text="The integer code used to age a bird by the MAPS protocol",
    )

    alpha = models.CharField(
        max_length=3, 
        unique=True,
        help_text="The 2 or 3 letter calendar age code of the bird as used by the BBL.",
    )

    description = models.CharField(max_length=255)
    explanation = models.TextField()

    def __str__(self):
        return f"{self.number} {self.alpha}"
