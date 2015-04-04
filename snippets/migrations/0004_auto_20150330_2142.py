# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0003_auto_20150330_2022'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='slug',
            field=models.IntegerField(null=True, blank=True, unique=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cody',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 30, 21, 41, 59, 896916), verbose_name='date published'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(null=True, blank=True, upload_to='upload'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='product',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 30, 21, 41, 59, 893854), verbose_name='date published'),
            preserve_default=True,
        ),
    ]
