from rest_framework import serializers
from modulos.mensajes.models import Mensaje
from modulos.usuarios.models import Usuario
from modulos.usuarios.serializers import PersonaSerializer
from collections import OrderedDict
import json


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=False)
    password = serializers.CharField(required=False)