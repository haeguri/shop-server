# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0015_auto_20150402_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cody',
            name='pub_date',
            field=models.DateTimeField(verbose_name='date published', default=datetime.datetime(2015, 4, 2, 7, 53, 27, 916655, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(max_length=1000),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='product',
            name='pub_date',
            field=models.DateTimeField(verbose_name='date published', default=datetime.datetime(2015, 4, 2, 7, 53, 27, 893712, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='productimage',
            name='description',
            field=models.TextField(null=True, max_length=1000),
            preserve_default=True,
        ),
    ]
