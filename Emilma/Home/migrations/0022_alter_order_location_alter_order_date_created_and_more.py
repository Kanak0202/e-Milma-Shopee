# Generated by Django 5.0.3 on 2024-03-29 09:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Home", "0021_alter_order_date_created"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="location",
            field=models.CharField(
                choices=[
                    ("OAT", "OAT"),
                    ("Football Ground", "Football Ground"),
                    ("Volleyball Ground", "Volleyball Ground"),
                    ("Admin Block", "Admin Block"),
                    ("New Academic Block Stairs", "New Academic Block Stairs"),
                    ("Manimala Hostel", "Manimala Hostel"),
                    ("Meenachil Hostel", "Meenachil Hostel"),
                    ("Sahayadri Hostel", "Sahayadri Hostel"),
                    ("Girls Hostel", "Girls Hostel"),
                ],
                max_length=200,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="order",
            name="date_created",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 3, 29, 9, 23, 55, 713463, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.DeleteModel(
            name="Cluster",
        ),
        migrations.DeleteModel(
            name="Location",
        ),
    ]
