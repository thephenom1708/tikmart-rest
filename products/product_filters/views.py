from rest_framework import generics, permissions

from products.models import Property, ProductAttribute
from products.product_filters.serializers import ProductFiltersSerializer


class ProductFilters(object):
    def __init__(self, properties, attributes):
        self.properties = properties
        self.attributes = attributes


class ProductFiltersRetrieveAPI(generics.RetrieveAPIView):
    permission_classes = [
        permissions.AllowAny,
    ]
    serializer_class = ProductFiltersSerializer

    def get_object(self):
        product_type = self.kwargs['product_type']
        print("hetrrrrrrr", product_type)
        properties = Property.objects.filter(attr__type=product_type)
        attributes = ProductAttribute.objects.filter(attr__type=product_type)
        return ProductFilters(properties=properties, attributes=attributes)