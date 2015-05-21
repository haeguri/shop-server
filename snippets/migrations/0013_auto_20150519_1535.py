# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0012_auto_20150518_1521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brandfeed',
            name='pub_date',
            field=models.DateTimeField(verbose_name='date published'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='channel',
            name='created',
            field=models.DateTimeField(verbose_name='date created'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='issue',
            name='pub_date',
            field=models.DateTimeField(verbose_name='date published'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='product',
            name='pub_date',
            field=models.DateTimeField(verbose_name='date published'),
            preserve_default=True,
        ),
    ]
