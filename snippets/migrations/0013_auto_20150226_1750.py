# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0012_auto_20150224_2033'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=20, null=True, blank=True)),
                ('category', models.ForeignKey(blank=True, related_name='tags_of_category', null=True, to='snippets.Category')),
                ('gender', models.ForeignKey(blank=True, related_name='tags_of_gender', null=True, to='snippets.Gender')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='category',
            name='name',
        ),
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.AddField(
            model_name='category',
            name='type',
            field=models.CharField(max_length=10, default=''),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='product',
            name='tag',
            field=models.ForeignKey(blank=True, related_name='products_of_tag', null=True, to='snippets.Tag'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='category',
            name='gender',
            field=models.ForeignKey(blank=True, related_name='categories_of_gender', null=True, to='snippets.Gender'),
        ),
    ]
