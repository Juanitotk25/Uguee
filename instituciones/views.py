from rest_framework import viewsets
from .models import Institucion, InsPaleta
from .serializers import InstitucionSerializer, InsPaletaSerializer

class InstitucionViewSet(viewsets.ModelViewSet):
    queryset = Institucion.objects.all()
    serializer_class = InstitucionSerializer

class InsPaletaViewSet(viewsets.ModelViewSet):
    queryset = InsPaleta.objects.all()
    serializer_class = InsPaletaSerializer



