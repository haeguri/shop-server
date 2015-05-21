# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0005_auto_20150512_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 12, 6, 27, 33, 477605, tzinfo=utc), verbose_name='주문일'),
            preserve_default=True,
        ),
    ]
