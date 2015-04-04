# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cody',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 30, 20, 2, 11, 251566), verbose_name='date published'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='product',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 30, 20, 2, 11, 248423), verbose_name='date published'),
            preserve_default=True,
        ),
    ]
