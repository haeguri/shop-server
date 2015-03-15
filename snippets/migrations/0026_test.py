# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0025_auto_20150312_0005'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('image', sorl.thumbnail.fields.ImageField(upload_to='whatever')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
