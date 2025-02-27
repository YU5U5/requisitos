from django.urls import path
from .views import ActualizarUsuarioView


urlpatterns = [
    
    path('<int:usuario_id>/', ActualizarUsuarioView.as_view(), name='actualizar_usuario'),  # Ruta para actualizar un usuario
]