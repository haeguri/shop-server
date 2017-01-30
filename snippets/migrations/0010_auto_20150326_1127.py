# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0009_auto_20150325_1729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cody',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 26, 11, 27, 50, 758644), verbose_name='date published'),
            preserve_default=True,
        ),
    ]
