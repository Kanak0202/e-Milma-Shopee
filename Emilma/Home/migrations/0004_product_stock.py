# Generated by Django 5.0.3 on 2024-03-17 09:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Home", "0003_alter_product_product_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="stock",
            field=models.IntegerField(default=0),
        ),
    ]
