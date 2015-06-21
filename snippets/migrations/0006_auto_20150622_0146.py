# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0005_testcontent_body'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='testcontent',
            options={'ordering': ('id',)},
        ),
    ]
