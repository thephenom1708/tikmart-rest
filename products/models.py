from ckeditor.fields import RichTextField
from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save, m2m_changed
from django.urls import reverse
from django.db.models import Avg
from django.core.validators import MaxValueValidator, MinValueValidator

from carts.utils import generateAttributesHash
from products.managers import ProductManager, ProductVariantManager
from products.utils import upload_image_path
from smart_selects.db_fields import ChainedManyToManyField
from tikmart_rest.utils import unique_slug_generator

User = settings.AUTH_USER_MODEL

PRODUCT_TYPES = (
    ('footwear', 'FOOTWEAR'),
    ('clothing', 'CLOTHING'),
    ('automobile', 'AUTOMOBILE'),
    ('furniture', 'FURNITURE'),
    ('sports-equipment', 'SPORTS-EQUIPMENT'),
    ('book', 'BOOK'),
)

GENDER_CHOICES = (
    ('male', 'Male'), ('female', 'Female'), ('unisex', 'Unisex'), ('kid', 'Kid'), ('NA', 'NA')
)

VIEW_SELECTION_TYPES = (
    ('single-selection', 'Single Selection'), ('multiple-selection', 'Multiple Selection'), ('NA', 'NA')
)


class ProductAttributeName(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50, choices=PRODUCT_TYPES, blank=True)
    view_selection_type = models.CharField(max_length=100, choices=VIEW_SELECTION_TYPES, blank=True)

    def __str__(self):
        return self.type + "--" + self.name


class ProductAttributeValue(models.Model):
    attr = models.ForeignKey(ProductAttributeName, related_name="values", on_delete=models.CASCADE)
    value = models.CharField(max_length=100)

    def __str__(self):
        return self.attr.name + "--" + self.value


class ProductAttribute(models.Model):
    attr = models.ForeignKey(ProductAttributeName, on_delete=models.CASCADE)
    values = ChainedManyToManyField(
        ProductAttributeValue,
        chained_field="attr",
        chained_model_field="attr",
        horizontal=True,
        related_name='attributes'
    )

    def __str__(self):
        return self.attr.__str__()


class PropertyName(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50, choices=PRODUCT_TYPES, blank=True)
    view_selection_type = models.CharField(max_length=100, choices=VIEW_SELECTION_TYPES, blank=True)

    def __str__(self):
        return self.type + "--" + self.name


class Property(models.Model):
    attr = models.ForeignKey(PropertyName, related_name="filter_values", on_delete=models.CASCADE)
    value = models.CharField(max_length=100)

    def __str__(self):
        return str(self.attr.type) + "--" + self.attr.name + "--" + str(self.value)


class Product(models.Model):
    title = models.CharField(max_length=120)
    brand = models.CharField(max_length=100, blank=True)
    slug = models.SlugField(blank=True, unique=True)
    type = models.CharField(max_length=50, choices=PRODUCT_TYPES)
    gender = models.CharField(max_length=50, choices=GENDER_CHOICES, blank=True)
    description = RichTextField()
    rating = models.DecimalField(decimal_places=1, max_digits=5, default=0.0, validators=[
        MaxValueValidator(limit_value=5.0),
        MinValueValidator(limit_value=0.0)
    ])
    price = models.DecimalField(decimal_places=2, max_digits=20, default=100.00)
    properties = ChainedManyToManyField(
        Property, related_name='products', blank=True,
        chained_field="type",
        chained_model_field="attr__type",
        horizontal=True
    )
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    attributes = ChainedManyToManyField(
        ProductAttribute, related_name='products', blank=True,
        chained_field="type",
        chained_model_field="attr__type",
        horizontal=True,
    )
    featured = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = ProductManager()

    def get_absolute_url(self):
        return reverse("categories:" + str(self.type) + "_detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

    def url(self):
        return "/products/" + str(self.type) + "/" + str(self.slug) + "/"

    def product_properties(self):
        product_properties = ", ".join([prop.attr.name for prop in self.properties.all()])
        if product_properties == "":
            return "-------"
        else:
            return product_properties

    def product_attributes(self):
        product_attrs = ", ".join([attribute.attr.name for attribute in self.attributes.all()])
        if product_attrs == "":
            return "-------"
        else:
            return product_attrs

    def calculate_rating(self):
        rating = self.reviews.all().aggregate(Avg('rating'))['rating__avg'] or 0.0
        return rating

    @property
    def name(self):
        return self.title


def product_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(product_pre_save_receiver, sender=Product)


class ProductVariant(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_variants')
    hash = models.SlugField(max_length=100, blank=True)
    attributes = models.ManyToManyField(ProductAttributeValue)

    objects = ProductVariantManager()

    def __str__(self):
        return self.product.name

    @property
    def name(self):
        return self.product.title


def product_variant_m2m_changed_receiver(sender, instance, action, *args, **kwargs):
    if action == 'post_add' or action == 'post_remove' or action == 'post_save' or action == 'post_clear':
        attributes = instance.attributes.values_list('id', flat=True)
        instance.hash = generateAttributesHash(attributes)
        instance.save()


m2m_changed.connect(product_variant_m2m_changed_receiver, sender=ProductVariant.attributes.through)
