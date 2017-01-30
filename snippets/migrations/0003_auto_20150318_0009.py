# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0002_remove_like_whether_like'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Like',
            new_name='ProductLike',
        ),
    ]
