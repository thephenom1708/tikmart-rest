from rest_framework import generics, status
from rest_framework import permissions
from rest_framework.response import Response

from carts.models import Cart, CartProduct
from carts.serializers import CartSerializer, CartProductSerializer
from products.models import ProductVariant, ProductAttributeValue, Product


class CartAPI(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = CartSerializer

    def get_object(self):
        cart, created = Cart.objects.new_or_get(user=self.request.user)
        return cart

    def update(self, request, *args, **kwargs):
        cart = self.get_object()
        product_id = request.data.get('product')
        attribute_ids = request.data.get('attributes')

        product = Product.objects.get(id=product_id)
        attr_count = product.attributes.count()

        if attr_count == len(attribute_ids):
            attributes = ProductAttributeValue.objects.filter(id__in=attribute_ids)

            product_variant, created = ProductVariant.objects.new_or_get(product=product, attributes=attributes)
            cart.products.add(product_variant)
            return Response({
                'product_variant_id': product_variant.id
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                'status': 406
            }, status=status.HTTP_406_NOT_ACCEPTABLE)

    def delete(self, request, *args, **kwargs):
        cart_product_id = request.data.get('cartProduct')
        CartProduct.objects.get(id=cart_product_id).delete()

        return Response({
            'status': 200
        }, status=status.HTTP_200_OK)


class CartProductAPI(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    lookup_field = 'id'
    serializer_class = CartProductSerializer
    queryset = CartProduct.objects.all()

    def update(self, request, *args, **kwargs):
        cart_product = self.get_object()
        cart_product.quantity = request.data.get('quantity')
        cart_product.save()

        return Response(status=status.HTTP_200_OK)
