# Generated by Django 4.1.4 on 2022-12-09 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("events", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="competition",
            name="brochure",
            field=models.FileField(blank=True, upload_to="competition/brochure"),
        ),
        migrations.AlterField(
            model_name="competition",
            name="logo",
            field=models.ImageField(blank=True, upload_to="competition/logo"),
        ),
    ]
