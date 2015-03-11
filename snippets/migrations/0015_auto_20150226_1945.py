# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0014_auto_20150226_1751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='tag',
            field=models.ForeignKey(related_name='products_of_tag', to='snippets.Tag'),
        ),
    ]
