from django_filters import FilterSet, filters

from products.models import Product, Property, ProductAttributeValue


class ProductFilter(FilterSet):
    categories = filters.CharFilter('type__name')
    properties = filters.CharFilter(method='filter_by_properties')
    attributes = filters.CharFilter(method='filter_by_attributes')
    brands = filters.CharFilter(method='filter_by_brands')

    class Meta:
        model = Product
        fields = ['title', 'brands', 'gender', 'properties', 'attributes']

    def filter_by_properties(self, queryset, name, value):
        property_ids = value.strip().split(",")
        properties = Property.objects.filter(id__in=property_ids)
        return queryset.filter(properties__in=properties).distinct()

    def filter_by_attributes(self, queryset, name, value):
        attribute_ids = value.strip().split(",")
        attribute_values = ProductAttributeValue.objects.filter(id__in=attribute_ids)
        return queryset.filter(attributes__values__in=attribute_values).distinct()

    def filter_by_brands(self, queryset, name, value):
        brand_names = value.strip().split(",")
        return queryset.filter(brand__in=brand_names).distinct()
