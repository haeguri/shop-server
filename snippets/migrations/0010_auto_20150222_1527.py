# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0009_auto_20150222_1458'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestCart',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='testitem',
            name='test_cart',
            field=models.ForeignKey(blank=True, to='snippets.TestCart', null=True, related_name='test_items_of_test_cart'),
            preserve_default=True,
        ),
    ]
