# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-12 00:52
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('receipt', '0002_auto_20171109_2034'),
    ]

    operations = [
        migrations.AddField(
            model_name='receipt',
            name='tax',
            field=models.CharField(default=1, max_length=250),
        ),
        migrations.AlterField(
            model_name='receipt',
            name='date',
            field=models.DateField(default=datetime.datetime(2017, 11, 12, 0, 52, 44, 462726, tzinfo=utc)),
        ),
    ]
