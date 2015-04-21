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
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('introduce', models.TextField(max_length=200, blank=True)),
                ('image', models.ImageField(default='', upload_to='upload/brand')),
                ('background', models.ImageField(default='', upload_to='upload/brand/background')),
                ('web', models.URLField(blank=True)),
                ('address', models.CharField(max_length=200, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BrandFollow',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('brand', models.ForeignKey(related_name='brand_follows_of_brand', to='snippets.Brand', unique=True)),
                ('user', models.ForeignKey(related_name='brand_follows_of_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BrandInterview',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
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
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=30, unique=True)),
                ('introduce', models.TextField(max_length=200)),
                ('image', models.ImageField(upload_to='channel')),
                ('background', models.ImageField(default='', upload_to='channel/background')),
                ('web', models.URLField()),
                ('created', models.DateTimeField(verbose_name='date created', default=datetime.datetime.now)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ChannelFollow',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('channel', models.ForeignKey(related_name='channel_follows_of_channel', to='snippets.Channel', unique=True)),
                ('user', models.ForeignKey(related_name='channel_follows_of_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('type', models.CharField(max_length=8)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('title', models.CharField(max_length=20, unique=True)),
                ('description', models.TextField(max_length=200, default='')),
                ('image', models.ImageField(default='', upload_to='channel/channel_issue')),
                ('which_day', models.CharField(max_length=2, default='MO', choices=[('MO', 'Monday'), ('TU', 'Tuesday'), ('WE', 'Wednesday'), ('TH', 'Thursday'), ('FR', 'Friday'), ('SA', 'Saturday')])),
                ('pub_date', models.DateTimeField(verbose_name='date published', default=datetime.datetime(2015, 4, 21, 15, 31, 57, 629328, tzinfo=utc))),
                ('channel', models.ForeignKey(related_name='codies_of_channel', to='snippets.Channel')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='IssueItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
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
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('issue', models.ForeignKey(related_name='issue_likes_of_issue', to='snippets.Issue', unique=True)),
                ('user', models.ForeignKey(related_name='issue_likes_of_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('pub_date', models.DateTimeField(verbose_name='date published', default=datetime.datetime(2015, 4, 21, 15, 31, 57, 609023, tzinfo=utc))),
                ('name', models.CharField(max_length=15, unique=True)),
                ('description', models.TextField(max_length=100, default='')),
                ('price', models.IntegerField(default=0)),
                ('brand', models.ForeignKey(related_name='products_of_brand', to='snippets.Brand', blank=True, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('description', models.TextField(max_length=1000, default='', blank=True)),
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
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
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
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('type', models.CharField(max_length=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TestHashTag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=10, unique=True)),
            ],
            options={
                'ordering': ('category',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TestHashTagCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=10, unique=True)),
                ('is_required', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TestModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=10, unique=True)),
                ('hash_tags', models.ManyToManyField(to='snippets.TestHashTag')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('address', models.TextField(max_length=200, blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='testhashtag',
            name='category',
            field=models.ForeignKey(default='', to='snippets.TestHashTagCategory'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='issueitem',
            name='product',
            field=models.ForeignKey(related_name='issue_items_of_product', to='snippets.Product'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='brand',
            name='gender',
            field=models.ForeignKey(related_name='brands_of_gender', to='snippets.Gender', blank=True, max_length=5, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='brand',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
