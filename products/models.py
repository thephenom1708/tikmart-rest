import random
import os
from ckeditor.fields import RichTextField
from django.conf import settings
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db.models import Q
from django.db.models.signals import pre_save, post_save, post_delete
from django.urls import reverse

from tikmart_rest.utils import unique_slug_generator

User = settings.AUTH_USER_MODEL


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    new_filename = random.randint(1, 3910209312)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "products/{new_filename}/{final_filename}".format(
        new_filename=new_filename,
        final_filename=final_filename
    )


class ProductQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)

    def featured(self):
        return self.filter(featured=True, active=True)

    def search(self, query):
        lookups = (Q(title__icontains=query) |
                   Q(description__icontains=query) |
                   Q(price__icontains=query) |
                   Q(tag__title__icontains=query)
                   )
        # tshirt, t-shirt, t shirt, red, green, blue,
        return self.filter(lookups).distinct()


class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset().active()

    def featured(self):  # Product.objects.featured()
        return self.get_queryset().featured()

    def get_by_id(self, id):
        qs = self.get_queryset().filter(id=id)  # Product.objects == self.get_queryset()
        if qs.count() == 1:
            return qs.first()
        return None

    def search(self, query):
        return self.get_queryset().active().search(query)


class Product(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(blank=True, unique=True)
    description = RichTextField()
    price = models.DecimalField(decimal_places=2, max_digits=20, default=39.99)
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    featured = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    content_type = models.ForeignKey(ContentType, blank=True, null=True, on_delete=models.CASCADE)

    # class Meta:
    #    abstract = True

    objects = ProductManager()

    def get_absolute_url(self):
        return reverse("categories:" + self.content_type.model + "_detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

    def url(self):
        if self.content_type.model == 'footware':
            return "/products/" + "footwear" + "/" + self.slug + "/"
        return "/products/" + self.content_type.model + "/" + self.slug + "/"

    @property
    def name(self):
        return self.title


def product_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(product_pre_save_receiver, sender=Product)


class ProductInCart(models.Model):
    product_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    product_id = models.PositiveIntegerField()
    product_object = GenericForeignKey('product_type', 'product_id')
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.product_object.title)


def product_in_cart_post_delete_receiver(sender, instance, *args, **kwargs):
    product_type = instance.product_type
    product_class = product_type.model_class()
    product_id = instance.product_id

    product_class.objects.get(id=product_id).delete()
    print('Deleted in cart product')


post_delete.connect(product_in_cart_post_delete_receiver, sender=ProductInCart)




