from rest_framework.response import Response
from .serializers import PersonaSerializer
# from modulos.personas.models import Persona
# from django.contrib.auth.models import User
from modulos.usuarios.models import Usuario
from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404

class PersonAPI(APIView):

    def get_object(self, pk):
        try:
            return Usuario.objects.get(id=pk).order_by('-en_linea','-fecha_ultima_sesion') 
        except Usuario.DoesNotExist:
            raise Http404
    

    # Crear Usuarios
    def post(self,request):
        serializer = PersonaSerializer(data= request.data)
        if serializer.is_valid():
            persona= serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

    #Buscar usuarios
    def get(self, request, pk=False, format=None):
        if not pk:
            persona = Usuario.objects.all().order_by('-en_linea','-fecha_ultima_sesion') 
        else:
            persona = Usuario.objects.filter(id = pk)
        serializer = PersonaSerializer(persona, many=True)
        return Response(serializer.data)

    # Actualizar Usuarios
    def put(self, request, pk, format=None):
        persona = self.get_object(pk)
        serializer = PersonaSerializer(persona, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

