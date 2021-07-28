from django.core.exceptions import ValidationError
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from . import serializers as sl
from .helpers import user_construct
from .models import Chat, Room, RoomUser, User


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


class UserViewSet(viewsets.ViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request):
        query_set = User.objects.exclude(pk=request.user.pk)
        return Response(sl.UserSerializer(query_set, many=True).data)


class RoomViewSet(viewsets.ViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def room_chats(self, request):
        if not 'uid' in request.GET or not 'cuid' in request.GET:
            return Response('Missing parameters.', 400)

        try:
            user = User.objects.get(id=request.GET['uid'])
            connected_user = User.objects.get(id=request.GET['cuid'])
        except User.DoesNotExist:
            return Response('Users not found.', 404)

        pivot = RoomUser.objects.filter(user_id=user.pk)

        if pivot.exists():
            user_room_ids = list(pivot.values_list('room_id', flat=True))
            connected_user_room = RoomUser.objects.filter(
                room_id__in=user_room_ids,
                user_id=connected_user.pk,
            ).first()

            if connected_user_room is not None:
                room = Room.objects.get(pk=connected_user_room.room_id)
                return Response(sl.RoomSerializer(room).data)

        room = Room.objects.create(
            name=connected_user.first_name,
            is_group=False
        )
        RoomUser.objects.create(room=room, user=user)
        RoomUser.objects.create(room=room, user=connected_user)
        return Response(sl.RoomSerializer(room).data)


class ChatViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Chat.objects.all()
    serializer_class = sl.ChatSerializer
