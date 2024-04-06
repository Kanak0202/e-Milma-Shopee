from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Customer, Admin, Deliverer

# class CreateUserForm(UserCreationForm):
#     class Meta:
#         model= User
#         fields = ['username', 'email', 'password1', 'password2']

class CustomerForm(UserCreationForm):
    class Meta:
        model = Customer
        fields = ['name', 'email', 'password1', 'password2', 'phoneno', 'hostel', 'roomno']

class AdminForm(UserCreationForm):
    class Meta:
        model = Admin
        fields = ['name', 'email', 'password1', 'password2', 'phoneno', 'address', 'aadharno']

class DelivererForm(UserCreationForm):
    class Meta:
        model = Deliverer
        fields = ['name', 'email', 'password1', 'password2', 'phoneno', 'address', 'aadharno']
