from django.contrib.auth.models import User
from django.db import models


class Room(models.Model):
    name = models.CharField(max_length=255)
    is_group = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return self.name


class RoomUser(models.Model):
    room = models.ForeignKey(Room, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)


class Chat(models.Model):
    user = models.ForeignKey(
        User,
        related_name='conversations',
        on_delete=models.CASCADE
    )
    room = models.ForeignKey(
        Room,
        related_name='conversations',
        on_delete=models.CASCADE
    )
    message = models.CharField(max_length=1024)
    is_read = models.BooleanField(default=False, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return f"{self.id}: {self.message}"
