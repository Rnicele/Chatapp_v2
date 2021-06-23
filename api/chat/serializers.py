from django.contrib.auth import authenticate
from rest_framework import serializers

from .models import Chat, Room


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=255)

    def login(self):
        return authenticate(**self.validated_data)


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
