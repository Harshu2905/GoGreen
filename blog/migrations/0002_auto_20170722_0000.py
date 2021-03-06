# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-21 18:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(default='', null=True),
        ),
        migrations.AlterField(
            model_name='like',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='blog.Article'),
        ),
    ]
