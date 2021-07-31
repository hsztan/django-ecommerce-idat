from rest_framework.generics import ListCreateAPIView
from .serializers import InteresadoSerializer
from .models import Interesado


# Create your views here.
class InteresadoCreateAPIView(ListCreateAPIView):
    queryset = Interesado.objects.all()
    serializer_class = InteresadoSerializer
