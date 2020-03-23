from rest_framework import viewsets, permissions, status, generics
from rest_framework.decorators import action
from rest_framework.response import Response

from addresses.models import Address
from orders.serializers import OrderSerializer
from orders.models import Order


class OrderViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.AllowAny,
    ]
    lookup_field = 'order_id'
    serializer_class = OrderSerializer

    def get_queryset(self):
        return self.request.user.billingprofile.orders.filter(active=True)

    @action(methods=['put'], detail=True,
            url_path='update-shipping-address/(?P<shipping_address>[0-9a-z]+)',
            url_name='update-shipping-address')
    def update_shipping_address(self, request, shipping_address, order_id=None):
        order = self.get_object()
        shipping_address_obj = Address.objects.get(id=shipping_address)
        order.shipping_address = shipping_address_obj
        order.save()
        return Response(data={
            'orderId': order_id,
            'shippingAddressId': order.shipping_address.id,
            'addressType': "shipping"
        }, status=status.HTTP_200_OK)

    @action(methods=['put'], detail=True,
            url_path='update-billing-address/(?P<billing_address>[0-9a-z]+)',
            url_name='update-billing-address')
    def update_billing_address(self, request, billing_address, order_id=None):
        billing_address_obj = Address.objects.get(id=billing_address)
        order = self.get_object()
        order.billing_address = billing_address_obj
        order.save()
        return Response(data={
            'orderId': order_id,
            'billingAddressId': order.billing_address.id,
            'addressType': "billing"
        }, status=status.HTTP_200_OK)

    @action(methods=['put'], detail=True,
            url_path='update-payment-method',
            url_name='update-payment-method')
    def update_payment_method(self, request, order_id=None):
        order = self.get_object()
        order.payment_method = request.data.get('payment_method')
        order.save()
        return Response(data={
            'orderId': order_id,
            'paymentMethod': order.payment_method
        }, status=status.HTTP_200_OK)

    @action(methods=['put'], detail=True, url_path='place-order', url_name='place-order')
    def place_order(self, request, order_id=None):
        order = self.get_object()
        if order.check_done():
            order.cart.checkout = True
            order.cart.save()
        order.save()
        return Response(data={
            'orderId': order_id
        }, status=status.HTTP_200_OK)


class OrderCreateAPI(generics.RetrieveAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    lookup_url_kwarg = ['billing_profile', 'cart']
    serializer_class = OrderSerializer

    def get_object(self):
        billing_profile = self.kwargs['billing_profile']
        cart = self.kwargs['cart']
        obj, created = Order.objects.new_or_get(billing_profile=billing_profile, cart_obj=cart)
        return obj
