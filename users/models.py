from django.db import models


class CommonInfo(models.Model):
    create_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Producer(CommonInfo):
    phone_number = models.CharField(max_length=12, verbose_name='Номер телефона')
    e_mail = models.EmailField(verbose_name='email', unique=True)
    name = models.CharField(max_length=20, verbose_name='Название поставщика')
    address = models.CharField(max_length=255, verbose_name='Адрес поставщика')


class Customer(CommonInfo):
    phone_number = models.CharField(max_length=12, verbose_name='Номер телефона')
    e_mail = models.EmailField(verbose_name='email', unique=True)
    first_name = models.CharField(max_length=50, verbose_name='Имя заказчика')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия заказчика')


class Product(CommonInfo):
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=50)


class Order(CommonInfo):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)