from django.shortcuts import render, redirect
from django.http import HttpResponse

from accounts.models import Customer, Order, Product
from accounts.form import OrderForm
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


def customer(request, pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()
    order_count = orders.count()
    context = {
        'customer': customer,
        'orders': orders,
        'order_count': order_count
    }
    return render(request=request, template_name='accounts/customer.html', context=context)


def createOrder(request):
    form = OrderForm()
    if request.method == 'POST':
        #print('Printing POST:', request.POST)
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'accounts/order_form.html', context)


def updateOrder(request, pk):

    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)

    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'accounts/order_form.html', context)


def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == "POST":
        order.delete()
        return redirect('/')

    context = {'item': order}
    return render(request, 'accounts/delete.html', context)
