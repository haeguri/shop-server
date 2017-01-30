# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0004_auto_20150318_1022'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='codycategory',
            name='image',
        ),
    ]
