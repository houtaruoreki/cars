# Generated by Django 5.0.3 on 2024-04-15 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Car",
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
                ("model", models.CharField(max_length=50)),
                ("brand", models.CharField(max_length=50)),
                ("year", models.IntegerField()),
                ("engine", models.CharField(max_length=50)),
                ("color", models.CharField(max_length=50)),
            ],
        ),
    ]
