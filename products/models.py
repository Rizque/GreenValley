from django.db import models
from users.models import Profile, Farm
from django.utils import timezone
import uuid

# Create your models here.


class Product(models.Model):
    product_id = models.UUIDField(default=uuid.uuid4, unique=True,
                                  primary_key=True, editable=False)
    farm = models.ForeignKey(
        Profile, null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
