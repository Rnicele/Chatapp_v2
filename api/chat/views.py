from django.core.exceptions import ValidationError
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from . import serializers as sl
from .helpers import user_construct
from .models import Chat, Room


class Login(APIView):
    def post(self, request):
        serializer = sl.LoginSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, 400)

        user = serializer.login()

        if user is None:
            return Response('Username or password is incorrect.', 400)

        return Response(user_construct(user))


class Register(APIView):
    def post(self, request):
        serializer = sl.RegisterSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, 400)

        try:
            user = serializer.register()
        except ValidationError as e:
            return Response(e.messages, 400)

        return Response(user_construct(user))


class RoomList(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = sl.RoomSerializer


class RoomDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = sl.RoomSerializer


class ChatList(generics.ListCreateAPIView):
    queryset = Chat.objects.all()
    serializer_class = sl.ChatSerializer


class ChatDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Chat.objects.all()
    serializer_class = sl.ChatSerializer
