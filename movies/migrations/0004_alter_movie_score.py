# Generated by Django 5.0.3 on 2024-03-21 15:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("movies", "0003_movie_score"),
    ]

    operations = [
        migrations.AlterField(
            model_name="movie",
            name="score",
            field=models.FloatField(blank=True, null=True),
        ),
    ]
