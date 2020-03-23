from django.contrib import admin

from .models import Product, ProductInCart, Review


class ProductAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'slug']

    class Meta:
        model = Product


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductInCart)
admin.site.register(Review)

# admin.site.register(Car)