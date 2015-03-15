# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('snippets', '0027_delete_test'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=20)),
                ('intro', models.TextField(blank=True, max_length=200)),
                ('image', models.ImageField(upload_to='upload/designer', default='')),
                ('background', models.ImageField(upload_to='upload/designer/background', default='')),
                ('web', models.CharField(blank=True, max_length=50)),
                ('address', models.CharField(blank=True, max_length=200)),
                ('gender', models.ForeignKey(null=True, max_length=5, blank=True, to='snippets.Gender', related_name='brands_of_gender')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BrandFollow',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('whether_follow', models.BooleanField(default=False)),
                ('brand', models.ForeignKey(to='snippets.Brand', related_name='brand_follows_of_brand')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='brand_follows_of_user')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='designer',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='designer',
            name='user',
        ),
        migrations.RemoveField(
            model_name='designerfollow',
            name='designer',
        ),
        migrations.RemoveField(
            model_name='designerfollow',
            name='user',
        ),
        migrations.DeleteModel(
            name='DesignerFollow',
        ),
        migrations.RemoveField(
            model_name='product',
            name='designer',
        ),
        migrations.DeleteModel(
            name='Designer',
        ),
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(null=True, blank=True, to='snippets.Brand', related_name='products_of_brand'),
            preserve_default=True,
        ),
    ]
