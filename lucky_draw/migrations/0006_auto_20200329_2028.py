# Generated by Django 3.0.4 on 2020-03-29 14:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lucky_draw', '0005_auto_20200328_1753'),
    ]

    operations = [
        migrations.AddField(
            model_name='luckydraw',
            name='orders_from_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='luckydrawprofile',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lucky_draw_profiles', to=settings.AUTH_USER_MODEL),
        ),
    ]
