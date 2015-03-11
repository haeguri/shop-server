# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('snippets', '0010_auto_20150222_1527'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChannelFollow',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('whether_follow', models.BooleanField(default=False)),
                ('channel', models.ForeignKey(related_name='channel_follows_of_channel', to='snippets.Channel')),
                ('user', models.ForeignKey(related_name='user_follows_of_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='testitem',
            name='test',
        ),
        migrations.DeleteModel(
            name='Test',
        ),
        migrations.RemoveField(
            model_name='testitem',
            name='test_cart',
        ),
        migrations.DeleteModel(
            name='TestCart',
        ),
        migrations.DeleteModel(
            name='TestItem',
        ),
        migrations.AlterField(
            model_name='designerfollow',
            name='designer',
            field=models.ForeignKey(related_name='designer_follows of_designer', to='snippets.Designer'),
        ),
    ]
