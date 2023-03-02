from django.db import models


class User(models.Model):
    pseudo = models.CharField(max_length=20)
    password = models.CharField(max_length=255)


class Room(models.Model):
    name = models.CharField(max_length=255)
    urlRoom = models.SlugField(unique=True)


class Message(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    date = models.DateField()
