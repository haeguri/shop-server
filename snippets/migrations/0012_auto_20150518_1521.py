# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0011_auto_20150518_1513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brandfeed',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 18, 6, 21, 8, 118858, tzinfo=utc), verbose_name='date published'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='product',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 18, 6, 21, 8, 135226, tzinfo=utc), verbose_name='date published'),
            preserve_default=True,
        ),
    ]
