# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0006_auto_20150622_0146'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='testcontent',
            options={'ordering': ['-id']},
        ),
    ]
