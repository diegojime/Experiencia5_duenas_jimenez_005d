from rest_framework import serializers
from apptienda.models import Cliente


class ClienteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cliente
        fields=['nombre','apellido', 'correo', 'rut', 'telefono', 'direccion']