import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="BreedingRecord",
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
                    "uuid",
                    models.UUIDField(
                        db_index=True, default=uuid.uuid4, editable=False, unique=True
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("date", models.DateField()),
                ("hawo", models.CharField(max_length=100, verbose_name="HAWO")),
                ("acfl", models.CharField(max_length=100, verbose_name="ACFL")),
                ("ytvi", models.CharField(max_length=100, verbose_name="YTVI")),
                ("revi", models.CharField(max_length=100, verbose_name="REVI")),
                ("tres", models.CharField(max_length=100, verbose_name="TRES")),
                ("cach", models.CharField(max_length=100, verbose_name="CACH")),
                ("woth", models.CharField(max_length=100, verbose_name="WOTH")),
                ("gcth", models.CharField(max_length=100, verbose_name="GCTH")),
                ("amro", models.CharField(max_length=100, verbose_name="AMRO")),
                ("grca", models.CharField(max_length=100, verbose_name="GRCA")),
                ("nopa", models.CharField(max_length=100, verbose_name="NOPA")),
                ("ywar", models.CharField(max_length=100, verbose_name="YWAR")),
                ("amre", models.CharField(max_length=100, verbose_name="AMRE")),
                ("initials", models.CharField(max_length=100)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
