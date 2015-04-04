# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0004_auto_20150330_2142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cody',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 30, 21, 59, 30, 681322), verbose_name='date published'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='product',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 30, 21, 59, 30, 677995), verbose_name='date published'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tag',
            name='slug',
            field=models.IntegerField(null=True, unique=True),
            preserve_default=True,
        ),
    ]
