from rest_framework.serializers import ModelSerializer

from carts.models import Cart, CartProduct
from products.serializers import ProductVariantSerializer


class CartProductSerializer(ModelSerializer):
    product_variant = ProductVariantSerializer()

    class Meta:
        model = CartProduct
        fields = ['id', 'product_variant', 'quantity', 'applied_for_return', 'return_status']


class CartSerializer(ModelSerializer):
    cart_products = CartProductSerializer(many=True)

    class Meta:
        model = Cart
        fields = ['id', 'cart_products', 'subtotal', 'total', 'checkout']
