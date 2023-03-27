from django.db import models
from saimniecibas.models import Profile
from django.utils import timezone
import uuid


class Product(models.Model):
    saimnieciba = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.SET_NULL)
    p_nosaukums = models.CharField(max_length=200)
    p_apraksts = models.TextField()
    p_foto = models.ImageField(null=True, blank=False)
    cena = models.DecimalField(max_digits=7, decimal_places=2)
    mervienibu_veidi = (
        ('kg', 'kilogrami'),
        ('g', 'grami'),
        ('l', 'litri'),
        ('ml', 'mililitri'),
        ('gab', 'gabalā'),
    )
    cenas_mervieniba = models.CharField(max_length=100, choices=mervienibu_veidi)
    p_datums = models.DateTimeField(default=timezone.now)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.p_nosaukums
