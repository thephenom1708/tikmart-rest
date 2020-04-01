from django.conf import settings
from django.db import models

from products.models import Product

User = settings.AUTH_USER_MODEL


class WishlistManager(models.Manager):
    def new_or_get(self, user):
        qs = self.get_queryset().filter(user=user)
        if qs.count() == 1:
            new_obj = False
            wishlist_obj = qs.first()
            if user.is_authenticated and wishlist_obj.user is None:
                wishlist_obj.user = user
                wishlist_obj.save()
        else:
            wishlist_obj = Wishlist.objects.new(user=user)
            new_obj = True
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
