# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0008_auto_20150512_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brandfeed',
            name='pub_date',
            field=models.DateTimeField(verbose_name='date published', default=datetime.datetime(2015, 5, 12, 7, 12, 32, 850904, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='issue',
            name='pub_date',
            field=models.DateTimeField(verbose_name='date published', default=datetime.datetime.now),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='product',
            name='pub_date',
            field=models.DateTimeField(verbose_name='date published', default=datetime.datetime(2015, 5, 12, 7, 12, 32, 867563, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
