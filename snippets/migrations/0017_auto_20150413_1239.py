# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0016_auto_20150402_1653'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
        migrations.AlterField(
            model_name='cody',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 13, 3, 39, 44, 672227, tzinfo=utc), verbose_name='date published'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='product',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 13, 3, 39, 44, 652327, tzinfo=utc), verbose_name='date published'),
            preserve_default=True,
        ),
    ]
