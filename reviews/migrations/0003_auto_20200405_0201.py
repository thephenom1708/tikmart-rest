# Generated by Django 3.0.4 on 2020-04-04 20:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_auto_20200325_1806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.DecimalField(decimal_places=1, default=0.0, max_digits=5, validators=[django.core.validators.MaxValueValidator(limit_value=5.0), django.core.validators.MinValueValidator(limit_value=0.0)]),
        ),
    ]