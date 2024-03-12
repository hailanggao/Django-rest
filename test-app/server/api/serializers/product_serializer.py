from rest_framework import serializers
from rest_framework.reverse import reverse

from ..models.products import Product


class ProductSerializer(serializers.ModelSerializer):
    # this will custimize the dicount fieldname and retrieve this field method with get prefix: get_discount
    discount = serializers.SerializerMethodField(read_only=True)
    edit_url = serializers.SerializerMethodField(read_only=True)  # one way
    url = serializers.HyperlinkedIdentityField(
        view_name="product-detail", lookup_field="pk"
    )  # preferred way
    email = serializers.EmailField(write_only=True)

    class Meta:
        model = Product
        fields = [
            "email",
            "url",
            "edit_url",
            "id",
            "title",
            "content",
            "price",
            "sale_price",
            "discount",
        ]

    # def create(self, validated_data):
    #     #return Product.objects.create(**validated_data)
    #     #email = validated_data.pop("email")
    #     obj = super().create(validated_data)
    #     #print(email, obj)
    #     return obj

    # def update(self, instance, validated_data):
    #     email = validated_data.pop("email")
    #     return super().update(instance, validated_data)

    def get_edit_url(self, obj):
        request = self.context.get("request")
        if request is None:
            return None
        return reverse(
            "product-edit", kwargs={"pk": obj.pk}, request=request
        )  # product-edit is the url view name in the url patterns

    # This will call the Product.get_discount method and return it to custimized field discount above
    def get_discount(self, obj):

        if not hasattr(obj, "id"):
            return None
        if not isinstance(obj, Product):
            return None
        return obj.get_discount()
