# Create your models here.
from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    username = models.CharField(max_length=150)
    password = models.CharField(max_length=255)
