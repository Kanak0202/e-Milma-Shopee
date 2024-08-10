from django.shortcuts import render, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
# from .forms import CreateUserForm
from django.contrib.auth import authenticate,login, logout
from django.contrib import messages
from .decorators import unauthenticated_user, allowed_users
from django.contrib.auth.models import Group
from .factory import UserFactory
from .models import UserProfile
from .models import Customer
import json
from django.http import JsonResponse
from django.contrib.auth.models import User
import re
from abc import ABC, abstractmethod

# Create your views here.
@unauthenticated_user
def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            user_profile = UserProfile.objects.get(user=user)
            role = user_profile.role
            login(request, user)
            if role == 'customer':
                return redirect('/')
            elif role == 'admin':
                return redirect('adminside/milmaorders')
            elif role == 'deliverer':
                #Will be redirected to deliverer page
                return redirect('/delivererSide/currentOrders')
            else:
                return redirect('/')
        else:
            messages.error(request, 'Invalid username or password')
            return render(request, 'login.html')
    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect('/login')


def build_validation_chain(user_data):
    username_handler = UsernameValidationHandler()
    email_handler = EmailValidationHandler(username_handler)
    return email_handler.handle_request(user_data)

# Modify the BaseHandler class to accept user data
class BaseHandler:
    def __init__(self, successor=None):
        self.successor = successor
    
    @abstractmethod
    def handle_request(self, user_data):
        if self.successor:
            return self.successor.handle_request(user_data)
        else:
            return 

class UsernameValidationHandler(BaseHandler):
    def handle_request(self, user_data):
        username = user_data.get('username')
        # Perform username validation logic
        if not username:
            return 'Username is required.'
        elif len(username) < 5:
            return 'Username must be at least 5 characters long.'
        elif User.objects.filter(username=username).exists():
            return 'Username is already taken.'
        else:
            # If validation succeeds, pass the request to the next handler
            if self.successor:
                return self.successor.handle_request(user_data)
            else:
                return None
            
class EmailValidationHandler(BaseHandler):
    def handle_request(self, user_data):
        email = user_data.get('email')
        # Perform email validation logic
        if not email:
            return 'Email is required.'
        elif not self.email_valid(email):
            return 'Invalid email format.'
        elif User.objects.filter(email=email).exists():
            return 'Email is already registered.'
        else:
            # If validation succeeds, pass the request to the next handler
            if self.successor:
                return self.successor.handle_request(user_data)
            else:
                return None
            
    def email_valid(self, email):
        # Regular expression to validate email format
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return re.match(pattern, email)

class PasswordValidationHandler(BaseHandler):
    def __init__(self, next_handler=None):
        self.next_handler = next_handler

    def handle_request(self, user_data):
        if user_data['password1'] != user_data['password2']:
            return "Passwords do not match"
        if self.is_valid_password(user_data['password1']):
            if self.next_handler:
                return self.next_handler.handle_request(user_data)
            else:
                return None  # Password meets all criteria
        else:
            return "Password must contain a lowercase letter, an uppercase letter, a special character, a number, and be at least 8 characters long."

    def is_valid_password(self, password):
        # Password must contain at least one lowercase letter
        if not any(char.islower() for char in password):
            return False
        # Password must contain at least one uppercase letter
        if not any(char.isupper() for char in password):
            return False
        # Password must contain at least one special character
        if not any(char in '!@#$%^&*()-_+=[]{}|:;"\'<>,.?/~`' for char in password):
            return False
        # Password must contain at least one digit
        if not any(char.isdigit() for char in password):
            return False
        # Password must be at least 8 characters long
        if len(password) < 8:
            return False
        return True
    
class PhoneNumberValidationHandler(BaseHandler):
    def __init__(self, next_handler=None):
        self.next_handler = next_handler

    def handle_request(self, user_data):
        validation_result = self.is_valid_phone_number(user_data['phoneno'])
        if validation_result is True:
            if self.next_handler:
                return self.next_handler.handle_request(user_data)
            else:
                return None  # Phone number meets all criteria
        else:
            return validation_result 

    def is_valid_phone_number(self, phone_number):
        # Phone number must start with a digit between 6 and 9 and be of length 10
        if not re.match(r'^[6-9]\d{9}$', phone_number):
            return "Invalid Phone Number"
        # Phone number must be unique
        if UserProfile.objects.filter(phoneno=phone_number).exists():
            return "Account with this phone number already exists"
        return True
    
class RollNumberValidationHandler:
    def __init__(self, next_handler=None):
        self.next_handler = next_handler

    def handle_request(self, user_data):
        role = user_data['role']
        rollno = user_data['rollno']
        if role == "customer":
            if self.is_valid_roll_number(user_data['rollno']):
                if self.next_handler:
                    return self.next_handler.handle_request(user_data)
                else:
                    return None  # Role number meets all criteria
            else:
                return "Account with this roll number already exists"
        else:
            return None

    def is_valid_roll_number(self, rollno):
        # Phone number must be unique
        if Customer.objects.filter(rollno=rollno).exists():
            return False
        return True

rollNumberHandlerObject = RollNumberValidationHandler(None)
phoneNumberHandlerObject = PhoneNumberValidationHandler(rollNumberHandlerObject)
passwordHandlerObject = PasswordValidationHandler(phoneNumberHandlerObject)
emailHandlerObject = EmailValidationHandler(passwordHandlerObject)
usernameHandler = UsernameValidationHandler(emailHandlerObject)

            
def register(request):
    if request.method == 'POST':
        user_data = request.POST.dict()
        error_message = usernameHandler.handle_request(user_data)
        if error_message:
            messages.error(request, error_message)
            return redirect('register')
        else:
            factory = UserFactory.get_factory(user_data["role"])
            if factory:
                user = factory.create_user(user_data)
                if user:
                    group_name = user_data["role"]
                    group, created = Group.objects.get_or_create(name=group_name)
                    group.user_set.add(user.user_profile.user)
                    messages.success(request, 'Account created successfully')
                    return redirect('login')
                else:
                    messages.error(request, 'Failed to create user')
            else:
                messages.error(request, 'Invalid User Role')
            return redirect('register')
    else:
        pass
    return render(request, 'register.html')


