from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("maps", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="capturerecord",
            name="ff_wear",
            field=models.IntegerField(
                blank=True,
                choices=[
                    (0, "0 - None (pale halo)"),
                    (1, "1 - Slight"),
                    (2, "2 - Light (little fraying & few nicks)"),
                    (3, "3 - Moderate (some fraying & chipping)"),
                    (4, "4 - Heavy (worn & frayed, tips worn off)"),
                    (5, "5 - Excessive (ragged, torn, broken rachis)"),
                ],
                null=True,
            ),
        ),
    ]
