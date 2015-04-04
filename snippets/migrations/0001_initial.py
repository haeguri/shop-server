# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import snippets.models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminChannel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
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
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('intro', models.TextField(max_length=200, blank=True)),
                ('image', models.ImageField(upload_to='upload/brand', default='')),
                ('background', models.ImageField(upload_to='upload/brand/background', default='', blank=True)),
                ('web', models.CharField(max_length=50, blank=True)),
                ('address', models.CharField(max_length=200, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BrandFollow',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('brand', models.ForeignKey(unique=True, to='snippets.Brand', related_name='brand_follows_of_brand')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='brand_follows_of_user')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
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
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('size', models.CharField(max_length=10, null=True)),
                ('color', models.CharField(max_length=10, null=True)),
                ('quantity', models.IntegerField(null=True)),
                ('cart', models.ForeignKey(to='snippets.Cart', related_name='cart_items_of_cart')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('type', models.CharField(max_length=10, default='')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('intro', models.TextField(max_length=200)),
                ('image', models.ImageField(upload_to='channel')),
                ('background', models.ImageField(upload_to='channel/background', null=True, blank=True)),
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
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('channel', models.ForeignKey(unique=True, to='snippets.Channel', related_name='channel_follows_of_channel')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='channel_follows_of_user')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Cody',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=20)),
                ('desc', models.TextField(max_length=200)),
                ('image', models.ImageField(upload_to='channel/channel_cody')),
                ('pub_date', models.DateTimeField(verbose_name='date published', default=datetime.datetime(2015, 3, 30, 20, 1, 59, 214722))),
                ('channel', models.ForeignKey(to='snippets.Channel', related_name='codies_of_channel')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CodyCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=20, default='')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CodyItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('tip', models.CharField(max_length=50)),
                ('cody', models.ForeignKey(to='snippets.Cody', related_name='cody_items_of_cody')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CodyLike',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('cody', models.ForeignKey(unique=True, to='snippets.Cody', related_name='cody_likes_of_cody')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='cody_likes_of_user')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('type', models.CharField(max_length=8)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('pub_date', models.DateTimeField(verbose_name='date published', default=datetime.datetime(2015, 3, 30, 20, 1, 59, 211597))),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField(max_length=100)),
                ('price', models.IntegerField(default=0)),
                ('image', models.ImageField(upload_to='upload')),
                ('brand', models.ForeignKey(blank=True, to='snippets.Brand', null=True, related_name='products_of_brand')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
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
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('product', models.ForeignKey(to='snippets.Product', related_name='product_likes_of_product')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='product_likes_of_user')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProductSort',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('type', models.CharField(max_length=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('type', models.CharField(max_length=20, default='')),
                ('category', models.ForeignKey(blank=True, to='snippets.Category', null=True, related_name='tags_of_category')),
                ('gender', models.ForeignKey(blank=True, to='snippets.Gender', null=True, related_name='tags_of_gender')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('address', models.TextField(max_length=200, blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='product',
            name='tag',
            field=models.ForeignKey(blank=True, to='snippets.Tag', null=True, related_name='products_of_tag'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='codyitem',
            name='product',
            field=models.ForeignKey(to='snippets.Product', related_name='cody_items_of_product'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='codycategory',
            name='gender',
            field=models.ForeignKey(blank=True, to='snippets.Gender', null=True, related_name='cody_categories_of_gender'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cody',
            name='cody_category',
            field=models.ForeignKey(blank=True, to='snippets.CodyCategory', null=True, related_name='codies_of_cody_category'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='category',
            name='gender',
            field=models.ForeignKey(blank=True, to='snippets.Gender', null=True, related_name='categories_of_gender'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cartitem',
            name='product',
            field=models.ForeignKey(to='snippets.Product', related_name='cart_items_of_product'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='brand',
            name='gender',
            field=models.ForeignKey(blank=True, to='snippets.Gender', max_length=5, null=True, related_name='brands_of_gender'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='brand',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
