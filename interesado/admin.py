from django.contrib import admin
from .models import Interesado

# Register your models here.
@admin.register(Interesado)
class UserAdmin(admin.ModelAdmin):
    ordering = ['id']