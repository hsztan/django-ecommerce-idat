from rest_framework import serializers
from .models import Leccion, Unidad, Curso, Horario


class HorarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Horario
        fields = ['id', 'fecha', 'frecuencia']


class LeccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leccion
        fields = ['id', 'nombre']


class UnidadSerializer(serializers.ModelSerializer):
    lecciones = LeccionSerializer(many=True)

    class Meta:
        model = Unidad
        fields = ['id', 'nombre', 'lecciones']


class CursoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = ['id', 'nombre', 'precio', 'image']

class CursoSerializer(serializers.ModelSerializer):
    unidades = UnidadSerializer(many=True)
    horarios = HorarioSerializer(many=True)

    class Meta:
        model = Curso
        fields = ['id', 'nombre', 'unidades', 'horarios', 'precio','resumen_corto', 'resumen_largo', 'duracion', 'image_thumb', 'image']