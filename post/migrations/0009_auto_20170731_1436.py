# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-31 14:36
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0008_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='draft',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='post',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 31, 14, 36, 57, 208996, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
