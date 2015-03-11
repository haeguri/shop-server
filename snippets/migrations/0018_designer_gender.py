# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0017_codyfollow'),
    ]

    operations = [
        migrations.AddField(
            model_name='designer',
            name='gender',
            field=models.ForeignKey(blank=True, related_name='designers_of_gender', null=True, to='snippets.Gender', max_length=5),
            preserve_default=True,
        ),
    ]
