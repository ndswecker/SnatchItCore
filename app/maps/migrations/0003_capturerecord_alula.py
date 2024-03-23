from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("maps", "0002_alter_capturerecord_band_number_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="capturerecord",
            name="alula",
            field=models.CharField(
                blank=True,
                choices=[
                    ("J", "J - Juvenile (OR Juv & Alternate)"),
                    ("L", "L - Limit of Juv & Formative"),
                    ("F", "F - Formative (OR Formative & Alternate)"),
                    ("B", "B - Basic (OR Basic & Alternate)"),
                    ("R", "R - Retained (Juv & Basic)"),
                    ("M", "M - Mixed Basic (woodpecker generally)"),
                    ("A", "A - Alternate (some or all)"),
                    (
                        "N",
                        "N - Non-juv (definitely no juv feathers, but Formative or Basic)",
                    ),
                    ("U", "U - Unknown"),
                ],
                max_length=1,
                null=True,
            ),
        ),
    ]
