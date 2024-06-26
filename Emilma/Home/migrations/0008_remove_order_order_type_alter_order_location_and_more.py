# Generated by Django 5.0.3 on 2024-03-28 04:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Home", "0007_order_order_type"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="order",
            name="order_type",
        ),
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
            name="status",
            field=models.CharField(
                choices=[
                    ("Pending", "Pending"),
                    ("Packing", "Packing"),
                    ("Out for delivery", "Out for delivery"),
                    ("Delivered", "Delivered"),
                ],
                max_length=200,
                null=True,
            ),
        ),
    ]
