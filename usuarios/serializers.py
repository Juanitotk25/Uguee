from rest_framework import serializers
from .models import Usuario, UsuarioType, Documento
from supabase import create_client
import os

# Carga variables de entorno para Supabase
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class UsuarioTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioType
        fields = '__all__'

class DocumentoSerializer(serializers.ModelSerializer):
    archivo = serializers.FileField(write_only=True, required=True)  # Para recibir el archivo

    class Meta:
        model = Documento
        fields = ['uid', 'tipo', 'url', 'archivo']
        read_only_fields = ['url']

    def create(self, validated_data):
        archivo = validated_data.pop('archivo')

        # Genera una ruta única para el archivo
        path = f"documentos/{archivo.name}"

        # Sube el archivo a Supabase Storage
        response = supabase.storage.from_('documentos').upload(path, archivo)
        if response.get('error'):
            raise serializers.ValidationError("Error al subir archivo a Supabase Storage")

        # Obtiene la URL pública del archivo subido
        public_url = supabase.storage.from_('documentos').get_public_url(path)['publicURL']

        validated_data['url'] = public_url

        return super().create(validated_data)

