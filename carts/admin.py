from django.contrib import admin

from .models import Cart, CartProduct


class CartProductInline(admin.TabularInline):
    model = CartProduct
    extra = 0


class CartAdmin(admin.ModelAdmin):
    inlines = [CartProductInline]
    list_display = ['id', 'user', 'checkout']
    list_filter = ['checkout', 'timestamp']
    search_fields = ['user__full_name', 'user__email']


admin.site.register(Cart, CartAdmin)
admin.site.register(CartProduct)
