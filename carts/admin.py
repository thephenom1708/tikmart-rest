from django.contrib import admin


from .models import Cart, FootwareInCart, ClothingInCart, AutomobileInCart, FurnitureInCart, BookInCart, SportsEquipmentInCart

admin.site.register(Cart)
admin.site.register(FootwareInCart)
admin.site.register(ClothingInCart)
admin.site.register(AutomobileInCart)
admin.site.register(FurnitureInCart)
admin.site.register(SportsEquipmentInCart)
admin.site.register(BookInCart)
