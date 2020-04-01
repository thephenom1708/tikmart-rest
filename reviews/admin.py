from django.contrib import admin

# Register your models here.
from reviews.models import Review


class ReviewAdmin(admin.ModelAdmin):
    class Meta:
        model = Review

    list_display = ['product', 'user', 'rating']
    list_filter = ['product__type']


admin.site.register(Review, ReviewAdmin)
