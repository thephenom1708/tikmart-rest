from decimal import Decimal
from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save, post_save, m2m_changed

from products.models import Product, ProductInCart

from choices.models import Color
from choices.models import FootwareSize, FootwareCategory
from choices.models import ClothingSize, ClothingCategory, ClothingOccasion
from choices.models import AutomobileType
from choices.models import Sport
from choices.models import Author, Publisher, Language, BookGenere

User = settings.AUTH_USER_MODEL


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
            cart_obj = Cart.objects.new(user=request.user)
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


class Cart(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    products = models.ManyToManyField(ProductInCart, blank=True)
    subtotal = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    total = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    checkout = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = CartManager()

    def __str__(self):
        return str(self.id)


def m2m_changed_cart_receiver(sender, instance, action, *args, **kwargs):
    if action == 'post_add' or action == 'post_remove' or action == 'post_save' or action == 'post_clear':
        products = instance.products.all()
        total = 0
        for x in products:
            total += x.product_object.price * x.quantity
        if instance.subtotal != total:
            instance.subtotal = total
            instance.save()


m2m_changed.connect(m2m_changed_cart_receiver, sender=Cart.products.through)


def pre_save_cart_receiver(sender, instance, *args, **kwargs):
    if instance.subtotal > 0:
        instance.total = Decimal(instance.subtotal) * Decimal(1.08)  # 8% tax
    else:
        instance.total = 0.00


pre_save.connect(pre_save_cart_receiver, sender=Cart)


class FootwareInCart(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=20, default=1.00)
    brand = models.CharField(max_length=100, blank=True, null=True)
    size = models.ForeignKey(FootwareSize, blank=True, null=True, on_delete=models.SET_NULL)
    color = models.ForeignKey(Color, blank=True, null=True, on_delete=models.SET_NULL)
    gender = models.CharField(max_length=50, blank=True, null=True)
    type = models.ForeignKey(FootwareCategory, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return str(self.id) + '--' + str(self.title) + "--" + str(self.brand)

    def compare(self, obj):
        excluded_keys = 'id', '_state'  # Example. Modify to your likings.
        return self._compare(self, obj, excluded_keys)

    def _compare(self, obj1, obj2, excluded_keys):
        d1, d2 = obj1.__dict__, obj2.__dict__
        old, new = {}, {}
        for k, v in d1.items():
            if k in excluded_keys:
                continue
            try:
                if v != d2[k]:
                    old.update({k: v})
                    new.update({k: d2[k]})
            except KeyError:
                old.update({k: v})
        return old, new


class ClothingInCart(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=20, default=1.00)
    brand = models.CharField(max_length=100, blank=True, null=True)
    category = models.ForeignKey(ClothingCategory, blank=True, null=True, on_delete=models.SET_NULL)
    type = models.CharField(max_length=100, blank=True, null=True)
    sleeve = models.CharField(max_length=50, blank=True, null=True)
    size = models.ForeignKey(ClothingSize, blank=True, null=True, on_delete=models.SET_NULL)
    color = models.ForeignKey(Color, blank=True, null=True, on_delete=models.SET_NULL)
    gender = models.CharField(max_length=50, blank=True, null=True)
    occasion = models.ForeignKey(ClothingOccasion, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title + "--" + self.brand

    def compare(self, obj):
        excluded_keys = 'id', '_state'  # Example. Modify to your likings.
        return self._compare(self, obj, excluded_keys)

    def _compare(self, obj1, obj2, excluded_keys):
        d1, d2 = obj1.__dict__, obj2.__dict__
        old, new = {}, {}
        for k, v in d1.items():
            if k in excluded_keys:
                continue
            try:
                if v != d2[k]:
                    old.update({k: v})
                    new.update({k: d2[k]})
            except KeyError:
                old.update({k: v})
        return old, new


class AutomobileInCart(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=20, default=1.00)
    brand = models.CharField(max_length=100, blank=True, null=True)
    type = models.ForeignKey(AutomobileType, blank=True, null=True, on_delete=models.SET_NULL)
    colors = models.ForeignKey(Color, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title + "--" + self.brand

    def compare(self, obj):
        excluded_keys = 'id', '_state'  # Example. Modify to your likings.
        return self._compare(self, obj, excluded_keys)

    def _compare(self, obj1, obj2, excluded_keys):
        d1, d2 = obj1.__dict__, obj2.__dict__
        old, new = {}, {}
        for k, v in d1.items():
            if k in excluded_keys:
                continue
            try:
                if v != d2[k]:
                    old.update({k: v})
                    new.update({k: d2[k]})
            except KeyError:
                old.update({k: v})
        return old, new


class ElectronicInCart(models.Model):
    pass


class FurnitureInCart(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=20, default=1.00)
    brand = models.CharField(max_length=100, blank=True, null=True)
    material = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.title + "--" + self.brand

    def compare(self, obj):
        excluded_keys = 'id', '_state'  # Example. Modify to your likings.
        return self._compare(self, obj, excluded_keys)

    def _compare(self, obj1, obj2, excluded_keys):
        d1, d2 = obj1.__dict__, obj2.__dict__
        old, new = {}, {}
        for k, v in d1.items():
            if k in excluded_keys:
                continue
            try:
                if v != d2[k]:
                    old.update({k: v})
                    new.update({k: d2[k]})
            except KeyError:
                old.update({k: v})
        return old, new


class SportsEquipmentInCart(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=20, default=1.00)
    brand = models.CharField(max_length=100, blank=True, null=True)
    related_sport = models.ForeignKey(Sport, blank=True, null=True, on_delete=models.SET_NULL)
    weight = models.CharField(max_length=100, blank=True, null=True)
    material = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.title + "--" + self.brand

    def compare(self, obj):
        excluded_keys = 'id', '_state'  # Example. Modify to your likings.
        return self._compare(self, obj, excluded_keys)

    def _compare(self, obj1, obj2, excluded_keys):
        d1, d2 = obj1.__dict__, obj2.__dict__
        old, new = {}, {}
        for k, v in d1.items():
            if k in excluded_keys:
                continue
            try:
                if v != d2[k]:
                    old.update({k: v})
                    new.update({k: d2[k]})
            except KeyError:
                old.update({k: v})
        return old, new


class BookInCart(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=20, default=1.00)
    author = models.ForeignKey(Author, blank=True, null=True, on_delete=models.SET_NULL)
    language = models.ForeignKey(Language, blank=True, null=True, on_delete=models.SET_NULL)
    genre = models.ManyToManyField(BookGenere, blank=True)
    publisher = models.ForeignKey(Publisher, blank=True, null=True, on_delete=models.SET_NULL)
    edition = models.CharField(max_length=100, blank=True, null=True)
    no_of_pages = models.IntegerField(blank=True, null=True)


    def __str__(self):
        return self.title + "--" + self.author

    def compare(self, obj):
        excluded_keys = 'id', '_state'  # Example. Modify to your likings.
        return self._compare(self, obj, excluded_keys)

    def _compare(self, obj1, obj2, excluded_keys):
        d1, d2 = obj1.__dict__, obj2.__dict__
        old, new = {}, {}
        for k, v in d1.items():
            if k in excluded_keys:
                continue
            try:
                if v != d2[k]:
                    old.update({k: v})
                    new.update({k: d2[k]})
            except KeyError:
                old.update({k: v})
        return old, new
