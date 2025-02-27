from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UsuarioRegistroSerializer, UsuarioUpdateSerializer
from registro.models import Usuario
from django.contrib.auth.hashers import check_password

# Create your views here.

class RegistroUsuarioView(APIView):
    def post(self, request):
        serializer = UsuarioRegistroSerializer(data=request.data)
        if serializer.is_valid():
            usuario = serializer.save()
            return Response({
                'mensaje': 'Registro exitoso',
                'correo_electronico': usuario.correo_electronico,
                'nombre': usuario.nombre
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

class ActualizarUsuarioView(APIView):
    def put(self, request, usuario_id):
        try:
            usuario = Usuario.objects.get(id=usuario_id)
        except Usuario.DoesNotExist:
            return Response({
                'mensaje': 'Usuario no encontrado'
            }, status=status.HTTP_404_NOT_FOUND)
            
        serializer = UsuarioUpdateSerializer(usuario, data=request.data, partial=True)  # Permite actualización parcial
        if serializer.is_valid():
            serializer.save()
            return Response({"mensaje": "Usuario actualizado correctamente"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
        
        
            
            



