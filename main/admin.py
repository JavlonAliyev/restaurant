from django.contrib import admin

from .models import Restuarant, Menu


@admin.register(Restuarant)
class RestuarantAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'amount_of_tables']


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ['id', 'restuarant', 'name', 'price', 'status']
