# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0023_stylecategory'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stylecategory',
            name='gender',
        ),
        migrations.DeleteModel(
            name='StyleCategory',
        ),
    ]
