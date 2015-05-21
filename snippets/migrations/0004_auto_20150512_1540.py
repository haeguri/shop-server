# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0003_auto_20150512_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brandfeed',
            name='pub_date',
            field=models.DateTimeField(verbose_name='date published'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='issue',
            name='pub_date',
            field=models.DateTimeField(verbose_name='date published'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='product',
            name='pub_date',
            field=models.DateTimeField(verbose_name='date published'),
            preserve_default=True,
        ),
    ]
