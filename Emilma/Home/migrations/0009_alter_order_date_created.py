# Generated by Django 5.0.3 on 2024-03-28 04:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Home", "0008_remove_order_order_type_alter_order_location_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="date_created",
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]