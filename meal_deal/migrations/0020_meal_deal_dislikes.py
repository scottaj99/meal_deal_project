# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-21 12:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meal_deal', '0019_meal_deal_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='meal_deal',
            name='dislikes',
            field=models.IntegerField(default=0),
        ),
    ]