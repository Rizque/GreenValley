from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import uuid

class Profile(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    username = models.CharField(max_length=200, blank=True, null=True)
    s_nosaukums = models.CharField(max_length=200)
    s_apraksts = models.TextField()
    s_foto = models.ImageField(null=True, blank=False, default='defaultx.jpg',)
    email = models.EmailField(max_length=500, blank=True, null=True)
    talrunis = models.CharField(max_length=8)
    lokacija = models.CharField(max_length=200)
    s_datums = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.s_nosaukums
    
    class Meta:
        db_table = 'saimniecibas_profile'
