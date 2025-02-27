from django.urls import path
from .views import ActualizarUsuarioView


urlpatterns = [
<<<<<<< HEAD
=======
    
>>>>>>> 2d5ec2d714b3400d29e1338625d8d3483b75d854
    path('actualizar/<int:usuario_id>/', ActualizarUsuarioView.as_view(), name='actualizar_usuario'),  # Ruta para actualizar un usuario
]