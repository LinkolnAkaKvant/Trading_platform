from django.contrib.auth import authenticate
from rest_framework import serializers
from core.models import User


class UserSerializer(serializers.ModelSerializer):
    """
    Сериализатор для подели пользователя
    """
    password = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'password']


class LoginSerializer(serializers.Serializer):
    """
    Сериализатор для работы с логированием пользователя
    """
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')
        user = authenticate(username=username, password=password)
        if user and user.is_active:
            return user
        raise serializers.ValidationError('Неверное имя пользователя или пароль')


class ProfileSerializer(serializers.ModelSerializer):
    """
    Сериализатор для работы с профилем пользователя
    """
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']