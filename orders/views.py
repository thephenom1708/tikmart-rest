from rest_framework import viewsets, permissions, status, generics
from rest_framework.decorators import action
from rest_framework.response import Response

from addresses.models import Address
from carts.models import Cart, CartProduct
from orders.serializers import OrderSerializer, OrderDetailSerializer
from orders.models import Order


class OrderViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.AllowAny,
    ]
    lookup_field = 'order_id'
    serializer_class = OrderDetailSerializer

    def get_queryset(self):
        # return self.request.user.billingprofile.orders.filter(active=True)
        return Order.objects.filter(active=True)

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
        order.payment_method = request.data.get('paymentMethod')
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
            order.status = "placed"
            order.cart.save()
        order.save()
        return Response(data={
            'orderId': order_id
        }, status=status.HTTP_200_OK)

    @action(methods=['put'], detail=True,
            url_path='return-product-request/(?P<cart_product_id>[0-9a-z]+)',
            url_name='return-product-request')
    def return_product_request(self, request, cart_product_id, order_id=None):
        cart_product = CartProduct.objects.get(id=cart_product_id)
        cart_product.applied_for_return = True
        cart_product.return_status = 'requested'
        cart_product.save()
        return Response(data={
            'orderId': order_id
        }, status=status.HTTP_200_OK)

    @action(methods=['put'], detail=True,
            url_path='return-product-initiate/(?P<cart_product_id>[0-9a-z]+)',
            url_name='return-product-initiate')
    def return_product_initiate(self, request, cart_product_id, order_id=None):
        cart_product = CartProduct.objects.get(id=cart_product_id)
        cart_product.return_status = 'initiated'
        cart_product.save()
        return Response(data={
            'orderId': order_id
        }, status=status.HTTP_200_OK)

    @action(methods=['put'], detail=True,
            url_path='return-product-completed/(?P<cart_product_id>[0-9a-z]+)',
            url_name='return-product-completed')
    def return_product_completed(self, request, cart_product_id, order_id=None):
        cart_product = CartProduct.objects.get(id=cart_product_id)
        cart_product.return_status = 'completed'
        cart_product.save()
        return Response(data={
            'orderId': order_id
        }, status=status.HTTP_200_OK)


class OrderCreateAPI(generics.RetrieveAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    lookup_url_kwarg = ['cart']
    serializer_class = OrderSerializer

    def get_object(self):
        cart_id = self.kwargs['cart']
        cart_obj = Cart.objects.get(id=cart_id)
        billing_profile = self.request.user.billingprofile
        obj, created = Order.objects.new_or_get(billing_profile=billing_profile, cart_obj=cart_obj)
        return obj


class OrderHistoryAPI(generics.ListAPIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = OrderDetailSerializer

    def get_queryset(self):
        self.request.user.billingprofile.orders.filter(active=True)

    def list(self, request, *args, **kwargs):
        qs = self.request.user.billingprofile.orders.filter(active=True).exclude(status="created")
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)
