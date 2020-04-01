from rest_framework.serializers import Serializer

from products.serializers import PropertySerializer, ProductAttributeSerializer


class ProductFiltersSerializer(Serializer):
    properties = PropertySerializer(many=True, read_only=True)
    attributes = ProductAttributeSerializer(many=True, read_only=True)

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass
