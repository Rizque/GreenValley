from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import uuid


class Profile(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True)
    username = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=500, blank=True, null=True)
    phone = models.CharField(max_length=8)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.username


class Farm (models.Model):
    owner = models.OneToOneField(
        Profile, on_delete=models.CASCADE, blank=True, null=True
    )
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField()
    foto = models.ImageField(null=True, blank=False, default='defaultx.jpg',)
    city = models.CharField(max_length=200, blank=True, null=True)
    country = models.CharField(
        max_length=200, blank=True, null=True, default="Latvija")
    address = models.CharField(max_length=200, blank=True, null=True)
    latitude = models.CharField(max_length=200, blank=True, null=True)
    longitude = models.CharField(max_length=200, blank=True, null=True)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
