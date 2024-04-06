from django.contrib import admin
from .models import Customer, Deliverer, Admin, UserProfile

# Register your models here.
admin.site.register(Customer)
admin.site.register(Admin)
admin.site.register(Deliverer)
admin.site.register(UserProfile)