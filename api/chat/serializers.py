from django.contrib.auth import authenticate, get_user_model
from django.core.exceptions import ValidationError
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

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


class RoomSerializer(serializers.ModelSerializer):

    class Meta:
        model = Room
        fields = '__all__'
        extra_kwargs = {
            'is_group': {'required': False}
        }


class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = '__all__'
        extra_kwargs = {
            'is_read': {'required': False},
            'created_at': {'required': False},
            'updated_at': {'required': False},
        }
