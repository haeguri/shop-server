# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0015_auto_20150520_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='pub_date',
            field=models.DateTimeField(blank=True, verbose_name='date published', default=datetime.datetime.now),
            preserve_default=True,
        ),
    ]
