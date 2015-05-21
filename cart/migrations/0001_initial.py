# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0002_auto_20150512_1522'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('size', models.CharField(null=True, max_length=10)),
                ('color', models.CharField(null=True, max_length=10)),
                ('quantity', models.IntegerField(null=True)),
                ('cart', models.ForeignKey(to='cart.Cart', related_name='cart_items_of_cart')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('recipient', models.CharField(max_length=10, default='', verbose_name='수령인')),
                ('mobile_no', models.CharField(max_length=15, default='', verbose_name='모바일번호')),
                ('addr1', models.CharField(max_length=100, default='', verbose_name='주소1')),
                ('addr2', models.CharField(max_length=100, default='', verbose_name='주소2')),
                ('ship_msg', models.TextField(max_length=500, default='', verbose_name='배송메세지')),
                ('means_pay', models.CharField(choices=[('mobile', '휴대폰'), ('card', '신용카드')], max_length=2, default='mobile', verbose_name='결제수단')),
                ('order_date', models.DateTimeField(default=datetime.datetime(2015, 5, 12, 6, 22, 56, 789723, tzinfo=utc), verbose_name='주문일')),
                ('state_ship', models.CharField(choices=[('wait', '출고대기'), ('outbound', '출고'), ('delivery', '배송중'), ('complete', '배송완료')], max_length=20, default='wait', verbose_name='배송상태')),
                ('state_pay', models.CharField(choices=[('wait', '결제대기'), ('complete', '결제완료')], max_length=20, default='wait', verbose_name='결제상태')),
                ('sum_price', models.PositiveIntegerField(default=0, verbose_name='구매가격', blank=True)),
                ('shipping', models.PositiveIntegerField(default=2500, verbose_name='배송료', blank=True)),
                ('total_price', models.PositiveIntegerField(default=0, verbose_name='합계금액', blank=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='orders_of_user')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='cartitem',
            name='order',
            field=models.ForeignKey(to='cart.Order', related_name='cart_items_of_order', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cartitem',
            name='product',
            field=models.ForeignKey(to='snippets.Product', related_name='cart_items_of_product'),
            preserve_default=True,
        ),
    ]
