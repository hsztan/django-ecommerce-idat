from django.db import models
from django.db.models.fields import AutoField, CharField, DecimalField
from django.db.models.fields.related import ForeignKey, ManyToManyField
from authentication.models import User
from curso.models import Curso

# Create your models here.

class Cupon(models.Model):
    id = AutoField(primary_key=True)
    precio = DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    porcentaje = DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'cupon'
        verbose_name = 'Cupon'
        verbose_name_plural = 'Cupones'
    

class Order(models.Model):
    id = AutoField(primary_key=True)
    code = CharField(max_length=30)
    user = ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    cursos = ManyToManyField(Curso)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'order'
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
    
    def __str__(self):
        return f'{self.user}'