# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('user_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('age', models.PositiveSmallIntegerField(blank=True)),
                ('resetKey', models.CharField(max_length=50, null=True)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            bases=('auth.user',),
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name_collection', models.CharField(max_length=100, blank=True)),
                ('format', models.CharField(max_length=4, blank=True)),
                ('subject', models.CharField(max_length=100, blank=True)),
                ('delta_sending_time', models.IntegerField(blank=True)),
                ('last_update_time', models.DateTimeField(blank=True)),
                ('user', models.ForeignKey(to='novajoy.Account', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PostLetters',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('target', models.CharField(max_length=50, blank=True)),
                ('title', models.CharField(max_length=100, blank=True)),
                ('body', models.TextField(blank=True)),
                ('attachment', models.TextField(null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RSSFeed',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.URLField(blank=True)),
                ('pubDate', models.DateTimeField(blank=True)),
                ('spoiled', models.BooleanField(default=False)),
                ('collection', models.ManyToManyField(to='novajoy.Collection', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RSSItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=222, null=True, blank=True)),
                ('description', models.TextField(blank=True)),
                ('link', models.URLField(blank=True)),
                ('author', models.CharField(max_length=30, null=True, blank=True)),
                ('pubDate', models.DateTimeField(blank=True)),
                ('rssfeed', models.ForeignKey(blank=True, to='novajoy.RSSFeed', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
