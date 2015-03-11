# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0002_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cody',
            name='channel',
        ),
        migrations.DeleteModel(
            name='Channel',
        ),
        migrations.RemoveField(
            model_name='codyitem',
            name='cody',
        ),
        migrations.DeleteModel(
            name='Cody',
        ),
        migrations.RemoveField(
            model_name='codyitem',
            name='product',
        ),
        migrations.DeleteModel(
            name='CodyItem',
        ),
    ]
