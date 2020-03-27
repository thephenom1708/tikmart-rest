# Generated by Django 3.0.4 on 2020-03-24 12:11

from django.db import migrations, models

import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20200324_1726'),
    ]

    operations = [
        migrations.AddField(
            model_name='productattribute',
            name='type',
            field=models.CharField(blank=True, choices=[('footwear', 'FOOTWEAR'), ('clothing', 'CLOTHING'), ('automobile', 'AUTOMOBILE'), ('furniture', 'FURNITURE'), ('sports-equipment', 'SPORTS-EQUIPMENT'), ('book', 'BOOK')], max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='attributes',
            field=smart_selects.db_fields.ChainedManyToManyField(blank=True, chained_field='type', chained_model_field='type', horizontal=True, related_name='products', to='products.ProductAttribute'),
        ),
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('footwear', 'FOOTWEAR'), ('clothing', 'CLOTHING'), ('automobile', 'AUTOMOBILE'), ('furniture', 'FURNITURE'), ('sports-equipment', 'SPORTS-EQUIPMENT'), ('book', 'BOOK')], max_length=50),
        ),
    ]