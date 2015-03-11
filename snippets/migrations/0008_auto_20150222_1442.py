# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0007_auto_20150222_1438'),
    ]

    operations = [
        migrations.RenameField(
            model_name='testitem',
            old_name='item',
            new_name='test',
        ),
    ]
