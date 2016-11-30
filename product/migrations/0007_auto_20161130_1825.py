# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-11-30 18:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_auto_20161130_1641'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menuitemproduct',
            name='product',
        ),
        migrations.AddField(
            model_name='menuitemproduct',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.Category', verbose_name=b'Category'),
        ),
    ]
