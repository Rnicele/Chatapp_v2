from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .helpers.auth import user_construct
from .models import Chat, Room
from .serializers import ChatSerializer, LoginSerializer, RoomSerializer


class Login(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.POST)

        if not serializer.is_valid():
            return Response(serializer.errors, 400)

        user = serializer.login()

        if user is None:
            return Response('Username or password is incorrect.', 400)

        return Response(user_construct(user))


class RoomList(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class RoomDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class ChatList(generics.ListCreateAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer


class ChatDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
