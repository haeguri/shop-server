# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0002_auto_20150422_0032'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
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
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=10, null=True)),
                ('color', models.CharField(max_length=10, null=True)),
                ('quantity', models.IntegerField(null=True)),
                ('cart', models.ForeignKey(to='cart.Cart', related_name='cart_items_of_cart')),
                ('product', models.ForeignKey(to='snippets.Product', related_name='cart_items_of_product')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
