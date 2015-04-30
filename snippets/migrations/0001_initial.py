# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import snippets.models
from django.conf import settings
import datetime


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=20)),
                ('introduce', models.TextField(blank=True, max_length=200)),
                ('profile', models.ImageField(default='', upload_to='upload/brand')),
                ('background', models.ImageField(default='', upload_to='upload/brand/background')),
                ('web', models.URLField(blank=True)),
                ('address', models.CharField(blank=True, max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BrandFollow',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('brand', models.ForeignKey(related_name='brand_follows_of_brand', unique=True, to='snippets.Brand')),
                ('user', models.ForeignKey(related_name='brand_follows_of_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
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
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=10, unique=True)),
                ('which_day', models.CharField(default='MO', choices=[('MO', 'Monday'), ('TU', 'Tuesday'), ('WE', 'Wednesday'), ('TH', 'Thursday'), ('FR', 'Friday'), ('SA', 'Saturday')], max_length=2)),
                ('created', models.DateTimeField(default=datetime.datetime.now, verbose_name='date created')),
                ('introduce', models.TextField(max_length=200)),
                ('profile', models.ImageField(upload_to='channel')),
                ('background', models.ImageField(default='', upload_to='channel/background')),
                ('web', models.URLField(blank=True)),
                ('address', models.CharField(default='', blank=True, max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ChannelFollow',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('channel', models.ForeignKey(related_name='channel_follows_of_channel', unique=True, to='snippets.Channel')),
                ('user', models.ForeignKey(related_name='channel_follows_of_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('type', models.CharField(max_length=8)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HashTag',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=10, unique=True)),
            ],
            options={
                'ordering': ('category',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HashTagCategory',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=10, unique=True)),
                ('is_required', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('pub_date', models.DateTimeField(default=datetime.datetime(2015, 4, 24, 10, 55, 24, 902604, tzinfo=utc), verbose_name='date published')),
                ('title', models.CharField(max_length=10, unique=True)),
                ('description', models.TextField(default='', max_length=200)),
                ('image', models.ImageField(default='', upload_to='channel/channel_issue')),
                ('view', models.PositiveIntegerField(default=0)),
                ('channel', models.ForeignKey(related_name='issues_of_channel', to='snippets.Channel')),
                ('hash_tags', models.ManyToManyField(to='snippets.HashTag')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='IssueItem',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('tip', models.CharField(max_length=50)),
                ('issue', models.ForeignKey(related_name='issue_items_of_issue', to='snippets.Issue')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='IssueLike',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('issue', models.ForeignKey(related_name='issue_likes_of_issue', unique=True, to='snippets.Issue')),
                ('user', models.ForeignKey(related_name='issue_likes_of_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('pub_date', models.DateTimeField(default=datetime.datetime(2015, 4, 24, 10, 55, 24, 884206, tzinfo=utc), verbose_name='date published')),
                ('name', models.CharField(max_length=15, unique=True)),
                ('description', models.TextField(default='', max_length=100)),
                ('price', models.IntegerField(default=0)),
                ('brand', models.ForeignKey(related_name='products_of_brand', blank=True, to='snippets.Brand', null=True)),
                ('gender', models.ForeignKey(to='snippets.Gender', null=True)),
                ('hash_tags', models.ManyToManyField(to='snippets.HashTag')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('description', models.TextField(default='', blank=True, max_length=1000)),
                ('image', models.ImageField(upload_to=snippets.models.ProductImage.get_upload_path)),
                ('product', models.ForeignKey(related_name='images', to='snippets.Product')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProductLike',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('product', models.ForeignKey(related_name='product_likes_of_product', to='snippets.Product')),
                ('user', models.ForeignKey(related_name='product_likes_of_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProductSort',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('type', models.CharField(max_length=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='issueitem',
            name='product',
            field=models.ForeignKey(related_name='issue_items_of_product', to='snippets.Product'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='hashtag',
            name='category',
            field=models.ForeignKey(default='', to='snippets.HashTagCategory'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='brand',
            name='gender',
            field=models.ForeignKey(related_name='brands_of_gender', max_length=5, blank=True, to='snippets.Gender', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='brand',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
