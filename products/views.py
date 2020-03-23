from rest_framework import viewsets, permissions

from products.models import Product
from products.serializers import ProductDetailSerializer


class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.AllowAny,
    ]
    serializer_class = ProductDetailSerializer
    queryset = Product.objects.all()
