from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from .serializers import UsuarioSerializer
from .models import Usuario
from django.core.mail import send_mail
from django.utils import timezone
import random


@api_view(['POST'])
@permission_classes([AllowAny])
def registro(request):
    if request.method == 'POST':
        try:
            data = request.data
            serializer = UsuarioSerializer(data=data)

            # Validar el formato de los datos
            if not serializer.is_valid():
                return JsonResponse({
                    'error': 'Datos inválidos',
                    'details': serializer.errors
                }, status=400)

            # Validar que las contraseñas coincidan
            if data['password1'] != data['password2']:
                return JsonResponse({
                    'error': 'Las contraseñas no coinciden'
                }, status=400)

            # Crear el usuario manualmente
            user = Usuario.objects.create_user(
                nombre=data['nombre'],
                correo_electronico=data['correo_electronico'],
                password=data['password1'],
            )

            return JsonResponse({
                'mensaje': 'Usuario registrado correctamente',
                'usuario_id': user.id
            }, status=201)

        except Exception as e:
            return JsonResponse({
                'error': str(e)
            }, status=400)

    return JsonResponse({
        'error': 'Método no permitido'
    }, status=405)
