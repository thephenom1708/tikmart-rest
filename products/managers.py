from django.db import models
from django.db.models import Q

from carts.utils import generateAttributesHash


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


class ProductVariantManager(models.Manager):
    def new_or_get(self, product, attributes):
        created = False

        attribute_ids = attributes.values_list('id', flat=True)
        attribute_hash = generateAttributesHash(attribute_ids)

        qs = self.get_queryset().filter(hash=attribute_hash)
        if qs.count() == 1:
            obj = qs.first()
        else:
            obj = self.model.objects.create(product=product)
            obj.attributes.add(*attributes)
            created = True
        return obj, created
