# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-11-30 16:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_menuitemproduct'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='menuitemproduct',
            options={'ordering': ['ordering'], 'verbose_name': 'Menu Item', 'verbose_name_plural': 'Menu Items for Products'},
        ),
    ]
