# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0019_auto_20150310_1139'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='codyfollow',
            name='whether_follow',
        ),
        migrations.AddField(
            model_name='codyfollow',
            name='whether_like',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
