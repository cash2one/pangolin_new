# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-11-21 21:33
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_auto_20161121_2029'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name=b'Category')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name=b'Name')),
                ('slug', models.CharField(blank=True, max_length=250, verbose_name=b'Url pic')),
                ('text1', ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name=b'Text1')),
                ('text2', ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name=b'Text2')),
                ('published', models.BooleanField(verbose_name=b'Published')),
                ('published_main', models.BooleanField(default=b'', verbose_name=b'Published on main')),
                ('ordering', models.IntegerField(blank=True, default=0, null=True, verbose_name=b'Ordering')),
                ('category', mptt.fields.TreeForeignKey(blank=True, default=b'', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='slides', to='content.Category', verbose_name=b'Category')),
            ],
            options={
                'verbose_name': 'Slide',
                'verbose_name_plural': 'Slides',
            },
        ),
    ]
