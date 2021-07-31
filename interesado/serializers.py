from django.core.exceptions import ObjectDoesNotExist, ValidationError
from rest_framework import serializers
from .models import Interesado
from curso.models import Curso
from rest_framework.status import HTTP_404_NOT_FOUND


class InteresadoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Interesado
        fields = ['id', 'nombre', 'correo', 'celular', 'curso']