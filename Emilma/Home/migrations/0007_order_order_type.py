# Generated by Django 5.0.3 on 2024-03-17 12:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Home", "0006_order_amount_order_customer_order_items_json_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="order_type",
            field=models.CharField(
                choices=[("Retail", "Retail"), ("Fast Food", "Fast Food")],
                max_length=200,
                null=True,
            ),
        ),
    ]