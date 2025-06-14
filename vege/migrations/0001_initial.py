# Generated by Django 5.2.1 on 2025-06-03 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="recipe",
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
                ("recipe_name", models.CharField()),
                ("recipe_description", models.TextField()),
                ("recipe_image", models.ImageField(upload_to="recipe")),
            ],
        ),
    ]
