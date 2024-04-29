# Generated by Django 5.0.4 on 2024-04-19 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("birds", "0003_alter_agewrp_explanation"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="band",
            options={"ordering": ("size",)},
        ),
        migrations.AddField(
            model_name="taxon",
            name="alpha",
            field=models.CharField(
                default="TEMP",
                help_text="The alpha code of the bird used by SnatchItCore (BBL preferenced).",
                max_length=4,
            ),
        ),
        migrations.AddField(
            model_name="taxon",
            name="number",
            field=models.IntegerField(
                default=0,
                help_text="The species number of the bird as determined by SnatchItCore (BBL preferenced).",
            ),
        ),
        migrations.AlterField(
            model_name="taxon",
            name="alpha_bbl",
            field=models.CharField(
                blank=True,
                help_text="The alpha code of the bird as determined by the BBL.",
                max_length=4,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="taxon",
            name="number_aou",
            field=models.IntegerField(
                blank=True,
                help_text="The species number of the bird as determined by the AOU.",
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="taxon",
            name="upper_parts",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="taxon",
            name="wrp_groups",
            field=models.ManyToManyField(
                blank=True, related_name="birds", to="birds.groupwrp"
            ),
        ),
    ]
