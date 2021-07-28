from django import db
from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL
from authentication.models import User

# Create your models here.

class Leccion(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=150)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'leccion'
        ordering = ['-updated_at']
        verbose_name = 'Leccion'
        verbose_name_plural = 'Lecciones'

    def __str__(self):
        return self.nombre


class Unidad(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=150)
    lecciones = models.ManyToManyField(Leccion)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'unidad'
        ordering = ['-updated_at']
        verbose_name = 'Unidad'
        verbose_name_plural = 'Unidades'

    def __str__(self):
        return self.nombre

class Horario(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.CharField(max_length=150)
    frecuencia = models.CharField(max_length=150)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'horario'
        ordering = ['-updated_at']
        verbose_name = 'Horario'
        verbose_name_plural = 'Horarios'

    def __str__(self):
        return self.fecha


class Curso(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=150)
    sub_titulo = models.CharField(max_length=250, null=True, blank=True)
    resumen_corto = models.TextField(null=True, blank=True)
    resumen_largo = models.TextField(null=True, blank=True)
    duracion = models.CharField(max_length=150)
    image_thumb = models.URLField(null=True, blank=True)
    image = models.URLField(null=True, blank=True)
    unidades = models.ManyToManyField(Unidad)
    horarios = models.ManyToManyField(Horario)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'curso'
        ordering = ['-updated_at']
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'

    def __str__(self):
        return self.nombre