# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0005_auto_20150216_2107'),
    ]

    operations = [
        migrations.AddField(
            model_name='channel',
            name='created',
            field=models.DateTimeField(verbose_name='date created', default=datetime.datetime.now),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cody',
            name='pub_date',
            field=models.DateTimeField(verbose_name='date published', default=datetime.datetime.now),
            preserve_default=True,
        ),
    ]
