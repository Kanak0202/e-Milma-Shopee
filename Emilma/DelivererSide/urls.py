from django.contrib import admin
from django.urls import path, include
from DelivererSide import views

urlpatterns = [
    path("currentOrders", views.currentOrders, name='currentOrders'),
    path("pastOrders", views.pastOrders, name='pastOrders'),
]