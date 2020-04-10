from django.contrib import admin

from .models import Order


class OrderAdmin(admin.ModelAdmin):
    date_hierarchy = 'timestamp'
    list_display = ('order_id', 'get_products', 'products_to_return', 'total', 'paid')
    list_filter = ('payment_method', 'status', 'paid', 'timestamp', 'active',)
    fieldsets = (
        ('Order', {'fields': ('order_id', ('cart', 'status'))}),
        ('Billing Profile Details', {'fields': ('billing_profile', ('shipping_address', 'billing_address'))}),
        ('Activity and Pricing', {'fields': (('shipping_total', 'total'), ('payment_method', 'paid'), 'active')}),
    )
    search_fields = ('order_id', 'billing_profile__email', 'payment_method', 'status', 'timestamp')
    ordering = ('total', 'timestamp')
    filter_horizontal = ()

    def get_products(self, obj):
        products = ", ".join([product.name for product in obj.products()])
        if len(products):
            return products
        else:
            return "---"
    get_products.short_description = "Products"

    def products_to_return(self, obj):
        products = ", ".join([product.name for product in obj.products().filter(applied_for_return=True)])
        if len(products):
            return products
        else:
            return "---"
    products_to_return.short_description = "Products To Return"


admin.site.register(Order, OrderAdmin)
