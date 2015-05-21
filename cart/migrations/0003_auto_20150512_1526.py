# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_auto_20150512_1523'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='order',
        ),
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 12, 6, 26, 37, 337679, tzinfo=utc), verbose_name='주문일'),
            preserve_default=True,
        ),
    ]
