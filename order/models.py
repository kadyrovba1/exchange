from django.db import models
from users.models import Customer, Producer
from product.models import Product



class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)