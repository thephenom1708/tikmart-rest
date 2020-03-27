from django.contrib import admin

from .models import Order


class OrderAdmin(admin.ModelAdmin):
    date_hierarchy = 'timestamp'
    list_display = (
        'order_id', 'billing_profile', 'payment_method', 'status', 'total', 'timestamp', 'paid')
    list_filter = ('payment_method', 'status', 'paid', 'timestamp', 'active',)
    fieldsets = (
        ('Order', {'fields': ('order_id', ('cart', 'status'))}),
        ('Billing Profile Details', {'fields': ('billing_profile', ('shipping_address', 'billing_address'))}),
        ('Activity and Pricing', {'fields': (('shipping_total', 'total'), ('payment_method', 'paid'), 'active')}),
    )
    search_fields = ('order_id', 'billing_profile__email', 'payment_method', 'status', 'timestamp')
    ordering = ('payment_method', 'status', 'shipping_total', 'total', 'timestamp', 'paid')
    filter_horizontal = ()

    def get_products(self, obj):
        return "\n".join([o.title for o in obj.cart.products.all()])


admin.site.register(Order, OrderAdmin)
