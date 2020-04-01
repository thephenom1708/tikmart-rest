from django.db import models


class CartManager(models.Manager):
    def new_or_get(self, user):
        qs = self.get_queryset().filter(user=user, checkout=False)
        if qs.count() == 1:
            new_obj = False
            cart_obj = qs.first()
            # self.request.session['cart_items'] = cart_obj.products.count()
            if user.is_authenticated and cart_obj.user is None:
                cart_obj.user = user
                cart_obj.save()
        else:
            cart_obj = self.model.objects.new(user=user)
            new_obj = True
            # self.request.session['cart_id'] = cart_obj.id
            # self.request.session['cart_items'] = cart_obj.products.count()
        return cart_obj, new_obj

    def new(self, user=None):
        user_obj = None
        if user is not None:
            if user.is_authenticated:
                user_obj = user
        return self.model.objects.create(user=user_obj)
