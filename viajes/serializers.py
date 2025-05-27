from rest_framework import serializers
from .models import Viaje, PasajeroViaje

class ViajeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Viaje
        fields = '__all__'

class PasajeroViajeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PasajeroViaje
        fields = '__all__'
