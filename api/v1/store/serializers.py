from rest_framework import serializers

from core.store.models import Store


class StoreBase(serializers.ModelSerializer):
    name = serializers.CharField(help_text="`name` of store")
    address = serializers.CharField(help_text="`address` of store")

    class Meta:
        model = Store
        fields = ("id", "name", "address")


class StoreCreateSerializers(StoreBase):
    pass


class StoreUpdateSerializers(StoreBase):
    pass


class StoreResponseSerializers(StoreBase):
    pass
