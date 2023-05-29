from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import uuid


class Profile(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True)
    username = models.CharField(max_length=200, )
    email = models.EmailField(max_length=500, )
    phone = models.CharField(max_length=8, blank=True, null=True)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.username


class Farm (models.Model):
    owner = models.OneToOneField(
        Profile, on_delete=models.CASCADE, blank=True, null=True
    )
    name = models.CharField(max_length=200)
    description = models.TextField()
    foto = models.ImageField(null=True, blank=False, default='defaultx.jpg',)
    city = models.CharField(max_length=200)
    country = models.CharField(
        max_length=200,  default="Latvija")
    address = models.CharField(max_length=200,)
    latitude = models.CharField(max_length=200, blank=True, null=True)
    longitude = models.CharField(max_length=200, blank=True, null=True)
    date = models.DateTimeField(default=timezone.now)

    # def __str__(self):
    #     return self.name


class Client (models.Model):
    person = models.OneToOneField(
        Profile, on_delete=models.CASCADE, blank=True, null=True
    )
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
