# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0011_auto_20150224_1932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channelfollow',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='channel_follows_of_user'),
        ),
    ]
