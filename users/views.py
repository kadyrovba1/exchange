from django.http import HttpResponse
from django.shortcuts import render
from .models import Product



def orders(request):
    products = Product.objects.order_by('-create_time')[:3]
    product = {'products': products}
    return render(request, 'users/orders.html', product)

