from rest_framework import serializers
from .models import Interesado


class InteresadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interesado
        fields = ['id', 'nombre', 'correo', 'celular', 'curso']