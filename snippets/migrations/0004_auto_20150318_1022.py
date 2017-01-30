# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0003_auto_20150318_0009'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='brandfollow',
            name='whether_follow',
        ),
        migrations.RemoveField(
            model_name='channelfollow',
            name='whether_follow',
        ),
        migrations.RemoveField(
            model_name='codylike',
            name='whether_like',
        ),
        migrations.AlterField(
            model_name='productlike',
            name='product',
            field=models.ForeignKey(related_name='product_likes_of_product', to='snippets.Product'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='productlike',
            name='user',
            field=models.ForeignKey(related_name='product_likes_of_user', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
