# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0006_auto_20150512_1540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brandfeed',
            name='pub_date',
            field=models.DateTimeField(verbose_name='date published', default=datetime.datetime(2015, 5, 12, 6, 40, 28, 747389, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='product',
            name='pub_date',
            field=models.DateTimeField(verbose_name='date published', default=datetime.datetime(2015, 5, 12, 6, 40, 28, 763657, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
