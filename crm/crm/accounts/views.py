from django.shortcuts import render
from django.http import HttpResponse

from accounts.models import Customer, Order, Product
# Create your views here.


def home(request):
    total_orders = Order.objects.all()
    orders = total_orders
    customers = Customer.objects.all()
    total_customer = customers.count()
    total_order = total_orders.count()
    delivered = total_orders.filter(status='Delivered').count()
    pending = total_orders.filter(status='Pending').count()

    context = {
        'orders': orders,
        'customers': customers,
        'total_customer': total_customer,
        'total_orders': total_order,
        'delivered': delivered,
        'pending': pending
    }

    return render(request=request, template_name='accounts/dashboard.html', context=context)


def products(request):
    products = Product.objects.all()

    return render(request=request, template_name='accounts/products.html', context={'products': products})


def customer(request):
    return render(request=request, template_name='accounts/customer.html')
