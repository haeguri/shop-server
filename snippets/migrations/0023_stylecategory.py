# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0022_auto_20150311_1335'),
    ]

    operations = [
        migrations.CreateModel(
            name='StyleCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default='', max_length=20)),
                ('gender', models.ForeignKey(null=True, related_name='tags_if_gender', to='snippets.Gender', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
