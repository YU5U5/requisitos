from django.urls import path
from .views import RegistroUsuarioView, ActualizarUsuarioView


urlpatterns = [
    path('registro/', RegistroUsuarioView.as_view(), name='registro'),  # Ruta para registrar un usuario
    path('actualizar/<int:usuario_id>/', ActualizarUsuarioView.as_view(), name='actualizar_usuario'),  # Ruta para actualizar un usuario
]