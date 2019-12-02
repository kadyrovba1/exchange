from django.urls import path
from .views import orders

urlpatterns = [
    #path('', index),
    path('orders/', orders, name='orders'),
]