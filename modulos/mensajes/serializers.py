from rest_framework import serializers
from modulos.mensajes.models import Mensaje
from modulos.usuarios.models import Usuario
from modulos.usuarios.serializers import PersonaSerializer
from collections import OrderedDict
import json
class PersonasSereializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = [
            'id',
            'username'
        ]


class MensajeSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField(required=False)
    borrado = serializers.BooleanField(required=False)
    observaciones = serializers.CharField(required=False)
    notas = serializers.CharField(required=False)
    image = serializers.CharField(required=False)
    # image = serializers.FileField(required=False)
    fecha_creacion = serializers.ReadOnlyField(required=False)
    usuario_id = serializers.CharField(required=False)
    usuario__username= serializers.ReadOnlyField(required=False)
    usuario__last_name = serializers.ReadOnlyField(required=False)
    usuario__first_name = serializers.ReadOnlyField(required=False)

    def create(self, validate_data):        
        
        mensaje = Mensaje()
        mensaje.borrado = validate_data.get('borrado')
        mensaje.observaciones = validate_data.get('observaciones')
        mensaje.notas = validate_data.get('notas')
        mensaje.image = validate_data.get('image')
        mensaje.fecha_creacion = validate_data.get('fecha_creacion')
        mensaje.usuario_id = validate_data.get('usuario_id')
        mensaje.save()
        return mensaje
        


    def update(self, instance, validated_data):
        instance.borrado = validated_data.get('borrado')
        instance.observaciones = validated_data.get('observaciones')
        instance.notas = validated_data.get('notas')
        instance.image = validated_data.get('image')
        instance.fecha_creacion = validated_data.get('fecha_creacion')
        instance.usuario_id = validated_data.get('usuario_id')
        instance.save()
        return instance

    class Meta:
        model = Mensaje
        fields="__all__"