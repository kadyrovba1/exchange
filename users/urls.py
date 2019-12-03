from django.urls import path
from .views import orders, product_detail

urlpatterns = [
    path('orders/', orders, name='orders'),
    path('order/<int:pk>/', product_detail, name='product-detail'),
]