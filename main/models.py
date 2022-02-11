from django.db import models


class Restuarant(models.Model):
    name = models.CharField(max_length=50)
    amount_of_tables = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Menu(models.Model):
    STATUS_YES = 1
    STATUS_NO = 0

    restuarant = models.ForeignKey(Restuarant, on_delete=models.RESTRICT)
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    status = models.SmallIntegerField(choices=(
        (STATUS_YES, "Bor"),
        (STATUS_NO, "Yo'q")
    ), default=0)


