# Generated by Django 5.0.3 on 2024-03-29 08:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Home", "0020_alter_order_date_created_alter_order_location"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="date_created",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 3, 29, 8, 32, 4, 815402, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]