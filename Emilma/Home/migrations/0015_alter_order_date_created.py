# Generated by Django 5.0.3 on 2024-03-28 17:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Home", "0014_order_products_alter_order_date_created"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="date_created",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 3, 28, 17, 3, 50, 32356, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
