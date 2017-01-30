# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import datetime


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminChannel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=30)),
                ('image', models.ImageField(upload_to='channel')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=20)),
                ('intro', models.TextField(blank=True, max_length=200)),
                ('image', models.ImageField(default='', upload_to='upload/brand')),
                ('background', models.ImageField(default='', blank=True, upload_to='upload/brand/background')),
                ('web', models.CharField(blank=True, max_length=50)),
                ('address', models.CharField(blank=True, max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BrandFollow',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('whether_follow', models.BooleanField(default=False)),
                ('brand', models.ForeignKey(related_name='brand_follows_of_brand', to='snippets.Brand')),
                ('user', models.ForeignKey(related_name='brand_follows_of_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('shipping', models.IntegerField(default=2500)),
                ('total_price', models.IntegerField(default=0)),
                ('address', models.TextField(max_length=100)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('size', models.CharField(null=True, max_length=10)),
                ('color', models.CharField(null=True, max_length=10)),
                ('quantity', models.IntegerField(null=True)),
                ('cart', models.ForeignKey(related_name='cart_items_of_cart', to='snippets.Cart')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('type', models.CharField(default='', max_length=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=30)),
                ('intro', models.TextField(max_length=200)),
                ('image', models.ImageField(upload_to='channel')),
                ('web', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('created', models.DateTimeField(verbose_name='date created', default=datetime.datetime.now)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ChannelFollow',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('whether_follow', models.BooleanField(default=False)),
                ('channel', models.ForeignKey(related_name='channel_follows_of_channel', to='snippets.Channel')),
                ('user', models.ForeignKey(related_name='channel_follows_of_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Cody',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('title', models.CharField(max_length=30)),
                ('desc', models.TextField(max_length=200)),
                ('image', models.ImageField(upload_to='channel/channel_cody')),
                ('pub_date', models.DateTimeField(verbose_name='date published', default=datetime.datetime.now)),
                ('channel', models.ForeignKey(related_name='codies_of_channel', to='snippets.Channel')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CodyCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(default='', max_length=20)),
                ('image', models.ImageField(default='', upload_to='upload/cody/category')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CodyItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('tip', models.CharField(max_length=50)),
                ('cody', models.ForeignKey(related_name='cody_items_of_cody', to='snippets.Cody')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CodyLike',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('whether_like', models.BooleanField(default=False)),
                ('cody', models.ForeignKey(related_name='cody_likes_of_cody', to='snippets.Cody')),
                ('user', models.ForeignKey(related_name='cody_likes_of_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('type', models.CharField(max_length=8)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('whether_like', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('pub_date', models.DateTimeField(verbose_name='date published', default=datetime.datetime.now)),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField(max_length=100)),
                ('price', models.IntegerField(default=0)),
                ('image', models.ImageField(upload_to='upload')),
                ('brand', models.ForeignKey(to='snippets.Brand', null=True, related_name='products_of_brand', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(default='', max_length=20)),
                ('category', models.ForeignKey(to='snippets.Category', null=True, related_name='tags_of_category', blank=True)),
                ('gender', models.ForeignKey(to='snippets.Gender', null=True, related_name='tags_of_gender', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('address', models.TextField(blank=True, max_length=200)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='product',
            name='tag',
            field=models.ForeignKey(to='snippets.Tag', null=True, related_name='products_of_tag', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='like',
            name='product',
            field=models.ForeignKey(related_name='likes_of_product', to='snippets.Product'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='like',
            name='user',
            field=models.ForeignKey(related_name='likes_of_user', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='codyitem',
            name='product',
            field=models.ForeignKey(related_name='cody_items_of_product', to='snippets.Product'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='codycategory',
            name='gender',
            field=models.ForeignKey(to='snippets.Gender', null=True, related_name='cody_categories_of_gender', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cody',
            name='cody_category',
            field=models.ForeignKey(to='snippets.CodyCategory', null=True, related_name='codies_of_cody_category', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='category',
            name='gender',
            field=models.ForeignKey(to='snippets.Gender', null=True, related_name='categories_of_gender', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cartitem',
            name='product',
            field=models.ForeignKey(related_name='cart_items_of_product', to='snippets.Product'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='brand',
            name='gender',
            field=models.ForeignKey(to='snippets.Gender', null=True, related_name='brands_of_gender', blank=True, max_length=5),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='brand',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
