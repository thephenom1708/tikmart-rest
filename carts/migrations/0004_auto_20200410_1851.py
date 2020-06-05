# Generated by Django 3.0.4 on 2020-04-10 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0003_auto_20200406_1940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartproduct',
            name='return_status',
            field=models.CharField(choices=[('requested', 'REQUESTED'), ('completed', 'COMPLETED'), ('NA', 'NA'), ('initiated', 'INITIATED')], default='NA', max_length=100),
        ),
    ]