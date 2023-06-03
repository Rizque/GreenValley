from django.contrib import admin
from .models import Product, ProductCategory, Rating

admin.site.register(Product)
admin.site.register(ProductCategory)
admin.site.register(Rating)
