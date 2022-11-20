from django.db import models
import uuid
from django.utils import timezone
from django.contrib.auth.models import User


class Saimnieciba(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    lietotajs = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True)

    s_nosaukums = models.CharField(max_length=200)
    s_apraksts = models.TextField()
    s_foto = models.ImageField(null=True, blank=True, default='default.jpg')
    # talrunis = models.IntegerField(default=0, null=True, blank=True)

    lokacija = models.CharField(max_length=200)
    datums = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.s_nosaukums
