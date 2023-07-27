# Generated by Django 3.1.13 on 2021-10-18 02:47

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ("extras", "0016_secret"),
    ]

    operations = [
        migrations.CreateModel(
            name="JobLogEntry",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True
                    ),
                ),
                ("log_level", models.CharField(default="default", max_length=32)),
                ("grouping", models.CharField(default="main", max_length=100)),
                ("message", models.TextField(blank=True)),
                ("created", models.DateTimeField(default=django.utils.timezone.now)),
                ("log_object", models.CharField(blank=True, max_length=200, null=True)),
                ("absolute_url", models.CharField(blank=True, max_length=255, null=True)),
                ("job_result", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="extras.jobresult")),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
