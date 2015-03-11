# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
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
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
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
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('intro', models.TextField(max_length=200)),
                ('image', models.ImageField(upload_to='channel')),
                ('web', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Cody',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('title', models.CharField(max_length=30)),
                ('desc', models.TextField(max_length=200)),
                ('image', models.ImageField(upload_to='channel/channel_cody')),
                ('channel', models.ForeignKey(related_name='codies_of_channel', to='snippets.Channel')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CodyItem',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('tip', models.CharField(max_length=50)),
                ('cody', models.ForeignKey(related_name='cody_items_of_cody', to='snippets.Cody')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Designer',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('intro', models.TextField(max_length=200, blank=True)),
                ('image', models.ImageField(upload_to='upload/designer', default='')),
                ('web', models.CharField(max_length=50, blank=True)),
                ('address', models.CharField(max_length=200, blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DesignerFollow',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('follow', models.BooleanField(default=False)),
                ('designer', models.ForeignKey(related_name='designer_follows of_Designer', to='snippets.Designer')),
                ('user', models.ForeignKey(related_name='designer_follows_of_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('type', models.CharField(max_length=5)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('whether_like', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField(max_length=100)),
                ('price', models.IntegerField(default=0)),
                ('image', models.ImageField(upload_to='upload')),
                ('category', models.ForeignKey(related_name='products_of_category', to='snippets.Category')),
                ('designer', models.ForeignKey(related_name='products_of_designer', to='snippets.Designer', null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('address', models.TextField(max_length=200, blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
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
            model_name='category',
            name='gender',
            field=models.ForeignKey(related_name='categories_of_gender', to='snippets.Gender'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cartitem',
            name='product',
            field=models.ForeignKey(related_name='cart_items_of_product', to='snippets.Product'),
            preserve_default=True,
        ),
    ]
