from django.shortcuts import render
from Home.models import Product, Order
from UserAuth.models import Deliverer
from datetime import date
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.contrib.auth.decorators import login_required
from UserAuth.decorators import allowed_users, admin_only, unauthenticated_user
from django.http import JsonResponse
import json


# Create your views here.
@login_required(login_url='login')
@admin_only
def display(request):
    if request.method == "POST":
        # Retrieve form data from the POST request
        product_name = request.POST.get('productname', '')
        category = request.POST.get('category', '')
        subcategory = request.POST.get('subcategory', '')
        price = request.POST.get('price', '')
        description = request.POST.get('description', '')
        stock = request.POST.get('stock', '')
        # Handle the uploaded image
        image = request.FILES.get('image', '')

        # Check if a product with the same name, description, and price already exists
        existing_product = Product.objects.filter(product_name=product_name, description=description, price=price).exists()
        if existing_product:
            params={
                'existing':True,
            }
            return render(request, 'displayProducts.html', params)
        if not existing_product:
            # Create a new Product object with the retrieved data
            new_product = Product(
                product_name=product_name,
                category=category,
                subcategory=subcategory,
                price=price,
                stock=stock,
                description=description,
                pub_date=date.today(),
                image=image
            )

            # Save the new product to the database
            new_product.save()

    # Retrieve all Product objects from the database
    products = Product.objects.all()
    num_prods = products.count()  # Count the number of Product objects

    # Render the template with the products count
    params = {'products': products}
    return render(request, 'displayProducts.html', params)

@admin_only
def milmaOrders(request):
    deliverers = Deliverer.objects.all()
    # Extract users associated with deliverers
    deliverer_users = [deliverer.user_profile.user for deliverer in deliverers]
   
    workingOrders = Order.objects.filter(status__in=['Pending', 'Packing', 'Assigned Deliverer', 'Out for delivery'])

    context = {
        'workingOrders':workingOrders,
        'deliverers':deliverer_users
    }
    return render(request, 'milmaOrders.html', context)

@admin_only
def pastOrders(request):
    completedOrders = Order.objects.filter(status='Delivered')
    context = {
        'completedOrders':completedOrders
    }
    return render(request, 'pastOrders.html', context)

def orderStatusUpdate(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        order_id = data.get('orderId')
        try:
            order = Order.objects.get(id=order_id)
            order.transition_to_next_state(data)
            return JsonResponse({'success': True})
        except Order.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Order not found'})
    return JsonResponse({'success': False, 'error': 'Invalid request method'})


