# Generated by Django 3.0.4 on 2020-04-10 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('type', models.CharField(choices=[('footwear', 'FOOTWEAR'), ('clothing', 'CLOTHING'), ('automobile', 'AUTOMOBILE'), ('furniture', 'FURNITURE'), ('electronic', 'ELECTRONIC'), ('sports-equipment', 'SPORTS-EQUIPMENT'), ('book', 'BOOK')], max_length=50)),
            ],
        ),
    ]
