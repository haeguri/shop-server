# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0024_auto_20150311_2056'),
    ]

    operations = [
        migrations.CreateModel(
            name='CodyCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=20, default='')),
                ('image', models.ImageField(upload_to='upload/cody/category', default='')),
                ('gender', models.ForeignKey(null=True, to='snippets.Gender', blank=True, related_name='cody_categories_of_gender')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='cody',
            name='cody_category',
            field=models.ForeignKey(null=True, to='snippets.CodyCategory', blank=True, related_name='codies_of_cody_category'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='designer',
            name='background',
            field=models.ImageField(upload_to='upload/designer/background', default=''),
            preserve_default=True,
        ),
    ]
