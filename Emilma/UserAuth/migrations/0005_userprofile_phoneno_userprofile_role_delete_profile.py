# Generated by Django 5.0.3 on 2024-03-26 05:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "UserAuth",
            "0004_remove_customer_date_created_remove_customer_email_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="userprofile",
            name="phoneno",
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name="userprofile",
            name="role",
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.DeleteModel(
            name="Profile",
        ),
    ]
