from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True, unique=True)
    phoneno = models.CharField(max_length=10, null=True, unique=True)
    role = models.CharField(max_length=10, null=True)
    def __str__(self):
        return self.user.username

class Customer(models.Model):
    user_profile = models.OneToOneField(UserProfile, null=True, on_delete=models.CASCADE)
    HOSTELS = (
        ('Manimala', 'Manimala'),
        ('Meenachil', 'Meenachil'),
        ('Sahayadri', 'Sahayadri'),
        ('Girls Hostel', 'Girls Hostel'),
        ('Outside', 'Outside')
    )
    rollno = models.CharField(max_length=200, null=True, unique=True)
    hostel = models.CharField(max_length=200, null=True, choices=HOSTELS)
    roomno = models.IntegerField(default=0)

class Admin(models.Model):
    user_profile = models.OneToOneField(UserProfile, null=True, on_delete=models.CASCADE)
    # Add any additional fields specific to Admin here
    address = models.CharField(max_length=200, null=True)
    aadharno = models.CharField(max_length=200, null=True, unique=True)

class Deliverer(models.Model):
    user_profile = models.OneToOneField(UserProfile, null=True, on_delete=models.CASCADE)
    # Add any additional fields specific to Deliverer here
    address = models.CharField(max_length=200, null=True)
    aadharno = models.CharField(max_length=200, null=True, unique=True)
