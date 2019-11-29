from django.db import models


class Order(models.Model):
    customer = models.ForeignKey('users.Customer', on_delete=models.CASCADE, related_name='Заказчик')
    producer = models.ForeignKey('users.Producer', on_delete=models.CASCADE, related_name='Поставщик')
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE, related_name='Продукт')