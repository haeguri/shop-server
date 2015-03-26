# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0008_auto_20150320_1524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cody',
            name='title',
            field=models.CharField(max_length=15),
            preserve_default=True,
        ),
    ]
