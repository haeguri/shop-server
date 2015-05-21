# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import snippets.models
from django.utils.timezone import utc
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
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('description', models.TextField(max_length=200, blank=True)),
                ('profile', models.ImageField(default='', upload_to='upload/brand')),
                ('background', models.ImageField(default='', upload_to='upload/brand/background')),
                ('web', models.URLField(blank=True)),
                ('address', models.CharField(max_length=200, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BrandFeed',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=20)),
                ('body', models.TextField(max_length=200, blank=True)),
                ('pub_date', models.DateTimeField(verbose_name='date published', default=datetime.datetime(2015, 5, 12, 6, 22, 50, 545432, tzinfo=utc))),
                ('image', models.ImageField(upload_to=snippets.models.BrandFeed.get_upload_path)),
                ('brand', models.ForeignKey(to='snippets.Brand', related_name='feeds')),
            ],
            options={
                'ordering': ('-pub_date',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BrandFollow',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('brand', models.ForeignKey(to='snippets.Brand', related_name='brand_follows_of_brand')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='brand_follows_of_user')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BrandInterview',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to=snippets.models.BrandInterview.get_upload_path)),
                ('brand', models.ForeignKey(to='snippets.Brand', related_name='interviews')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(unique=True, max_length=10)),
                ('brief', models.CharField(default='', max_length=10)),
                ('created', models.DateTimeField(verbose_name='date created', default=datetime.datetime.now)),
                ('introduce', models.TextField(max_length=200)),
                ('profile', models.ImageField(upload_to='channel')),
                ('background', models.ImageField(default='', upload_to='channel/background')),
                ('web', models.URLField(blank=True)),
                ('address', models.CharField(max_length=20, default='', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ChannelFollow',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('channel', models.ForeignKey(to='snippets.Channel', related_name='channel_follows_of_channel')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='channel_follows_of_user')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=8)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HashTag',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(unique=True, max_length=10)),
            ],
            options={
                'ordering': ('category',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HashTagCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(unique=True, max_length=10)),
                ('is_required', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('pub_date', models.DateTimeField(verbose_name='date published', default=datetime.datetime(2015, 5, 12, 6, 22, 50, 565832, tzinfo=utc))),
                ('title', models.CharField(unique=True, max_length=10)),
                ('description', models.TextField(default='', max_length=200)),
                ('image', models.ImageField(default='', upload_to='channel/channel_issue')),
                ('view', models.PositiveIntegerField(default=0)),
                ('channel', models.ForeignKey(to='snippets.Channel', related_name='issues_of_channel')),
                ('hash_tags', models.ManyToManyField(related_name='issues', to='snippets.HashTag')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='IssueItem',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('tip', models.CharField(max_length=50)),
                ('issue', models.ForeignKey(to='snippets.Issue', related_name='issue_items_of_issue')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='IssueLike',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('issue', models.ForeignKey(to='snippets.Issue', related_name='issue_likes_of_issue')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='issue_likes_of_user')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('pub_date', models.DateTimeField(verbose_name='date published', default=datetime.datetime(2015, 5, 12, 6, 22, 50, 561803, tzinfo=utc))),
                ('name', models.CharField(unique=True, max_length=15)),
                ('description', models.TextField(default='', max_length=100)),
                ('price', models.IntegerField(default=0)),
                ('brand', models.ForeignKey(related_name='products_of_brand', null=True, to='snippets.Brand', blank=True)),
                ('gender', models.ForeignKey(to='snippets.Gender', null=True)),
                ('hash_tags', models.ManyToManyField(related_name='products', to='snippets.HashTag')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('description', models.TextField(max_length=1000, default='', blank=True)),
                ('image', models.ImageField(upload_to=snippets.models.ProductImage.get_upload_path)),
                ('product', models.ForeignKey(to='snippets.Product', related_name='images')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProductLike',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('product', models.ForeignKey(to='snippets.Product', related_name='product_likes_of_product')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='product_likes_of_user')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PubDay',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('day', models.CharField(max_length=2, choices=[('월', '월요일'), ('화', '화요일'), ('수', '수요일'), ('목', '목요일'), ('금', '금요일'), ('토', '토요일')], blank=True, default='월')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='issueitem',
            name='product',
            field=models.ForeignKey(to='snippets.Product', related_name='issue_items_of_product'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='hashtag',
            name='category',
            field=models.ForeignKey(to='snippets.HashTagCategory'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='channel',
            name='pub_days',
            field=models.ManyToManyField(blank=True, to='snippets.PubDay'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='brand',
            name='gender',
            field=models.ForeignKey(related_name='brands_of_gender', null=True, to='snippets.Gender', blank=True, max_length=5),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='brand',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
