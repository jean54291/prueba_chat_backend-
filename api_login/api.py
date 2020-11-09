from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from modulos.usuarios.models import Usuario
from django.contrib.auth.hashers import check_password
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework import status
from django.forms.models import model_to_dict
from .serializers import LoginSerializer
from collections import OrderedDict
from django.http import HttpResponse
from django.core.serializers.json import DjangoJSONEncoder
import json
from json import loads, dumps

class Login (APIView):
    def post(self,request):
        serializer = LoginSerializer(data= request.data)
        if serializer.is_valid():
            print(request.data)
            username = request.data.get('username')
            password = request.data.get('pass')
            try:
                user = Usuario.objects.get(username=username)
            except  Usuario.DoesNotExist:
                respuesta = {"status":status.HTTP_200_OK,"errores":"usuario no existe"}
                return HttpResponse(dumps(respuesta, cls=DjangoJSONEncoder))
            
            pw_valid = check_password(password, user.password)
            if not pw_valid:
                respuesta = {"status":status.HTTP_200_OK,"errores":"password invalido"}
                return HttpResponse(dumps(respuesta, cls=DjangoJSONEncoder))

            autenticacion = authenticate(username = user.username, password = user.password)
            token,_ = Token.objects.get_or_create(user=user)
            datos = []
            print(token)
            if token:
                user.en_linea = True
                user.save()
                datos.append(model_to_dict(user))
                respuesta = {"status":status.HTTP_200_OK,"token":str(token),"errores":False,"datos":datos}
        
        return HttpResponse(dumps(respuesta, cls=DjangoJSONEncoder))

class Logout (APIView):
    def post(self, request):
        serializer = LoginSerializer(data= request.data)
        if serializer.is_valid():
            id_user = request.data.get('id')
            try:
                user = Usuario.objects.get(id=id_user)
                user.en_linea = False
                token = Token.objects.get(user=user)
                token.delete()
                user.save()
                respuesta = {"status":status.HTTP_200_OK,"errores":False}
                return HttpResponse(dumps(respuesta, cls=DjangoJSONEncoder))
            except Token.DoesNotExist:
                respuesta = {"status":status.HTTP_200_OK,"errores":"No existe el token para el usuario"}
                return HttpResponse(dumps(respuesta, cls=DjangoJSONEncoder))
        else:
            respuesta = {"status":status.HTTP_200_OK,"errores":"error al momento de hacer el logout"}
            return HttpResponse(dumps(respuesta, cls=DjangoJSONEncoder))