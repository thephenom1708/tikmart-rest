from django.conf import settings
from django.db import models

from products.models import Product

User = settings.AUTH_USER_MODEL


class WishlistManager(models.Manager):
    def new_or_get(self, request):
        qs = self.get_queryset().filter(user=request.user)
        if qs.count() == 1:
            new_obj = False
            wishlist_obj = qs.first()
            request.session['wishlist_items_count'] = wishlist_obj.products.count()
            if request.user.is_authenticated and wishlist_obj.user is None:
                wishlist_obj.user = request.user
                wishlist_obj.save()
        else:
            wishlist_obj = Wishlist.objects.new(user=request.user)
            new_obj = True
            request.session['wishlist_id'] = wishlist_obj.id
            request.session['wishlist_items_count'] = wishlist_obj.products.count()
        return wishlist_obj, new_obj

    def new(self, user=None):
        user_obj = None
        if user is not None:
            if user.is_authenticated:
                user_obj = user
        return self.model.objects.create(user=user_obj)


class Wishlist(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, blank=True)

    objects = WishlistManager()

    def __str__(self):
        return str(self.id)
