# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings
import snippets.models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('introduce', models.TextField(blank=True, max_length=200)),
                ('image', models.ImageField(default='', upload_to='upload/brand')),
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
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('brand', models.ForeignKey(unique=True, to='snippets.Brand', related_name='brand_follows_of_brand')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='brand_follows_of_user')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BrandInterview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
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
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
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
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
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
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(unique=True, max_length=30)),
                ('introduce', models.TextField(max_length=200)),
                ('image', models.ImageField(upload_to='channel')),
                ('background', models.ImageField(default='', upload_to='channel/background')),
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
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
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
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(unique=True, max_length=20)),
                ('description', models.TextField(default='', max_length=200)),
                ('image', models.ImageField(default='', upload_to='channel/channel_cody')),
                ('which_day', models.CharField(default='MO', choices=[('MO', 'Monday'), ('TU', 'Tuesday'), ('WE', 'Wednesday'), ('TH', 'Thursday'), ('FR', 'Friday'), ('SA', 'Saturday')], max_length=2)),
                ('pub_date', models.DateTimeField(default=datetime.datetime(2015, 4, 20, 9, 50, 12, 713438, tzinfo=utc), verbose_name='date published')),
                ('channel', models.ForeignKey(to='snippets.Channel', related_name='codies_of_channel')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CodyCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(default='', max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CodyItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
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
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
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
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('type', models.CharField(max_length=8)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('pub_date', models.DateTimeField(default=datetime.datetime(2015, 4, 20, 9, 50, 12, 695017, tzinfo=utc), verbose_name='date published')),
                ('name', models.CharField(unique=True, max_length=15)),
                ('description', models.TextField(default='', max_length=100)),
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
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('description', models.TextField(default='', blank=True, max_length=1000)),
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
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
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
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('type', models.CharField(max_length=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('category', models.CharField(default='', choices=[('TOP', 'Top'), ('BOT', 'Bottom'), ('ACC', 'Accessory')], help_text='Category is concept bigger than the Tag', max_length=3)),
                ('type', models.CharField(default='', max_length=20)),
                ('slug', models.SlugField(unique=True, help_text='Displayed tags depends on the order of priority.. like Outer->Jeans->Bags')),
                ('gender', models.ForeignKey(to='snippets.Gender', related_name='tags_of_gender', blank=True, null=True)),
            ],
            options={
                'ordering': ('slug',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
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
            field=models.ForeignKey(to='snippets.Gender', related_name='brands_of_gender', blank=True, max_length=5, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='brand',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
