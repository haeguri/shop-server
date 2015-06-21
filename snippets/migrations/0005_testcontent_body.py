# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0004_testcontent'),
    ]

    operations = [
        migrations.AddField(
            model_name='testcontent',
            name='body',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
    ]
