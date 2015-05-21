# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_auto_20150512_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateTimeField(verbose_name='주문일', default=datetime.datetime(2015, 5, 12, 6, 27, 26, 635678, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
