from django.contrib import admin

from wishlist.models import Wishlist


class WishlistProductInline(admin.TabularInline):
    model = Wishlist.products.through
    extra = 0
    verbose_name = "Product"
    verbose_name_plural = "Wishlist Products"


class WishlistAdmin(admin.ModelAdmin):
    inlines = [WishlistProductInline]
    exclude = ['products']
    list_display = ['id', 'user']
    search_fields = ['user__email', 'user__full_name']


admin.site.register(Wishlist, WishlistAdmin)
