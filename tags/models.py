from django.db import models

from products.choices import PRODUCT_TYPES


class Tag(models.Model):
    title = models.CharField(max_length=120)
    type = models.CharField(max_length=50, choices=PRODUCT_TYPES)

    def __str__(self):
        return str(self.title)

    @property
    def name(self):
        return str(self.title)
