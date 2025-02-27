from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import LoginSerializer
from registro.models import Usuario
from django.contrib.auth.hashers import check_password
from rest_framework_simplejwt.tokens import RefreshToken
from django.utils.timezone import now

# Create your views here.

class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        
        # Validar el formato de los datos
        if not serializer.is_valid():
            return Response({
                'mensaje': 'Error en el inicio de sesión',
                'errores': serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
        
        correo_electronico = serializer.validated_data['correo_electronico']
        password = serializer.validated_data['password']

        # Verificar si el usuario existe
        try:
            usuario = Usuario.objects.get(correo_electronico=correo_electronico)
        except Usuario.DoesNotExist:
            return Response({
                'mensaje': 'Correo o contraseña inválidos.'
            }, status=status.HTTP_400_BAD_REQUEST)


        # Verificar si la contraseña es correcta
        if not check_password(password, usuario.password):
            return Response({
                'mensaje': 'Correo o contraseña inválidos.'
            }, status=status.HTTP_400_BAD_REQUEST)

        #actualiza fecha y hora despues del login
        usuario.last_login = now()
        usuario.save(update_fields=['last_login'])

        # Generar el token JWT
        refresh = RefreshToken.for_user(usuario)

        # Devolver la respuesta exitosa
        return Response({
            'mensaje': 'Inicio de sesión exitoso',
            'correo_electronico': usuario.correo_electronico,
            'access_token': str(refresh.access_token),  # Token de acceso
            'refresh_token': str(refresh)  # Refresh token
        }, status=status.HTTP_200_OK)