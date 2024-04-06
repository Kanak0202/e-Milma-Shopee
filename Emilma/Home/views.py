from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
import json
# Create your views here.
from django.shortcuts import render
from .models import Product, Order
from math import ceil
from django.contrib.auth.decorators import login_required
from UserAuth.decorators import unauthenticated_user, allowed_users
from django.contrib.auth.models import User
from UserAuth.models import Customer, UserProfile
from datetime import datetime
from django.utils import timezone
import pytz

def index(request):
    products = Product.objects.exclude(category='Fast Food')

    allProds = []
    catprods = products.values('subcategory', 'product_id')
    cats = {item['subcategory'] for item in catprods}
    catsCount = len(cats)
    
    for cat in cats:
        prod = products.filter(subcategory=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) + (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])
    
    params = {'allProds':allProds, 'sections':catsCount}
    return render(request, 'index.html', params)

@login_required(login_url='login')
def cafe(request):
    products = Product.objects.filter(category='Fast Food')

    allProds = []
    catprods = products.values('subcategory', 'product_id')
    cats = {item['subcategory'] for item in catprods}
    catsCount = len(cats)
    
    for cat in cats:
        prod = products.filter(subcategory=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) + (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])
    
    params = {'allProds':allProds, 'sections':catsCount}
    return render(request, 'cafe.html', params)


@allowed_users(allowed_roles=['customer']) # decorator
def checkout(request):
    return render(request, 'checkout.html')

@allowed_users(allowed_roles=['customer']) # decorator
def details(request):
    return render(request, 'deliveryDetails.html', {'user': request.user})

@allowed_users(allowed_roles=['customer']) # decorator
def payment(request):
    return render(request, 'paymentGateway.html')

def processPayment(request):
    if request.method == "POST":
        # Get the JSON data from the request body
        data = json.loads(request.body)
        customer_username = data.get("customer")
        items_json = json.dumps(data.get("items_json"))
        items_jsonopt = data.get("items_json")
        status = "Pending"
        location = data.get("location")
        amount = data.get("amount")
        print(items_json)

        # Get the customer instance corresponding to the provided username
        try:
    # Retrieve the UserProfile instance using the username
            user_profile = UserProfile.objects.get(user__username=customer_username)
    # Retrieve the Customer instance using the UserProfile
            customer = Customer.objects.get(user_profile=user_profile)
        except UserProfile.DoesNotExist:
            return JsonResponse({'error': 'User profile not found'}, status=400)
        except Customer.DoesNotExist:
            return JsonResponse({'error': 'Customer not found'}, status=400)
        ist_time = timezone.localtime(timezone.now(), pytz.timezone('Asia/Kolkata'))
        # Create and save the order object
        order = Order.objects.create(
            customer=customer,
            items_json=items_json,
            status=status,
            location=location,
            amount=amount,
            date_created=ist_time
        )
        for item in items_jsonopt:
            product_id = item  # Assuming product_id is provided in the items_json
            try:
                product = Product.objects.get(pk=product_id)
                order.products.add(product)
            except Product.DoesNotExist:
                # Handle case where product with given ID doesn't exist
                pass

        # Return a JSON response indicating success
        return JsonResponse({'message': 'Order placed successfully'})

    # Return a JSON response if request method is not POST
    return JsonResponse({'error': 'Invalid request method'})

def userOrders(request):
    user_profile = request.user.userprofile
    customer = user_profile.customer  # Assuming UserProfile has a ForeignKey to Customer

    # Filter orders based on the current customer
    workingOrders = Order.objects.filter(customer=customer, status__in=['Pending', 'Packing', 'Assigned Deliverer', 'Out for delivery'])
    completedOrders = Order.objects.filter(customer=customer, status='Delivered')
    # Check if there are any elements in the lists before accessing them
    working_order_count = workingOrders.count()
    completed_order_count = completedOrders.count()

    context = {
        'workingOrders': workingOrders,
        'completedOrders': completedOrders
    }
    return render(request, 'userOrders.html', context)
# def about(request):
#     return render(request, 'about.html')
    # return HttpResponse("This is the about page")
