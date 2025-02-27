from rest_framework import serializers

class LoginSerializer(serializers.Serializer):
    correo = serializers.EmailField()
    password = serializers.CharFiel(write_only=True)