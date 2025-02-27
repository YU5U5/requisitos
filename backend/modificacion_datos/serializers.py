from rest_framework import serializers
from registro.models import Usuario


class RegistroUsuarioSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = Usuario
        fields = ['nombre', 'correo_electronico', 'password']
    
    def create(self, validated_data):
        usuario = Usuario.objects.create_user(**validated_data)  # Usa el manager para crear un usuario
        return usuario
    
class UsuarioUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['nombre', 'correo_electronico', 'password']  # Campos que pueden actualizarse
        extra_kwargs = {
            'password': {'write_only': True, 'required': False},  # La contraseña es opcional en la actualización
        }
    
    def update(self, instance, validated_data):
        if 'password' in validated_data:
            instance.set_password(validated_data['password'])  # Hashea la nueva contraseña
        instance.nombre = validated_data.get('nombre', instance.nombre)  # Actualiza el nombre si se proporciona
        instance.correo_electronico = validated_data.get('correo_electronico', instance.correo_electronico)  # Actualiza el correo
        instance.save()
        return instance