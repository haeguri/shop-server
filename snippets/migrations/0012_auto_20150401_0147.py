# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import snippets.models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0011_auto_20150331_1131'),
    ]

    operations = [
        migrations.CreateModel(
            name='BrandInterview',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('image', models.ImageField(upload_to=snippets.models.BrandInterview.get_upload_path)),
                ('brand', models.ForeignKey(related_name='interviews', to='snippets.Brand')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='cody',
            name='pub_date',
            field=models.DateTimeField(verbose_name='date published', default=datetime.datetime(2015, 3, 31, 16, 47, 27, 828693, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=15, unique=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='product',
            name='pub_date',
            field=models.DateTimeField(verbose_name='date published', default=datetime.datetime(2015, 3, 31, 16, 47, 27, 807859, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
