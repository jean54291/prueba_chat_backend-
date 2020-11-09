from django.shortcuts import render
from rest_framework.response import Response
from .serializers import MensajeSerializer,PersonasSereializer
from modulos.usuarios.models import Usuario
from modulos.mensajes.models import Mensaje
from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404



class MensajeApi(APIView):
    def get_object(self, pk):
        try:
            return Mensaje.objects.get(id=pk,borrado=False) 
        except Mensaje.DoesNotExist:
            raise Http404

        # Crear mensajes
    def post(self,request):
        serializer = MensajeSerializer(data= request.data)
        if serializer.is_valid():
            mensajes= serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)


        #Buscar mensajes
    def get(self, request, pk=False, format=None):
        if not pk:
            mensaje = Mensaje.objects.values('id','borrado','observaciones','notas','image','fecha_creacion','usuario_id','usuario__username','usuario__first_name','usuario__last_name').filter(borrado=False)
        else:
            mensaje = Mensaje.objects.filter(id = pk ,borrado=False)
        # print(mensaje)
        serializer = MensajeSerializer(mensaje, many=True)
        return Response(serializer.data)


        # Actualizar mensaje
    def put(self, request, pk, format=None):
        mensaje = self.get_object(pk)
        serializer = MensajeSerializer(mensaje, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)