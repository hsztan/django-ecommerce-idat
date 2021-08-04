from django.db.models import query
from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, ListCreateAPIView
from .serializers import AddOrderSerializer, CuponSerializer
from .models import Cupon, Order
from curso.models import Curso
from authentication.models import User
from interesado.models import Interesado
import uuid

# Create your views here.

class CuponListView(ListAPIView):
    queryset = Cupon.objects.all()
    serializer_class = CuponSerializer

class OrderCreateListView(ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = AddOrderSerializer
    
    def post(self, request, *args, **kwargs):
        
        total_price = 0
        for curso_id in request.data["cursos"]:
            curso = Curso.objects.get(id=curso_id)
            total_price += curso.precio
        if request.data.get('cupon', ''):
            cupon = Cupon.objects.get(request.data['cupon'])
            if cupon.precio:
                total_price -= cupon.precio
            if cupon.porcentaje:
                total_price *= (1 - cupon.porcentaje *0.1)
        request.data["total"] = total_price

        user = User.objects.get(id=request.data["user"])
        # if Interesado.objects.get(correo=user.email):
        #     total_price *= .9 #TODO
        # from pdb import set_trace
        # set_trace()
        print(total_price)


        code = str(uuid.uuid4().hex)[:11]
        request.data["code"] = code
        return self.create(request, *args, **kwargs)
