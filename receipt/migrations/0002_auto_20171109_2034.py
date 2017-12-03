# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-09 20:34
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('receipt', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='receipt',
            name='date',
            field=models.DateField(default=datetime.datetime(2017, 11, 9, 20, 34, 53, 415028, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='receipt',
            name='text',
            field=models.TextField(default=1),
        ),
        migrations.AddField(
            model_name='receipt',
            name='total',
            field=models.CharField(default=1, max_length=250),
        ),
    ]