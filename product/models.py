from django.db import models


class Product(models.Model):
    producer = models.ForeignKey('users.Producer', on_delete=models.CASCADE, related_name='Producer name')
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    create_time = models.DateTimeField(auto_now_add=True)