from rest_framework import viewsets
from .models import Viaje, PasajeroViaje
from .serializers import ViajeSerializer, PasajeroViajeSerializer

class ViajeViewSet(viewsets.ModelViewSet):
    queryset = Viaje.objects.all()
    serializer_class = ViajeSerializer

class PasajeroViajeViewSet(viewsets.ModelViewSet):
    queryset = PasajeroViaje.objects.all()
    serializer_class = PasajeroViajeSerializer
