from rest_framework import serializers

from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    # reviews = ReviewSerializer(many=True)

    class Meta:
        model = Product
        fields = ['id']


class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'slug', 'image', 'price', 'url']
