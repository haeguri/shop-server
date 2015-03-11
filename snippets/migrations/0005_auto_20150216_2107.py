# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0004_channel_cody_codyitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='test',
            name='product',
        ),
        migrations.DeleteModel(
            name='Test',
        ),
    ]
