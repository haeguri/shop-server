# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0013_auto_20150519_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brandfeed',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='date published', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='channel',
            name='created',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='date created', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='issue',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='date published', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='product',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='date published', blank=True),
            preserve_default=True,
        ),
    ]
