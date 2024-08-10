from django.shortcuts import render
from Home.models import Order
from django.http import JsonResponse
import json

# Create your views here.
def currentOrders(request):
    user_profile = request.user.userprofile
    deliverer = user_profile.deliverer
    orders = Order.objects.filter(deliverer=deliverer, status__in=['Assigned Deliverer', 'Out for delivery'])
    context = {
        'orders':orders
    }
    return render(request, 'delivererHomePage.html', context)

def pastOrders(request):
    user_profile = request.user.userprofile
    deliverer = user_profile.deliverer
    orders = Order.objects.filter(deliverer=deliverer, status__in=['Delivered'])
    context = {
        'orders':orders
    }
    return render(request, 'delivererPastOrders.html', context)


