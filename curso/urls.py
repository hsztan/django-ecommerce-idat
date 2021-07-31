from django.urls import path
from .views import CursoListAPIView, CursoRetrieveAPIView, BeneficioListAPIView

urlpatterns = [
    path('', CursoListAPIView.as_view(), name='cursos'),
    path('<int:id>', CursoRetrieveAPIView.as_view(), name='cursos'),
    path('beneficios/', BeneficioListAPIView.as_view(), name='beneficios'),
]
