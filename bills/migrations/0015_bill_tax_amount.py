# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-03 08:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bills', '0014_bill_sale_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='bill',
            name='tax_amount',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
