# Generated by Django 5.0.3 on 2024-03-28 05:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Home", "0011_alter_order_date_created"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="order",
            name="items_json",
        ),
        migrations.AddField(
            model_name="order",
            name="products",
            field=models.ManyToManyField(to="Home.product"),
        ),
        migrations.AlterField(
            model_name="order",
            name="date_created",
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
