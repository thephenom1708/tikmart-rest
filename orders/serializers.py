from rest_framework import serializers

from addresses.serializers import AddressSerializer
from billing.serializers import BillingProfileSerializer
from carts.serializers import CartSerializer
from orders.models import Order


class OrderSerializer(serializers.ModelSerializer):
    billing_profile = BillingProfileSerializer(required=False)
    shipping_address = AddressSerializer(required=False)
    billing_address = AddressSerializer(required=False)
    timestamp = serializers.DateTimeField(format="%d %B %Y %I:%m %P")

    class Meta:
        model = Order
        fields = [
            'id', 'order_id', 'billing_profile', 'shipping_address', 'billing_address',
            'cart', 'payment_method', 'status', 'shipping_total', 'total', 'timestamp',
        ]


class OrderDetailSerializer(serializers.ModelSerializer):
    billing_profile = BillingProfileSerializer(required=False)
    shipping_address = AddressSerializer(required=False)
    billing_address = AddressSerializer(required=False)
    cart = CartSerializer(required=False)
    timestamp = serializers.DateTimeField(format="%d %B %Y %I:%m %P")

    class Meta:
        model = Order
        fields = '__all__'
