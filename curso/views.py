from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import CursoListSerializer, CursoSerializer, BeneficioListSerializer
from .models import Curso, Beneficio
from rest_framework import permissions


# Create your views here.
class CursoListAPIView(ListAPIView):
    serializer_class = CursoListSerializer
    queryset = Curso.objects.all()
    # permission_classes = [permissions.IsAuthenticated]

    # def perform_create(self, serializer):
    #     return serializer.save(user=self.request.user) # user_id

    # def get_queryset(self):
    #     return self.queryset.filter(user=self.request.user) # user_id

class CursoRetrieveAPIView(RetrieveAPIView):
    serializer_class = CursoSerializer
    queryset = Curso.objects.all()
    # permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'

    # def get_queryset(self):
    #     return self.queryset.filter(user=self.request.user)

class BeneficioListAPIView(ListAPIView):
    serializer_class = BeneficioListSerializer
    queryset = Beneficio.objects.all()