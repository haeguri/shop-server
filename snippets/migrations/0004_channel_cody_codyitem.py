# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0003_auto_20150216_2028'),
    ]

    operations = [
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=30)),
                ('intro', models.TextField(max_length=200)),
                ('image', models.ImageField(upload_to='channel')),
                ('web', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Cody',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=30)),
                ('desc', models.TextField(max_length=200)),
                ('image', models.ImageField(upload_to='channel/channel_cody')),
                ('channel', models.ForeignKey(related_name='codies_of_channel', to='snippets.Channel')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CodyItem',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('tip', models.CharField(max_length=50)),
                ('cody', models.ForeignKey(related_name='cody_items_of_cody', to='snippets.Cody')),
                ('product', models.ForeignKey(related_name='cody_items_of_product', to='snippets.Product')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
