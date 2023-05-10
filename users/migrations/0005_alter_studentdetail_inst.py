# Generated by Django 4.1.4 on 2022-12-10 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0004_studentdetail_inst_alter_studentdetail_course"),
    ]

    operations = [
        migrations.AlterField(
            model_name="studentdetail",
            name="inst",
            field=models.CharField(
                choices=[
                    ("tkm", "TKM College of Engineering"),
                    ("cet", "College of Engineering Trivandrum"),
                    ("gect", "GEC Thrissur"),
                    ("geck", "GEC Kannur"),
                    ("rgr", "Rajagiri School of Engineering and Technology"),
                    ("gecbrt", "Government Engineering College, Barton Hill"),
                    ("mace", "MACE Kothamangalam"),
                ],
                default="tkm",
                max_length=200,
            ),
        ),
    ]