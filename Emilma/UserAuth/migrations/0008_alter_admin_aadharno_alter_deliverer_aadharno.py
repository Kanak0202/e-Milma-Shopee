# Generated by Django 5.0.3 on 2024-03-28 18:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("UserAuth", "0007_alter_userprofile_email"),
    ]

    operations = [
        migrations.AlterField(
            model_name="admin",
            name="aadharno",
            field=models.CharField(max_length=200, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name="deliverer",
            name="aadharno",
            field=models.CharField(max_length=200, null=True, unique=True),
        ),
    ]
