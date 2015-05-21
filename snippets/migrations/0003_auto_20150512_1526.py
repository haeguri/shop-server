# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0002_auto_20150512_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brandfeed',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 12, 6, 26, 31, 124248, tzinfo=utc), verbose_name='date published'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='issue',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 12, 6, 26, 31, 144728, tzinfo=utc), verbose_name='date published'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='product',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 12, 6, 26, 31, 140802, tzinfo=utc), verbose_name='date published'),
            preserve_default=True,
        ),
    ]
