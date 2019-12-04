from django.urls import path
from .views import *

urlpatterns = [
    path('orders/', orders, name='orders'),
    path('order/<int:pk>/', product_detail, name='product-detail'),
    path('producers/', producers, name='producers'),
    path('producer/<int:pk>', producer_detail, name='producer-detail'),
]