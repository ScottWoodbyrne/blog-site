# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-04 10:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20160729_1349'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='cancel_at_period_end',
            field=models.CharField(default='flase', max_length=5),
        ),
    ]
