from django.db import models
from django.contrib.auth.models import AbstractUser

class Producer(AbstractUser):
    phone_number = models.CharField(max_length=12, verbose_name='Номер телефона')
    email = models.EmailField(verbose_name='email', unique=True)
    company = models.CharField(max_length=20, verbose_name='Название поставщика')
    address = models.CharField(max_length=255, verbose_name='Адрес поставщика')

    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'


class Customer(AbstractUser):
    phone_number = models.CharField(max_length=12, verbose_name='Номер телефона')
    email = models.EmailField(verbose_name='email', unique=True)
    first_name = models.CharField(max_length=50, verbose_name='Имя заказчика')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия заказчика')

    class Meta:
        verbose_name = 'Заказчик'
        verbose_name_plural = 'Заказчики'