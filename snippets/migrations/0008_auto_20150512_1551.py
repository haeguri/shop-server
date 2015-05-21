# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0007_auto_20150512_1540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brandfeed',
            name='pub_date',
            field=models.DateTimeField(verbose_name='date published', default=datetime.datetime(2015, 5, 12, 6, 51, 28, 721332, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='issue',
            name='pub_date',
            field=models.DateTimeField(verbose_name='date published', auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='product',
            name='pub_date',
            field=models.DateTimeField(verbose_name='date published', default=datetime.datetime(2015, 5, 12, 6, 51, 28, 737690, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
