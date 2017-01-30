# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0005_remove_codycategory_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='codylike',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='cody_likes_of_user', unique=True),
            preserve_default=True,
        ),
    ]
