from django.db import models


class Producer(models.Model):
    company = models.CharField(max_length=20, verbose_name='Название поставщика')
    phone_number = models.CharField(max_length=12, verbose_name='Номер телефона')
    email = models.EmailField(verbose_name='email', unique=True)
    address = models.CharField(max_length=255, verbose_name='Адрес поставщика')
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'

    def __str__(self):
        return self.company


class Customer(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='Имя заказчика')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия заказчика')
    phone_number = models.CharField(max_length=12, verbose_name='Номер телефона')
    email = models.EmailField(verbose_name='email', unique=True)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Заказчик'
        verbose_name_plural = 'Заказчики'

    def __str__(self):
        return self.first_name


class Product(models.Model):
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE, verbose_name='Поставщик', related_name='name_producer')
    name = models.CharField(max_length=50, verbose_name='Название товара')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name='Заказчик', related_name='orderer')
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE, verbose_name='Поставщик')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар', related_name='product_name')
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


