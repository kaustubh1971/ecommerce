# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2019-01-10 13:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0010_product_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('slug', models.SlugField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
                ('products', models.ManyToManyField(blank=True, to='products.Product')),
            ],
        ),
    ]
