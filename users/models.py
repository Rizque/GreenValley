from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import uuid
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut


class Profile(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True)
    username = models.CharField(max_length=200, )
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=500, )
    phone = models.CharField(max_length=8, blank=True, null=True)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        if self.user:
            self.first_name = self.user.first_name
            self.last_name = self.user.last_name
        super(Profile, self).save(*args, **kwargs)


class Farm(models.Model):
    owner = models.OneToOneField(
        Profile, on_delete=models.CASCADE, blank=True, null=True
    )
    name = models.CharField(max_length=200)
    description = models.TextField()
    foto = models.ImageField(null=True, blank=True)
    phone = models.CharField(max_length=8, blank=True, null=True)
    country = models.CharField(max_length=200, default="Latvija")
    city = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    latitude = models.CharField(max_length=200, blank=True, null=True)
    longitude = models.CharField(max_length=200, blank=True, null=True)
    date = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        if self.country and self.city and self.address:
            address = f"{self.country}, {self.city}, {self.address}"
            latitude, longitude = geocode_address(address)
            if latitude is not None and longitude is not None:
                self.latitude = str(latitude)
                self.longitude = str(longitude)
        super(Farm, self).save(*args, **kwargs)


def geocode_address(address):
    geolocator = Nominatim(user_agent='my_app_name')
    try:
        location = geolocator.geocode(address)
        if location is not None:
            return location.latitude, location.longitude
        return None, None
    except GeocoderTimedOut:
        return geocode_address(address)


class Client (models.Model):
    person = models.OneToOneField(
        Profile, on_delete=models.CASCADE, blank=True, null=True
    )
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
