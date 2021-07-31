from django.contrib import admin
from .models import Curso, Unidad, Leccion, Horario, Beneficio

# Register your models here.
@admin.register(Curso)
class UserAdmin(admin.ModelAdmin):
    # list_display = ['__all__']
    ordering = ['id']

@admin.register(Unidad)
class UserAdmin(admin.ModelAdmin):
    # list_display = ['__all__']
    ordering = ['id']

@admin.register(Leccion)
class UserAdmin(admin.ModelAdmin):
    # list_display = ['__all__']
    ordering = ['id']

@admin.register(Horario)
class UserAdmin(admin.ModelAdmin):
    # list_display = ['__all__']
    ordering = ['id']

@admin.register(Beneficio)
class BeneficioAdmin(admin.ModelAdmin):
    # list_display = ['__all__']
    ordering = ['id']