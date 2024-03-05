from rest_framework import serializers

from ..models.products import Product


class ProductSerializer(serializers.ModelSerializer):
    # this will custimize the dicount fieldname and retrieve this field method with get prefix: et_discount
    discount = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Product
        fields = ["title", "content", "price", "sale_price", "discount"]

    # This will call the Product.get_discount method and return it to custimized field discount above
    def get_discount(self, obj):

        if not hasattr(obj, "id"):
            return None
        if not isinstance(obj, Product):
            return None
        return obj.get_discount()
