from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    avatar = models.CharField(max_length=255, blank=True, null=True)


class Room(models.Model):
    name = models.CharField(max_length=255)
    is_group = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return self.name


class RoomUser(models.Model):
    room = models.ForeignKey(Room, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.DO_NOTHING
    )


class Chat(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='conversations',
        on_delete=models.DO_NOTHING
    )
    room = models.ForeignKey(
        Room,
        related_name='conversations',
        on_delete=models.DO_NOTHING
    )
    message = models.CharField(max_length=1024)
    is_read = models.BooleanField(default=False, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return f"{self.id}: {self.message}"
