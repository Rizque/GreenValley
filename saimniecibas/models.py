from django.db import models
import uuid


class Saimnieciba(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    s_nosaukums = models.CharField(max_length=200)
    s_apraksts = models.TextField()
    s_foto = models.ImageField(null=True, blank=True, default='default.jpg')
    lokacija = models.CharField(max_length=200)

    def __str__(self):
        return self.s_nosaukums
