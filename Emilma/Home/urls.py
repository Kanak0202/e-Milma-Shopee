from django.contrib import admin
from django.urls import path, include
from Home import views

urlpatterns = [
    path("", views.index, name='Home'),
    path("cafe", views.cafe, name='Cafe'),
    path("checkout", views.checkout, name='Checkout'),
    path("details", views.details, name='Details'),
    path("payment", views.payment, name='Payment'),
    path("processPayment", views.processPayment, name='ProcessPayment'),
    path("orders", views.userOrders, name='UserOrders'),
]