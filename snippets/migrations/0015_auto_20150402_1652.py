# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0014_auto_20150402_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cody',
            name='pub_date',
            field=models.DateTimeField(verbose_name='date published', default=datetime.datetime(2015, 4, 2, 7, 52, 51, 850798, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='product',
            name='pub_date',
            field=models.DateTimeField(verbose_name='date published', default=datetime.datetime(2015, 4, 2, 7, 52, 51, 827898, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='productimage',
            name='description',
            field=models.TextField(max_length=500, null=True),
            preserve_default=True,
        ),
    ]
