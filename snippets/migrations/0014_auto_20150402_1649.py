# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0013_auto_20150401_0148'),
    ]

    operations = [
        migrations.AddField(
            model_name='productimage',
            name='description',
            field=models.TextField(null=True, max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cody',
            name='pub_date',
            field=models.DateTimeField(verbose_name='date published', default=datetime.datetime(2015, 4, 2, 7, 49, 11, 312377, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(max_length=500),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='product',
            name='pub_date',
            field=models.DateTimeField(verbose_name='date published', default=datetime.datetime(2015, 4, 2, 7, 49, 11, 293107, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
