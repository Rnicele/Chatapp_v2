from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
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


class UserViewSet(viewsets.ViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request):
        query_set = User.objects.all()
        users = sl.UserSerializer(query_set, many=True)
        return Response(users.data)

    # def create(self, request):
    #     pass

    # def retrieve(self, request, pk=None):
    #     pass

    # def update(self, request, pk=None):
    #     pass

    # def partial_update(self, request, pk=None):
    #     pass

    # def destroy(self, request, pk=None):
    #     pass
