# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-07-18 21:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='full_name',
            field=models.CharField(max_length=50),
        ),
    ]
