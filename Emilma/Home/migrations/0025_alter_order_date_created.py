# Generated by Django 5.0.3 on 2024-03-29 13:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Home", "0024_alter_order_date_created"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="date_created",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 3, 29, 13, 36, 8, 819405, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
