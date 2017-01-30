# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0006_auto_20150319_0554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='codylike',
            name='cody',
            field=models.ForeignKey(unique=True, related_name='cody_likes_of_cody', to='snippets.Cody'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='codylike',
            name='user',
            field=models.ForeignKey(related_name='cody_likes_of_user', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
