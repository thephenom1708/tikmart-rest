# Generated by Django 3.0.4 on 2020-04-10 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20200327_2102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('created', 'Created'), ('placed', 'Placed'), ('shipped', 'Shipped'), ('delivered', 'Delivered')], default='created', max_length=120),
        ),
    ]
