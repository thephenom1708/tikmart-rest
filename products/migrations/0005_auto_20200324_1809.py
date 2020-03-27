# Generated by Django 3.0.4 on 2020-03-24 12:39

import django.db.models.deletion
from django.db import migrations, models

import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20200324_1741'),
    ]

    operations = [
        migrations.CreateModel(
            name='FilterAttribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=100)),
                ('type', models.CharField(blank=True, choices=[('footwear', 'FOOTWEAR'), ('clothing', 'CLOTHING'), ('automobile', 'AUTOMOBILE'), ('furniture', 'FURNITURE'), ('sports-equipment', 'SPORTS-EQUIPMENT'), ('book', 'BOOK')], max_length=50)),
                ('attr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='filter_values', to='products.ProductAttributeName')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='filter_attributes',
            field=smart_selects.db_fields.ChainedManyToManyField(blank=True, chained_field='type', chained_model_field='type', related_name='products', to='products.FilterAttribute'),
        ),
    ]