from django.contrib import admin

# Register your models here.
from .models.products import Product

admin.site.register(Product)
