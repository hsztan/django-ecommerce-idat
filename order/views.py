from django.db.models import query
from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, ListCreateAPIView
from .serializers import AddOrderSerializer, CuponSerializer
from .models import Cupon, Order
import uuid

# Create your views here.

class CuponListView(ListAPIView):
    queryset = Cupon.objects.all()
    serializer_class = CuponSerializer

class AddOrderView(CreateAPIView):
    serializer_class = AddOrderSerializer
    
    def post(self, request, *args, **kwargs):
        # from pdb import set_trace
        # set_trace()
        code = str(uuid.uuid4().hex)[:11]
        request.data["code"] = code
        return self.create(request, *args, **kwargs)
