from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Product, Producer




def orders(request):
    products = Product.objects.order_by('-create_time')
    product = {'products': products}
    return render(request, 'users/orders.html', product)

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'users/product_detail.html', {'product': product})

def producers(request):
    producers = Producer.objects.order_by('-create_time')
    producer = {'producers': producers}
    return render(request, 'users/producers.html', producer)

def producer_detail(request, pk):
    producer = get_object_or_404(Producer, pk=pk)

    return render(request, 'users/producer_detail.html', {'producer': producer})