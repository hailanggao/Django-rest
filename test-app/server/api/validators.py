from rest_framework import serializers
from .models.products import Product


def validate_title(value):
    qs = Product.objects.filter(title__iexact=value)  # iexact is case sensitive
    if qs.exists():
        raise serializers.ValidationError(f"{value} is already exists.")
    return value
