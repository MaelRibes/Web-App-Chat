from django.db import models


class Room(models.Model):
    name = models.CharField(max_length=255)
    urlRoom = models.SlugField(unique=True)

# Create your models here.
