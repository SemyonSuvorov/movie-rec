# Generated by Django 5.0.3 on 2024-03-17 19:11

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Movie",
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
                ("title", models.CharField(max_length=120, unique=True)),
                ("overview", models.TextField()),
                ("release_date", models.DateField(blank=True, null=True)),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
