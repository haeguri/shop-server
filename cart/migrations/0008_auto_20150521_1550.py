# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0007_auto_20150519_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 21, 6, 50, 15, 348949, tzinfo=utc), verbose_name='주문일'),
            preserve_default=True,
        ),
    ]
