from typing import OrderedDict
from django.contrib import admin
from .models import Cupon, Order

# Register your models here.
@admin.register(Cupon)
class CuponAdmin(admin.ModelAdmin):
    # list_display = ['__all__']
    ordering = ['id']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    ordering = ['id']