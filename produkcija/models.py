from django.db import models
from saimniecibas.models import Saimnieciba

# Create your models here.


class Produkts(models.Model):
    saimnieciba = models.ForeignKey(Saimnieciba, on_delete=models.CASCADE)
    p_nosaukums = models.CharField(max_length=200)
    p_apraksts = models.TextField()
    p_foto = models.ImageField()
    cena = models.DecimalField(max_digits=7, decimal_places=2)
    mervienibu_veidi = (
        ('kg', 'Kilogrami'),
        ('ml', 'mililitri'),
        ('l', 'litri'),
        ('gab', 'gabalā')
    )
    cenas_mervieniba = models.CharField(
        max_length=100, choices=mervienibu_veidi)
