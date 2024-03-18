import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("maps", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="capturerecord",
            name="band_number",
            field=models.IntegerField(
                blank=True,
                default=123456789,
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(
                        100000000, message="Band number must be at least 9 digits long."
                    ),
                    django.core.validators.MaxValueValidator(
                        999999999, message="Band number must be less than 10 digits."
                    ),
                ],
            ),
        ),
        migrations.AlterField(
            model_name="capturerecord",
            name="band_size",
            field=models.CharField(
                choices=[
                    ("0A", "0A"),
                    ("0", "0"),
                    ("1", "1"),
                    ("1A", "1A"),
                    ("1B", "1B"),
                    ("1D", "1D"),
                    ("2", "2"),
                    ("3", "3"),
                    ("3A", "3A"),
                    ("3B", "3B"),
                    ("4", "4"),
                    ("R", "Recap"),
                    ("U", "Unbanded"),
                ],
                default="1B",
                max_length=2,
            ),
        ),
    ]
