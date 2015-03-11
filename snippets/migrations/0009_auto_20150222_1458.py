# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0008_auto_20150222_1442'),
    ]

    operations = [
        migrations.AddField(
            model_name='testitem',
            name='name',
            field=models.CharField(blank=True, max_length=10, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='testitem',
            name='test',
            field=models.ForeignKey(to='snippets.Test', related_name='test_items_of_test'),
        ),
    ]
