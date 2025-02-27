from django.urls import path
from . import views

urlpatterns = [
    path('', views.registro, name='registro'),  # Ruta para el registro
    #path('', views.validar_correo, name='validar_correo'),  # Ruta para validar correo
]