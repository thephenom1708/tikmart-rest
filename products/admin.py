from django.contrib import admin

from .models import (
    ProductAttributeName,
    ProductAttributeValue,
    ProductAttribute,
    PropertyName,
    Property,
    Product,
    ProductVariant
)


class ProductAdmin(admin.ModelAdmin):
    class Meta:
        model = Product

    list_display = ['title', 'brand', 'type', 'price', 'featured', 'product_properties', 'product_attributes']
    list_filter = ('type', 'properties', 'active', 'featured')

    search_fields = ('title', 'brand', 'type', 'title', 'gender')
    ordering = ('title', 'brand', 'price', 'active', 'featured')
    filter_horizontal = ('properties', 'attributes')


admin.site.register(ProductAttributeName)
admin.site.register(ProductAttributeValue)
admin.site.register(ProductAttribute)
admin.site.register(PropertyName)
admin.site.register(Property)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductVariant)
