from django.db import models
from users.models import Profile, Farm
from django.utils import timezone
from django.core.validators import MinValueValidator

import uuid

# Create your models here.


class ProductCategory(models.Model):
    name = models.CharField(max_length=200, unique=True)
    category_id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name


UNIT_CHOICES = (
        ('kg', 'kilogrami'),
        ('g', 'grami'),
        ('l', 'litri'),
        ('ml', 'mililitri'),
        ('gab', 'gabalā'),
    )

class Product(models.Model):
    product_id = models.UUIDField(default=uuid.uuid4, unique=True,
                                  primary_key=True, editable=False)
    farm = models.ForeignKey(
        Profile, null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=200)
    category = models.ForeignKey(
        ProductCategory, on_delete=models.CASCADE, null=True)
    description = models.TextField()
    p_foto = models.ImageField(null=True, blank=False)

    price = models.DecimalField(
        max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])

    unit = models.CharField(max_length=20, choices=UNIT_CHOICES, default='gab')
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
