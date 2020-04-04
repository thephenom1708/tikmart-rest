from django.db import models
from django.conf import settings
from products.models import Product
from django.db.models.signals import post_save
from django.core.validators import MaxValueValidator, MinValueValidator

User = settings.AUTH_USER_MODEL


class Review(models.Model):
    product = models.ForeignKey(Product, null=True, related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='reviews', on_delete=models.CASCADE)
    rating = models.DecimalField(decimal_places=1, max_digits=5, default=0.0, validators=[
        MaxValueValidator(limit_value=5.0),
        MinValueValidator(limit_value=0.0)
    ])
    content = models.TextField(blank=True, null=True, max_length=1000)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.title + "--" + self.user.email + "--" + str(self.rating)


def review_post_save_receiver(sender, instance, *args, **kwargs):
    new_product_rating = instance.product.calculate_rating()
    print("\n\nRating: ", new_product_rating)
    instance.product.rating = new_product_rating
    instance.product.save()


post_save.connect(review_post_save_receiver, sender=Review)
