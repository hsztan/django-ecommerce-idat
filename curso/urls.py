from django.urls import path
from .views import CursoListAPIView, CursoRetrieveAPIView

urlpatterns = [
    path('', CursoListAPIView.as_view(), name='curso'),
    path('<int:id>', CursoRetrieveAPIView.as_view(), name='curso')
]
