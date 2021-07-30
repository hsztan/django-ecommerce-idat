from django.urls import path
from .views import InteresadoCreateAPIView

urlpatterns = [
    path('', InteresadoCreateAPIView.as_view(), name='interesados'),
    # path('<int:id>', CursoRetrieveAPIView.as_view(), name='curso')
]
