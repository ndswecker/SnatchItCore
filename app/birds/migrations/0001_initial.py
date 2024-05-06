import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AgeAnnual",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "number",
                    models.IntegerField(
                        help_text="The integer code used to age a bird by the MAPS protocol"
                    ),
                ),
                (
                    "alpha",
                    models.CharField(
                        help_text="The 2 or 3 letter calendar age code of the bird as used by the BBL.",
                        max_length=3,
                        unique=True,
                    ),
                ),
                ("description", models.CharField(max_length=255)),
                ("explanation", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Band",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("size", models.CharField(max_length=2)),
                ("comment", models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                "ordering": ("size",),
            },
        ),
        migrations.CreateModel(
            name="AgeWRP",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "code",
                    models.CharField(
                        help_text="The 3 or 4 letter WRP age code of the bird.",
                        max_length=4,
                        unique=True,
                    ),
                ),
                (
                    "sequence",
                    models.IntegerField(
                        help_text="The order progression by life cycle stage. Lower numbers are younger birds."
                    ),
                ),
                (
                    "description",
                    models.CharField(
                        help_text="A 3 to 4 word description for the the 3 to 4 letter WRP group code.",
                        max_length=255,
                    ),
                ),
                (
                    "explanation",
                    models.TextField(
                        blank=True,
                        help_text="A longer explanation of the WRP group code, its meaning, and examples.",
                        null=True,
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("current", "Current"),
                            ("discontinued", "Discontinued"),
                        ],
                        default="current",
                        help_text="The current usage of the age code.",
                        max_length=20,
                    ),
                ),
                (
                    "annuals",
                    models.ManyToManyField(
                        help_text="The set of annual ages that can be assigned to a bird of this WRP age code.",
                        related_name="wrp_ages",
                        to="birds.ageannual",
                    ),
                ),
            ],
            options={
                "ordering": ("sequence",),
            },
        ),
        migrations.CreateModel(
            name="GroupWRP",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("number", models.IntegerField(unique=True)),
                (
                    "explanation",
                    models.TextField(
                        help_text="A longer explanation of the molt sequence."
                    ),
                ),
                (
                    "ages",
                    models.ManyToManyField(
                        help_text="The set of acceptable ages for a bird of this group.",
                        related_name="wrp_groups",
                        to="birds.agewrp",
                    ),
                ),
            ],
            options={
                "ordering": ("number",),
            },
        ),
        migrations.CreateModel(
            name="Taxon",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "common",
                    models.CharField(
                        help_text="The common name of the bird as determined by the AOU.",
                        max_length=255,
                    ),
                ),
                (
                    "scientific",
                    models.CharField(
                        help_text="The scientific name of the bird as determined by the AOU.",
                        max_length=255,
                    ),
                ),
                (
                    "number",
                    models.IntegerField(
                        default=0,
                        help_text="The species number of the bird as determined by SnatchItCore (BBL preferenced).",
                    ),
                ),
                (
                    "number_bbl",
                    models.IntegerField(
                        blank=True,
                        help_text="The species number of the bird as determined by the BBL.",
                        null=True,
                    ),
                ),
                (
                    "number_aou",
                    models.IntegerField(
                        blank=True,
                        help_text="The species number of the bird as determined by the AOU.",
                        null=True,
                    ),
                ),
                (
                    "alpha",
                    models.CharField(
                        default="TEMP",
                        help_text="The alpha code of the bird used by SnatchItCore (BBL preferenced).",
                        max_length=4,
                    ),
                ),
                (
                    "alpha_bbl",
                    models.CharField(
                        blank=True,
                        help_text="The alpha code of the bird as determined by the BBL.",
                        max_length=4,
                        null=True,
                    ),
                ),
                (
                    "alpha_aou",
                    models.CharField(
                        blank=True,
                        help_text="The alpha code of the bird as determined by the AOU.",
                        max_length=4,
                        null=True,
                    ),
                ),
                (
                    "taxonomic_order",
                    models.IntegerField(
                        blank=True,
                        help_text="The taxonomic order of the bird as determined by the BBL.",
                        null=True,
                    ),
                ),
                (
                    "page_number",
                    models.IntegerField(
                        blank=True,
                        help_text="The Second Edition Pyle page number of the bird. Could be part 1 or part 2.",
                        null=True,
                    ),
                ),
                ("wing_min", models.IntegerField(blank=True, null=True)),
                ("wing_max", models.IntegerField(blank=True, null=True)),
                ("tail_min", models.IntegerField(blank=True, null=True)),
                ("tail_max", models.IntegerField(blank=True, null=True)),
                ("wing_female_min", models.IntegerField(blank=True, null=True)),
                ("wing_female_max", models.IntegerField(blank=True, null=True)),
                ("wing_male_min", models.IntegerField(blank=True, null=True)),
                ("wing_male_max", models.IntegerField(blank=True, null=True)),
                ("tail_female_min", models.IntegerField(blank=True, null=True)),
                ("tail_female_max", models.IntegerField(blank=True, null=True)),
                ("tail_male_min", models.IntegerField(blank=True, null=True)),
                ("tail_male_max", models.IntegerField(blank=True, null=True)),
                ("exp_culmen_min", models.FloatField(blank=True, null=True)),
                ("exp_culmen_max", models.FloatField(blank=True, null=True)),
                ("tarsus_min", models.FloatField(blank=True, null=True)),
                ("tarsus_max", models.FloatField(blank=True, null=True)),
                ("sex_by_bp", models.BooleanField(blank=True, null=True)),
                ("sex_by_cp", models.BooleanField(blank=True, null=True)),
                ("sex_by_plumage", models.BooleanField(blank=True, null=True)),
                ("sex_by_wing", models.BooleanField(blank=True, null=True)),
                ("sex_by_tail", models.BooleanField(blank=True, null=True)),
                ("sex_by_exp_culmen", models.BooleanField(blank=True, null=True)),
                ("sex_by_tarsus", models.BooleanField(blank=True, null=True)),
                (
                    "upper_parts",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("wg_minus_tl_min", models.IntegerField(blank=True, null=True)),
                ("wg_minus_tl_max", models.IntegerField(blank=True, null=True)),
                ("bill_nares_min", models.FloatField(blank=True, null=True)),
                ("bill_nares_max", models.FloatField(blank=True, null=True)),
                ("bill_width_min", models.FloatField(blank=True, null=True)),
                ("bill_width_max", models.FloatField(blank=True, null=True)),
                ("p_minus_s_min", models.FloatField(blank=True, null=True)),
                ("p_minus_s_max", models.FloatField(blank=True, null=True)),
                ("p_minus_p6_min", models.FloatField(blank=True, null=True)),
                ("p_minus_p6_max", models.FloatField(blank=True, null=True)),
                ("p6_minus_p10_min", models.FloatField(blank=True, null=True)),
                ("p6_minus_p10_max", models.FloatField(blank=True, null=True)),
                ("p9_minus_p5_min", models.FloatField(blank=True, null=True)),
                ("p9_minus_p5_max", models.FloatField(blank=True, null=True)),
                ("p6_emarginated", models.BooleanField(blank=True, null=True)),
                (
                    "bands",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The acceptable band sizes for the bird listed in order of suitability.",
                        related_name="taxa",
                        to="birds.band",
                    ),
                ),
                (
                    "wrp_groups",
                    models.ManyToManyField(
                        blank=True, related_name="birds", to="birds.groupwrp"
                    ),
                ),
            ],
            options={
                "ordering": ("number_aou",),
            },
        ),
        migrations.CreateModel(
            name="BandAllocation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "sex",
                    models.CharField(
                        choices=[("m", "Male"), ("f", "Female"), ("u", "Unisex")],
                        default="u",
                        max_length=10,
                    ),
                ),
                (
                    "priority",
                    models.IntegerField(
                        help_text="A lower number means the band is more suitable for the bird."
                    ),
                ),
                (
                    "band",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="allocations",
                        to="birds.band",
                    ),
                ),
                (
                    "bird",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="band_sizes",
                        to="birds.taxon",
                    ),
                ),
            ],
            options={
                "ordering": ("bird", "priority"),
                "unique_together": {("bird", "band", "sex", "priority")},
            },
        ),
    ]
