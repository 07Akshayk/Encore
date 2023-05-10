# Generated by Django 4.1.4 on 2022-12-10 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("events", "0004_certificate_point"),
    ]

    operations = [
        migrations.AddField(
            model_name="certificate",
            name="category",
            field=models.CharField(
                choices=[
                    ("Worshop", "Worshop"),
                    ("Lecture", "Lecture"),
                    ("Competition", "Competition"),
                ],
                default="Competition",
                max_length=50,
            ),
        ),
    ]
