# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='nickname',
            field=models.CharField(validators=[django.core.validators.MinLengthValidator(4)], unique=True, max_length=20, verbose_name='별명'),
            preserve_default=True,
        ),
    ]
