# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('snippets', '0020_auto_20150310_2101'),
    ]

    operations = [
        migrations.CreateModel(
            name='CodyLike',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('whether_like', models.BooleanField(default=False)),
                ('cody', models.ForeignKey(to='snippets.Cody', related_name='cody_likes_of_cody')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='cody_likes_of_user')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='codyfollow',
            name='cody',
        ),
        migrations.RemoveField(
            model_name='codyfollow',
            name='user',
        ),
        migrations.DeleteModel(
            name='CodyFollow',
        ),
    ]
