from rest_framework.serializers import ModelSerializer

from products.models import (
    ProductAttributeName, ProductAttributeValue, ProductAttribute,
    PropertyName, Property,
    Product, ProductVariant
)
from reviews.serializers import ReviewSerializer


class ProductAttributeNameSerializer(ModelSerializer):
    class Meta:
        model = ProductAttributeName
        fields = '__all__'


class ProductAttributeValueSerializer(ModelSerializer):
    attr = ProductAttributeNameSerializer()

    class Meta:
        model = ProductAttributeValue
        fields = '__all__'


class ProductAttributeSerializer(ModelSerializer):
    attr = ProductAttributeNameSerializer()
    values = ProductAttributeValueSerializer(many=True)

    class Meta:
        model = ProductAttribute
        fields = '__all__'


class PropertyNameSerializer(ModelSerializer):
    class Meta:
        model = PropertyName
        fields = '__all__'


class PropertySerializer(ModelSerializer):
    attr = PropertyNameSerializer()

    class Meta:
        model = Property
        fields = '__all__'


class ProductSerializer(ModelSerializer):
    properties = PropertySerializer(many=True)
    attributes = ProductAttributeSerializer(many=True)
    reviews = ReviewSerializer(read_only=True, many=True)

    class Meta:
        model = Product
        fields = [
            'id', 'slug', 'title', 'brand', 'image', 'description', 'type', 'gender', 'price',
            'properties', 'attributes',
            'featured', 'active', 'timestamp',
            'reviews',
            'url'
        ]


class ProductDetailSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'slug', 'image', 'price', 'url']


class ProductVariantSerializer(ModelSerializer):
    product = ProductSerializer()
    attributes = ProductAttributeValueSerializer(many=True)

    class Meta:
        model = ProductVariant
        fields = '__all__'
