from django.contrib.auth import authenticate, get_user_model
from rest_framework import serializers

from .models import Chat, Room

UserModel = get_user_model()


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=255)

    def login(self):
        return authenticate(**self.validated_data)


class RegisterSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=255)
    last_name = serializers.CharField(max_length=255)
    email = serializers.EmailField()
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=255)

    def register(self):
        user = UserModel(**self.validated_data)
        user.set_password(self.validated_data['password'])
        user.validate_unique()
        user.save()

        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['id', 'first_name', 'last_name']
