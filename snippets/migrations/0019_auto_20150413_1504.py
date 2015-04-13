# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('snippets', '0018_auto_20150413_1240'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('address', models.TextField(max_length=200, blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='brand',
            name='intro',
            field=models.TextField(help_text="Means to 'Introduce'", max_length=200, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='category',
            name='type',
            field=models.CharField(help_text="Large categorization than the below 'tag' model", default='', max_length=10),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cody',
            name='pub_date',
            field=models.DateTimeField(verbose_name='date published', default=datetime.datetime(2015, 4, 13, 6, 4, 53, 640580, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='product',
            name='pub_date',
            field=models.DateTimeField(verbose_name='date published', default=datetime.datetime(2015, 4, 13, 6, 4, 53, 620333, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tag',
            name='slug',
            field=models.IntegerField(unique=True, help_text='Displayed depends on the order of priority, like Outer->Jeans->Bags', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tag',
            name='type',
            field=models.CharField(help_text="Smaller categorization than the above 'category' model", default='', max_length=20),
            preserve_default=True,
        ),
    ]
