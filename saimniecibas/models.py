from django.db import models


class Saimnieciba(models.Model):
    nosaukums = models.CharField(max_length=200)
    apraksts = models.TextField()
    foto = models.ImageField()
    lokacija = models.CharField(max_length=200)

    def __str__(self):
        return self.nosaukums
