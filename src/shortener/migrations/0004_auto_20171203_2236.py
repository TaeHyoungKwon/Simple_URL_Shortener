# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-03 13:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0003_shortenurl_is_public'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hitupdatedtime',
            name='clicked_user',
        ),
        migrations.RemoveField(
            model_name='shortenurl',
            name='owner',
        ),
    ]
