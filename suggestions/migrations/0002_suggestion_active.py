# Generated by Django 5.0.3 on 2024-03-21 19:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("suggestions", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="suggestion",
            name="active",
            field=models.BooleanField(default=True),
        ),
    ]
