from rest_framework import serializers
from core.product.models import Product


class ProductBase(serializers.ModelSerializer):
    name = serializers.CharField(help_text="`name` of product")
    price = serializers.IntegerField(help_text="`price of product")
    store_id = serializers.IntegerField(help_text="`id` off store")

    class Meta:
        model = Product
        fields = ("id", "name", 'price', 'store_id')


class ProductCreateSerializers(ProductBase):
    pass


class ProductUpdateSerializers(ProductBase):
    price = serializers.IntegerField(help_text="`price of product")


class ProductResponseSerializers(ProductBase):
    pass


""""
    Tạo serializers ở đây
"""


class Example(serializers.ModelSerializer):
    pass
