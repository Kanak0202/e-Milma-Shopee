from django.contrib.auth.models import User
from .models import Customer, Admin, Deliverer, UserProfile

class UserFactory:
    @staticmethod
    def create_user(user_data):
        pass
    @staticmethod
    def get_factory(role):
        if role == 'customer':
            return CustomerFactory()
        elif role == 'admin':
            return AdminFactory()
        elif role == 'deliverer':
            return DelivererFactory()
        else:
            return None

class CustomerFactory(UserFactory):
    @staticmethod
    def create_user(user_data):
        user = User.objects.create_user(username=user_data['username'], first_name=user_data['firstname'],  last_name=user_data['lastname'], email=user_data['email'], password=user_data['password1'])
        user_profile = UserProfile.objects.create(user=user, name=user_data['username'], email=user_data['email'], role=user_data['role'], phoneno = user_data['phoneno'])
        customer = Customer.objects.create(
            user_profile=user_profile,
            rollno=user_data['rollno'],
            hostel=user_data['hostel'],
            roomno=user_data['roomno']
        )
        return customer

class AdminFactory(UserFactory):
    @staticmethod
    def create_user(user_data):
        user = User.objects.create_user(username=user_data['username'], email=user_data['email'], password=user_data['password1'])
        user_profile = UserProfile.objects.create(user=user, name=user_data['username'], email=user_data['email'], role=user_data['role'], phoneno = user_data['phoneno'])
        admin = Admin.objects.create(
            user_profile=user_profile,
            address=user_data['address'],
            aadharno=user_data['aadharno']
        )
        return admin

class DelivererFactory(UserFactory):
    @staticmethod
    def create_user(user_data):
        user = User.objects.create_user(username=user_data['username'], email=user_data['email'], password=user_data['password1'])
        user_profile = UserProfile.objects.create(user=user, name=user_data['username'], email=user_data['email'], role=user_data['role'], phoneno = user_data['phoneno'])
        deliverer = Deliverer.objects.create(
            user_profile=user_profile,
            address=user_data['address'],
            aadharno=user_data['aadharno']
        )
        return deliverer


