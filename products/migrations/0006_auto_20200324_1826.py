# Generated by Django 3.0.4 on 2020-03-24 12:56

from django.db import migrations, models

import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20200324_1809'),
    ]

    operations = [
        migrations.CreateModel(
            name='FilterAttributeName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('type', models.CharField(blank=True, choices=[('footwear', 'FOOTWEAR'), ('clothing', 'CLOTHING'), ('automobile', 'AUTOMOBILE'), ('furniture', 'FURNITURE'), ('sports-equipment', 'SPORTS-EQUIPMENT'), ('book', 'BOOK')], max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='filterattribute',
            name='type',
        ),
        migrations.AlterField(
            model_name='product',
            name='filter_attributes',
            field=smart_selects.db_fields.ChainedManyToManyField(blank=True, chained_field='type', chained_model_field='attr.type', related_name='products', to='products.FilterAttribute'),
        ),
    ]
