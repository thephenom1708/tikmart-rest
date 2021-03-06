from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions, generics
from rest_framework.filters import SearchFilter, OrderingFilter

from products.filters import ProductFilter
from products.models import Product
from products.serializers import ProductDetailSerializer, ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.AllowAny,
    ]
    lookup_field = 'slug'
    serializer_class = ProductSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filter_class = ProductFilter
    ordering_fields = ['price', 'timestamp', 'featured']
    ordering = ['title', 'price']
    search_fields = ['title', 'type', 'brand', 'properties__value']

    def get_queryset(self):
        product_type = self.kwargs['product_type']
        tag_id = self.request.query_params.get('tag')
        if tag_id:
            lookups = Q(tags__id=tag_id)
            return Product.objects.filter(type=product_type, active=True).filter(lookups).distinct()
        return Product.objects.filter(type=product_type, active=True)


class ProductDetailViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.AllowAny,
    ]
    serializer_class = ProductDetailSerializer
    queryset = Product.objects.all()


class FeaturedProductsAPI(generics.ListAPIView):
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ProductSerializer

    def get_queryset(self):
        product_type = self.kwargs['product_type']
        return Product.objects.filter(type=product_type, active=True, featured=True)
