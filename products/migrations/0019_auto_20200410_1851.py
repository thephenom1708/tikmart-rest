# Generated by Django 3.0.4 on 2020-04-10 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0001_initial'),
        ('products', '0018_auto_20200405_0201'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='products', to='tags.Tag'),
        ),
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('footwear', 'FOOTWEAR'), ('clothing', 'CLOTHING'), ('automobile', 'AUTOMOBILE'), ('furniture', 'FURNITURE'), ('electronic', 'ELECTRONIC'), ('sports-equipment', 'SPORTS-EQUIPMENT'), ('book', 'BOOK')], max_length=50),
        ),
        migrations.AlterField(
            model_name='productattributename',
            name='type',
            field=models.CharField(blank=True, choices=[('footwear', 'FOOTWEAR'), ('clothing', 'CLOTHING'), ('automobile', 'AUTOMOBILE'), ('furniture', 'FURNITURE'), ('electronic', 'ELECTRONIC'), ('sports-equipment', 'SPORTS-EQUIPMENT'), ('book', 'BOOK')], max_length=50),
        ),
        migrations.AlterField(
            model_name='propertyname',
            name='type',
            field=models.CharField(blank=True, choices=[('footwear', 'FOOTWEAR'), ('clothing', 'CLOTHING'), ('automobile', 'AUTOMOBILE'), ('furniture', 'FURNITURE'), ('electronic', 'ELECTRONIC'), ('sports-equipment', 'SPORTS-EQUIPMENT'), ('book', 'BOOK')], max_length=50),
        ),
    ]
