from django.contrib import admin
from django.urls import path, include
from AdminSide import views

urlpatterns = [
    path("display", views.display, name='display'),
    path("milmaorders", views.milmaOrders, name='milmaorders'),
    path("pastorders", views.pastOrders, name='pastorders'),
    path("updateOrderStatus", views.orderStatusUpdate, name='updateOrderStatus'),
]