from django.db import models


class CartManager(models.Manager):
    def new_or_get(self, request):
        qs = self.get_queryset().filter(user=request.user, checkout=False)
        if qs.count() == 1:
            new_obj = False
            cart_obj = qs.first()
            request.session['cart_items'] = cart_obj.products.count()
            if request.user.is_authenticated and cart_obj.user is None:
                cart_obj.user = request.user
                cart_obj.save()
        else:
            cart_obj = self.model.objects.new(user=request.user)
            new_obj = True
            request.session['cart_id'] = cart_obj.id
            request.session['cart_items'] = cart_obj.products.count()
        return cart_obj, new_obj

    def new(self, user=None):
        user_obj = None
        if user is not None:
            if user.is_authenticated:
                user_obj = user
        return self.model.objects.create(user=user_obj)
