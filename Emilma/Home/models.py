from django.db import models
from UserAuth.models import Customer, Deliverer
from datetime import datetime
from django.utils import timezone
import pytz

# Create your models here.
def product_image_upload(instance, filename):
    return f'E:/Web-D projects/e-Milma Shopee/Emilma/static/Products/Images/{filename}'
class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length = 50)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    price=models.IntegerField(default=0)
    description = models.CharField(max_length=300)
    stock = models.IntegerField(default=0)
    pub_date = models.DateField()
    image = models.ImageField(upload_to=product_image_upload, default=0)
    def __str__(self):
        return self.product_name
    
class OrderState:
    def transition_to_next_state(self, order, data):
        order.status = data['status']
        order.save()
        # raise NotImplementedError("Subclasses must implement transition_to_next_state method")

class PendingState(OrderState):
    pass

class PackingState(OrderState):
    def transition_to_next_state(self, order, data):
        order.status = data['status']
        deliveryPartner = data["deliverer"]
        deliverer = Deliverer.objects.get(user_profile__user__username=deliveryPartner)
        print(deliverer)
        order.deliverer = deliverer
        order.save()

class AssignedDelivererState(OrderState):
    pass

class OutForDeliveryState(OrderState):
    pass   

class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Packing', 'Packing'),
        ('Assigned Deliverer', 'Assigned Deliverer'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered')
    )
    LOCATION = (
        ('OAT', 'OAT'),
        ('Football Ground', 'Football Ground'),
        ('Volleyball Ground', 'Volleyball Ground'),
        ('Admin Block', 'Admin Block'),
        ('New Academic Block Stairs', 'New Academic Block Stairs'),
        ('Manimala Hostel', 'Manimala Hostel'),
        ('Meenachil Hostel', 'Meenachil Hostel'),
        ('Sahayadri Hostel', 'Sahayadri Hostel'),
        ('Girls Hostel', 'Girls Hostel'),
    )
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    items_json =  models.CharField(max_length=5000, null=True) 
    products = models.ManyToManyField(Product)
    date_created = models.DateTimeField(default=timezone.localtime(timezone.now(), timezone=pytz.timezone('Asia/Kolkata')))
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    location = models.CharField(max_length=200, null=True, choices=LOCATION)
    amount = models.IntegerField(default=0)
    deliverer = models.ForeignKey(Deliverer,  null=True, on_delete=models.SET_NULL, blank=True)
    razorpay_id = models.CharField(max_length=100, blank=True)
    paid = models.BooleanField(default=False)

    def transition_to_next_state(self, data):
        # print(data)
        # print(self)
        print("Inside transition function")
        current_state = self.get_current_state()
        print(current_state)
        if current_state:
            current_state.transition_to_next_state(self, data)

    # Method to retrieve the current state object
    def get_current_state(self):
        print("Inside current state function")
        print("Current status: ", self.status)
        if self.status == 'Pending':
            print("Inside get current pending")
            return PendingState()
        elif self.status == 'Packing':
            return PackingState()
        elif self.status == 'Assigned Deliverer':
            return AssignedDelivererState()
        elif self.status == 'Out for delivery':
            return OutForDeliveryState()
    
class Cart(models.Model):
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    items_json =  models.CharField(max_length=5000, null=True) 
    isActive = models.BooleanField(default=False)

    @classmethod
    def get_cart(cls, customer):
        """
        Retrieve or create the cart for the specified customer.
        """
        cart, created = cls.objects.get_or_create(customer=customer)
        return cart

    def clear_cart(self):
        """
        Clear the cart by emptying the items.
        """
        self.items_json = None
        self.save()

    def complete_order(self):
        """
        Mark the cart as inactive when the order is completed.
        """
        self.is_active = False
        self.save()
