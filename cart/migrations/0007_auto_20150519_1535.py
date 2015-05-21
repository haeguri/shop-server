# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0006_auto_20150512_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 19, 6, 35, 18, 448418, tzinfo=utc), verbose_name='주문일'),
            preserve_default=True,
        ),
    ]
