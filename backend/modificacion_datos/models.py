from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager, PermissionsMixin

# Create your models here.

class UsuarioManager(BaseUserManager):
    def create_user(self, nombre,correo_electronico, password=None):
        if not correo_electronico:
            raise ValueError('El correo electrónico es obligatorio')
        correo_electronico = self.normalize_email(correo_electronico)
        usuario = self.model(nombre=nombre, correo_electronico=correo_electronico)
        usuario.set_password(password)
        usuario.save(using=self._db)
        return usuario
    
    def create_superuser(self, correo_electronico, nombre, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)  # Permiso para acceder al panel de administración
        extra_fields.setdefault("is_superuser", True)  # Permiso de superusuario
        return self.create_user(correo_electronico, nombre, password, **extra_fields)
    
class Usuario(AbstractBaseUser, PermissionsMixin):
    nombre = models.CharField(max_length=100)  
    correo_electronico = models.EmailField(unique=True) 
    password = models.CharField(max_length=100) 
    fecha_registro = models.DateTimeField(auto_now_add=True) 
    last_login = models.DateTimeField(auto_now=True)  

    is_active = models.BooleanField(default=True)  # Indica si el usuario está activo
    is_staff = models.BooleanField(default=False)  # Permiso para acceder al panel de administración

    objects = UsuarioManager()  # Se vincula con el manager personalizado

    # Campo que se usará para iniciar sesión en lugar de 'username'
    USERNAME_FIELD = 'correo_electronico'
    REQUIRED_FIELDS = ['nombre']  # Campos obligatorios 

    def __str__(self):
        return self.nombre  # Devuelve el nombre del usuario cuando se muestra como texto

    class Meta:
        db_table = 'usuario' 
       