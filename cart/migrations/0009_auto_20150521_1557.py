# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0008_auto_20150521_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateTimeField(verbose_name='주문일', default=datetime.datetime(2015, 5, 21, 6, 57, 36, 355742, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
