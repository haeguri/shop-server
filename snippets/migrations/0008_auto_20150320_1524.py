# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0007_auto_20150319_0555'),
    ]

    operations = [
        migrations.AddField(
            model_name='channel',
            name='background',
            field=models.ImageField(upload_to='channel/background', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='brandfollow',
            name='brand',
            field=models.ForeignKey(to='snippets.Brand', related_name='brand_follows_of_brand', unique=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='channelfollow',
            name='channel',
            field=models.ForeignKey(to='snippets.Channel', related_name='channel_follows_of_channel', unique=True),
            preserve_default=True,
        ),
    ]
