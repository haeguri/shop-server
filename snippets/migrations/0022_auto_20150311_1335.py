# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0021_auto_20150310_2108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gender',
            name='type',
            field=models.CharField(max_length=8),
        ),
    ]
