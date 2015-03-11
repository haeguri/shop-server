# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('snippets', '0016_auto_20150227_1003'),
    ]

    operations = [
        migrations.CreateModel(
            name='CodyFollow',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('whether_follow', models.BooleanField(default=False)),
                ('cody', models.ForeignKey(to='snippets.Cody', related_name='cody_follows_of_cody')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='cody_follows_of_user')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
