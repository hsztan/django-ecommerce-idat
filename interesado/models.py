from django.db import models
from curso.models import Curso
from django.core.validators import validate_email

# Create your models here.
class Interesado(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=150, null=False, blank=False)
    celular = models.CharField(max_length=30, null=False, blank=False)
    correo = models.EmailField(null=False, blank=False, validators=[validate_email], unique=True)
    curso = models.ForeignKey(Curso, null=True, on_delete=models.SET_NULL)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'interesado'
        ordering = ['-updated_at']
        verbose_name = 'Interesado'
        verbose_name_plural = 'Interesados'

    def __str__(self):
        return self.nombre