from django.db import models
from django.conf import settings
from products.models import Product

User = settings.AUTH_USER_MODEL


class Review(models.Model):
    product = models.ForeignKey(Product, null=True, related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='reviews', on_delete=models.CASCADE)
    rating = models.IntegerField(default=3, blank=True, null=True)
    content = models.TextField(blank=True, null=True, max_length=1000)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.title + "--" + self.user.email + "--" + str(self.rating)
