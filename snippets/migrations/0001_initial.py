# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime
import snippets.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('introduce', models.TextField(max_length=200, blank=True)),
                ('image', models.ImageField(upload_to='upload/brand', default='')),
                ('background', models.ImageField(upload_to='upload/brand/background', default='')),
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
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('brand', models.ForeignKey(to='snippets.Brand', unique=True, related_name='brand_follows_of_brand')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='brand_follows_of_user')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BrandInterview',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=snippets.models.BrandInterview.get_upload_path)),
                ('brand', models.ForeignKey(to='snippets.Brand', related_name='interviews')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
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
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
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
            name='Channel',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('introduce', models.TextField(max_length=200)),
                ('image', models.ImageField(upload_to='channel')),
                ('background', models.ImageField(upload_to='channel/background', default='')),
                ('web', models.URLField()),
                ('created', models.DateTimeField(default=datetime.datetime.now, verbose_name='date created')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ChannelFollow',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('channel', models.ForeignKey(to='snippets.Channel', unique=True, related_name='channel_follows_of_channel')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='channel_follows_of_user')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Cody',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, unique=True)),
                ('description', models.TextField(max_length=200, default='')),
                ('image', models.ImageField(upload_to='channel/channel_cody', default='')),
                ('which_day', models.CharField(choices=[('MO', 'Monday'), ('TU', 'Tuesday'), ('WE', 'Wednesday'), ('TH', 'Thursday'), ('FR', 'Friday'), ('SA', 'Saturday')], max_length=2, default='MO')),
                ('pub_date', models.DateTimeField(default=datetime.datetime(2015, 4, 21, 5, 22, 46, 792841, tzinfo=utc), verbose_name='date published')),
                ('channel', models.ForeignKey(to='snippets.Channel', related_name='codies_of_channel')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CodyCategory',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, default='')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CodyItem',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
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
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('cody', models.ForeignKey(to='snippets.Cody', unique=True, related_name='cody_likes_of_cody')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='cody_likes_of_user')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=8)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(default=datetime.datetime(2015, 4, 21, 5, 22, 46, 774416, tzinfo=utc), verbose_name='date published')),
                ('name', models.CharField(max_length=15, unique=True)),
                ('description', models.TextField(max_length=100, default='')),
                ('price', models.IntegerField(default=0)),
                ('brand', models.ForeignKey(to='snippets.Brand', related_name='products_of_brand', blank=True, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
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
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
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
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=20, default='')),
                ('slug', models.SlugField(help_text='Displayed tags depends on the order of priority.. like Outer->Jeans->Bags', unique=True)),
                ('gender', models.ForeignKey(to='snippets.Gender', related_name='tags_of_gender', blank=True, null=True)),
            ],
            options={
                'ordering': ('slug',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TestHashTag',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, unique=True)),
            ],
            options={
                'ordering': ('hash_tag_category',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TestHashTagCategory',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, unique=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TestModel',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
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
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField(max_length=200, blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='testhashtag',
            name='hash_tag_category',
            field=models.ForeignKey(to='snippets.TestHashTagCategory', default=''),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='product',
            name='tag',
            field=models.ForeignKey(to='snippets.Tag', related_name='products_of_tag', null=True),
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
            field=models.ForeignKey(to='snippets.Gender', related_name='cody_categories_of_gender', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cody',
            name='cody_category',
            field=models.ForeignKey(to='snippets.CodyCategory', related_name='codies_of_cody_category', blank=True, null=True),
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
            field=models.ForeignKey(to='snippets.Gender', max_length=5, related_name='brands_of_gender', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='brand',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
