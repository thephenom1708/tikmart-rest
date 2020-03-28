from django.db import models
from django.conf import settings
from accounts.models import User as UserModel
from django.db.models.signals import pre_save, post_save
from django.db.models import Sum

User = settings.AUTH_USER_MODEL


class LuckyDraw(models.Model):
    users = models.ManyToManyField(User, blank=True, related_name='lucky_draws', through='lucky_draw.LuckyDrawProfile')
    winner = models.ForeignKey(User, null=True, blank=True, related_name='winning_lucky_draws', on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    order_amount_limit = models.DecimalField(max_digits=20, decimal_places=2, default=100.0)
    created_on = models.DateTimeField(auto_now_add=True)
    finished_on = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return str(self.id) + '---' + str(self.created_on)


def pre_save_lucky_draw_receiver(sender, instance, *args, **kwargs):
    LuckyDraw.objects.filter(active=True).update(active=False)


pre_save.connect(pre_save_lucky_draw_receiver, sender=LuckyDraw)


def post_save_lucky_draw_receiver(sender, instance, *args, **kwargs):
    for user in UserModel.objects.filter(active=True):
        user_carts_sum = user.carts.filter(checkout=True).aggregate(Sum('subtotal'))['subtotal__sum'] or 0
        if user_carts_sum >= instance.order_amount_limit:
            LuckyDrawProfile.objects.get_or_create(user=user, lucky_draw=instance, order_amount=user_carts_sum)
        else:
            LuckyDrawProfile.objects.filter(user=user, lucky_draw=instance).delete()


post_save.connect(post_save_lucky_draw_receiver, sender=LuckyDraw)


class LuckyDrawProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='lucky_draw_profiles')
    lucky_draw = models.ForeignKey(LuckyDraw, on_delete=models.CASCADE, related_name='lucky_draw_profiles')
    participated = models.BooleanField(default=False)
    order_amount = models.DecimalField(max_digits=20, decimal_places=2, default=0.0)

    def __str__(self):
        return self.user.email
