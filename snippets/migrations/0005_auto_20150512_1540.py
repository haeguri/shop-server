# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0004_auto_20150512_1540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brandfeed',
            name='pub_date',
            field=models.DateTimeField(verbose_name='date published', default=datetime.datetime(2015, 5, 12, 6, 40, 20, 957547, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='product',
            name='pub_date',
            field=models.DateTimeField(verbose_name='date published', default=datetime.datetime(2015, 5, 12, 6, 40, 20, 976876, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
