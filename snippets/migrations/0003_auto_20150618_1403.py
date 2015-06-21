# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0002_auto_20150611_1447'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='brand',
            name='designer',
        ),
        migrations.RemoveField(
            model_name='brand',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='brandfollow',
            name='brand',
        ),
        migrations.RemoveField(
            model_name='brandfollow',
            name='user',
        ),
        migrations.DeleteModel(
            name='BrandFollow',
        ),
        migrations.RemoveField(
            model_name='brandinterview',
            name='brand',
        ),
        migrations.DeleteModel(
            name='BrandInterview',
        ),
        migrations.RemoveField(
            model_name='product',
            name='brand',
        ),
        migrations.DeleteModel(
            name='Brand',
        ),
    ]
