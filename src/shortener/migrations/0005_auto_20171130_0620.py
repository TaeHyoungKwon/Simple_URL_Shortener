# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-29 21:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0004_shortenurl_hit'),
    ]

    operations = [
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hit', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='shortenurl',
            name='hit',
        ),
        migrations.AddField(
            model_name='information',
            name='shorten_url',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='shortener.ShortenURL'),
        ),
    ]
