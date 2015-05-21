# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0014_auto_20150520_1425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date published', blank=True),
            preserve_default=True,
        ),
    ]
