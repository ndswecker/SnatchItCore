# Generated by Django 5.0.3 on 2024-03-25 02:53

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("maps", "0005_alter_capturerecord_net"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="capturerecord",
            name="date_time",
        ),
        migrations.AddField(
            model_name="capturerecord",
            name="capture_time",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name="capturerecord",
            name="release_time",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
