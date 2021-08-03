from rest_framework import serializers
from .models import Cupon, Order

class CuponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cupon
        fields = ['id', 'precio', 'porcentaje']

class AddOrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ['id', 'user', 'cursos', 'code']