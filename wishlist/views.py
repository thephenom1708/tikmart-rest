from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from products.models import Product
from .serializers import WishlistSerializer
from wishlist.models import Wishlist


class WishlistViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    lookup_field = 'user'
    serializer_class = WishlistSerializer

    def get_queryset(self):
        # return self.request.user.wishlist
        return Wishlist.objects.all()

    @action(methods=['put'], detail=True, url_path='add-to-wishlist', url_name='add_to_wishlist')
    def add_to_wishlist(self, request, user=None):
        wishlist = self.get_object()
        product_to_add_id = request.data.get('product')
        product = Product.objects.get(id=product_to_add_id)
        wishlist.products.add(product)
        return Response(data={
            'id': product.id
        }, status=status.HTTP_200_OK)

    @action(methods=['put'], detail=True, url_path='remove-from-wishlist', url_name='remove_from_wishlist')
    def remove_from_wishlist(self, request, user=None):
        wishlist = self.get_object()
        product_to_remove_id = request.data.get('product')
        product = Product.objects.get(id=product_to_remove_id)
        wishlist.products.remove(product)
        return Response(data={
            'id': product.id
        }, status=status.HTTP_200_OK)
