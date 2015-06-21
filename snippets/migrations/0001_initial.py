# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import datetime
import django.utils.timezone
import snippets.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('email', models.EmailField(unique=True, verbose_name='이메일 주소', max_length=255)),
                ('nickname', models.CharField(unique=True, verbose_name='별명', max_length=20)),
                ('date_joined', models.DateTimeField(verbose_name='가입일', auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('description', models.TextField(blank=True, max_length=200)),
                ('profile', models.ImageField(upload_to='upload/brand', default='')),
                ('background', models.ImageField(upload_to='upload/brand/background', default='')),
                ('web', models.URLField(blank=True, verbose_name='웹 페이지')),
                ('address', models.CharField(blank=True, verbose_name='오프라인 주소', max_length=200)),
                ('designer', models.OneToOneField(verbose_name='디자이너', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BrandFollow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('brand', models.ForeignKey(related_name='brand_follows_of_brand', to='snippets.Brand')),
                ('user', models.ForeignKey(related_name='brand_follows_of_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BrandInterview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('image', models.ImageField()),
                ('brand', models.ForeignKey(related_name='interviews', to='snippets.Brand')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('brief', models.CharField(max_length=10)),
                ('created', models.DateTimeField(verbose_name='date created', auto_now_add=True)),
                ('introduce', models.TextField(max_length=200)),
                ('profile', models.ImageField(upload_to=snippets.models.Channel.get_profile_path)),
                ('background', models.ImageField(upload_to=snippets.models.Channel.get_background_path)),
                ('maker', models.OneToOneField(verbose_name='컨텐츠 제작자', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ChannelFollow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('channel', models.ForeignKey(related_name='channel_follows_of_channel', to='snippets.Channel')),
                ('user', models.ForeignKey(related_name='channel_follows_of_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('type', models.CharField(max_length=8)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HashTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
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
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
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
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('pub_date', models.DateTimeField(blank=True, default=datetime.datetime.now, verbose_name='date published')),
                ('title', models.CharField(unique=True, max_length=10)),
                ('description', models.TextField(default='', max_length=200)),
                ('image', models.ImageField(upload_to='channel/channel_issue', default='')),
                ('view', models.PositiveIntegerField(default=0)),
                ('channel', models.ForeignKey(related_name='issues_of_channel', to='snippets.Channel')),
                ('hash_tags', models.ManyToManyField(related_name='issues', to='snippets.HashTag')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='IssueItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
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
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('issue', models.ForeignKey(related_name='issue_likes_of_issue', to='snippets.Issue')),
                ('user', models.ForeignKey(related_name='issue_likes_of_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('pub_date', models.DateTimeField(blank=True, default=datetime.datetime.now, verbose_name='date published')),
                ('name', models.CharField(unique=True, max_length=15)),
                ('description', models.TextField(default='', max_length=100)),
                ('price', models.IntegerField(default=0)),
                ('brand', models.ForeignKey(blank=True, related_name='products_of_brand', null=True, to='snippets.Brand')),
                ('gender', models.ForeignKey(null=True, to='snippets.Gender')),
                ('hash_tags', models.ManyToManyField(related_name='products', to='snippets.HashTag')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
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
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('product', models.ForeignKey(related_name='product_likes_of_product', to='snippets.Product')),
                ('user', models.ForeignKey(related_name='product_likes_of_user', to=settings.AUTH_USER_MODEL)),
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
            field=models.ForeignKey(to='snippets.HashTagCategory'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='brand',
            name='gender',
            field=models.ForeignKey(verbose_name='디자인 타겟', max_length=5, blank=True, null=True, to='snippets.Gender', related_name='brands_of_gender'),
            preserve_default=True,
        ),
    ]
