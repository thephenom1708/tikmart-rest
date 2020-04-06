from decimal import Decimal

from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save, post_save, m2m_changed, post_delete

from carts.managers import CartManager
from products.models import ProductVariant

User = settings.AUTH_USER_MODEL


RETURN_STATUS_CHOICES = {
    ('NA', 'NA'),
    ('requested', 'REQUESTED'),
    ('initiated', 'INITIATED'),
    ('completed', 'COMPLETED')
}


class Cart(models.Model):
    user = models.ForeignKey(User, related_name='carts', null=True, blank=True, on_delete=models.CASCADE)
    products = models.ManyToManyField(ProductVariant, blank=True, related_name='carts', through='carts.CartProduct')
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
        for product_variant in products:
            cart_product = instance.cart_products.get(product_variant=product_variant)
            total += product_variant.product.price * cart_product.quantity
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


class CartProduct(models.Model):
    product_variant = models.ForeignKey(ProductVariant, on_delete=models.CASCADE, related_name='cart_products')
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_products')
    quantity = models.PositiveIntegerField(default=1)
    applied_for_return = models.BooleanField(default=False)
    return_status = models.CharField(max_length=100, choices=RETURN_STATUS_CHOICES, default='NA')

    def __str__(self):
        return str(self.id) + '--' + self.product_variant.name + '--' + str(self.cart.id)


def pre_save_cart_product_receiver(sender, instance, *args, **kwargs):
    old_instance = CartProduct.objects.filter(id=instance.id).first()
    if old_instance is not None:
        changed_quantity = instance.quantity - old_instance.quantity
        addition_amount = instance.product_variant.product.price * changed_quantity
    else:
        addition_amount = instance.product_variant.product.price * instance.quantity

    changed_total = instance.cart.subtotal + addition_amount
    if instance.cart.subtotal != changed_total:
        instance.cart.subtotal = changed_total
        instance.cart.save()


def post_delete_cart_product_receiver(sender, instance, *args, **kwargs):
    amount = instance.product_variant.product.price * instance.quantity

    changed_total = instance.cart.subtotal - amount
    if instance.cart.subtotal != changed_total:
        instance.cart.subtotal = changed_total
        instance.cart.save()


pre_save.connect(pre_save_cart_product_receiver, sender=CartProduct)
post_delete.connect(post_delete_cart_product_receiver, sender=CartProduct)
