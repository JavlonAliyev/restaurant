from django.db import models

from main.models import Restuarant


class Order(models.Model):
    restuarant = models.ForeignKey(Restuarant, on_delete=models.RESTRICT)
    number_of_tables = models.IntegerField()
    total_price = models.IntegerField()

    date = models.DateField()


class OrderMenu(models.Model):
    order = models.ForeignKey(Order, on_delete=models.RESTRICT)
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    amount = models.IntegerField()

