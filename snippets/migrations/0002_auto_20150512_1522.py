# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brandfeed',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 12, 6, 22, 56, 764894, tzinfo=utc), verbose_name='date published'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='issue',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 12, 6, 22, 56, 785268, tzinfo=utc), verbose_name='date published'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='product',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 12, 6, 22, 56, 781438, tzinfo=utc), verbose_name='date published'),
            preserve_default=True,
        ),
    ]
