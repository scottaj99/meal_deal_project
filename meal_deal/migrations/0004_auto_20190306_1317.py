# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-06 13:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meal_deal', '0003_auto_20190305_1930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
