from django.db import models


class Saimnieciba(models.Model):
    s_nosaukums = models.CharField(max_length=200)
    s_apraksts = models.TextField()
    s_foto = models.ImageField()
    lokacija = models.CharField(max_length=200)

    def __str__(self):
        return self.nosaukums
