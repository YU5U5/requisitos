from django.db import models
from django.contrib.auth.models import BaseUserManager

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

class Usuario(models.Model):  # La clase `Usuario` debe estar bien definida
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    correo_electronico = models.CharField(max_length=100, unique=True)
    celular = models.CharField(max_length=10)
    direccion = models.CharField(max_length=255, blank=True, null=True)
    fecha_registro = models.DateTimeField()
    last_login = models.DateTimeField()

    objects = UsuarioManager()  # Asigna el manager personalizado

    def __str__(self):
        return self.nombre
    class Meta:
        managed = False  
        db_table = 'Usuario'  

