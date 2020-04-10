from django.contrib import admin

from .forms import ProductForm
from .models import (
    ProductAttributeName,
    ProductAttributeValue,
    ProductAttribute,
    PropertyName,
    Property,
    Product,
    ProductVariant
)


class ProductAttributeNameAdmin(admin.ModelAdmin):
    class Meta:
        model = ProductAttributeName

    list_display = ['name', 'type', 'view_selection_type']
    list_filter = ['type', 'view_selection_type']


class ProductAttributeValueAdmin(admin.ModelAdmin):
    class Meta:
        model = ProductAttributeValue

    list_display = ['attr', 'value']
    list_filter = ['attr__type', 'attr__view_selection_type']
    search_fields = ['attr__name', 'value']


class ProductAttributeInline(admin.TabularInline):
    model = ProductAttribute.values.through
    extra = 0
    verbose_name = "Attribute Value"
    verbose_name_plural = "Attribute Values"


class ProductAttributeAdmin(admin.ModelAdmin):
    inlines = [ProductAttributeInline]
    fields = ['attr']


class PropertyNameAdmin(admin.ModelAdmin):
    class Meta:
        model = ProductAttributeName

    list_display = ['name', 'type', 'view_selection_type']
    list_filter = ['type', 'view_selection_type']


class PropertyInline(admin.TabularInline):
    model = Product.properties.through
    extra = 0
    verbose_name = "Property"
    verbose_name_plural = "Properties"


class PropertyAdmin(admin.ModelAdmin):
    class Meta:
        model = ProductAttributeValue

    list_display = ['attr', 'value']
    list_filter = ['attr__type', 'attr__view_selection_type']
    search_fields = ['attr__name', 'value']


class ProductAdmin(admin.ModelAdmin):
    class Meta:
        model = Product

    form = ProductForm
    inlines = [PropertyInline]
    list_display = ['title', 'brand', 'type', 'price', 'featured', 'product_properties', 'product_attributes']
    list_filter = ('type', 'properties', 'active', 'featured')
    fieldsets = (
        ('Product Details', {'fields': ('title', ('brand', 'type'), ('image', 'gender'), 'description')}),
        ('Customization', {'fields': ('attributes', )}),
        ('Activity and Pricing', {'fields': ('price', ('featured', 'active'), 'tags')}),
    )
    search_fields = ('title', 'brand', 'type', 'title', 'gender')
    ordering = ('title', 'brand', 'price', 'active', 'featured')
    filter_horizontal = ('properties', 'attributes', 'tags')


admin.site.register(ProductAttributeName, ProductAttributeNameAdmin)
admin.site.register(ProductAttributeValue, ProductAttributeValueAdmin)
admin.site.register(ProductAttribute, ProductAttributeAdmin)
admin.site.register(PropertyName, PropertyNameAdmin)
admin.site.register(Property, PropertyAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductVariant)
