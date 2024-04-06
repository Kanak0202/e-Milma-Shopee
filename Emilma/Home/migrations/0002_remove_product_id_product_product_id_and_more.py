# Generated by Django 5.0.3 on 2024-03-09 18:05

import Home.models
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Home", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="id",
        ),
        migrations.AddField(
            model_name="product",
            name="product_id",
            field=models.AutoField(default=0, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="product",
            name="image",
            field=models.ImageField(
                default=0, upload_to=Home.models.product_image_upload
            ),
        ),
    ]