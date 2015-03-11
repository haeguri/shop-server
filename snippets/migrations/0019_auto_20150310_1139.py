# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0018_designer_gender'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminChannel',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=30)),
                ('image', models.ImageField(upload_to='channel')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RenameField(
            model_name='designerfollow',
            old_name='follow',
            new_name='whether_follow',
        ),
        migrations.AlterField(
            model_name='designerfollow',
            name='designer',
            field=models.ForeignKey(related_name='designer_follows_of_designer', to='snippets.Designer'),
        ),
    ]
