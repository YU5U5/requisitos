from django.db import models
from django.db import models
from django.contrib.auth.models import BaseUserManager


# Create your models here.
class UsuarioManager(BaseUserManager):
    def create_user(self, correo_electronico, nombre, password=None, **extra_fields):
        if not correo_electronico:
            raise ValueError('El correo electrónico es obligatorio')
        correo_electronico = self.normalize_email(correo_electronico)
        usuario = self.model(correo_electronico=correo_electronico, nombre=nombre, **extra_fields)
        usuario.set_password(password)
        usuario.save(using=self._db)
        return usuario

    def create_superuser(self, correo_electronico, nombre, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(correo_electronico, nombre, password, **extra_fields)


    nombre = models.CharField(max_length=100)
    correo_electronico = models.EmailField(unique=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)


    USERNAME_FIELD = 'correo_electronico'
    REQUIRED_FIELDS = ['nombre']

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'Usuario'
        managed = False