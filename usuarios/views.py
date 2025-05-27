from rest_framework import viewsets
from .models import Usuario, UsuarioType, Documento
from .serializers import UsuarioSerializer, UsuarioTypeSerializer, DocumentoSerializer
from rest_framework.permissions import AllowAny  # o IsAuthenticated según lo que quieras

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [AllowAny]  # Cambia si quieres restringir acceso

class UsuarioTypeViewSet(viewsets.ModelViewSet):
    queryset = UsuarioType.objects.all()
    serializer_class = UsuarioTypeSerializer
    permission_classes = [AllowAny]

class DocumentoViewSet(viewsets.ModelViewSet):
    queryset = Documento.objects.all()
    serializer_class = DocumentoSerializer
    permission_classes = [AllowAny]

