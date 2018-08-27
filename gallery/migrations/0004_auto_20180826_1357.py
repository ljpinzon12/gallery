# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-26 18:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0003_auto_20180819_1053'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='media',
            name='created',
        ),
        migrations.AlterField(
            model_name='media',
            name='mediaType',
            field=models.CharField(choices=[('V', 'VIDEO'), ('A', 'AUDIO')], default='V', max_length=10),
        ),
    ]