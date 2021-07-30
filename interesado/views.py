from rest_framework.generics import CreateAPIView
from .serializers import InteresadoSerializer
from .models import Interesado


# Create your views here.
class InteresadoCreateAPIView(CreateAPIView):
    serializer_class = InteresadoSerializer
