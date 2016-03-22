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
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=150, null=True)),
                ('email', models.EmailField(max_length=254, blank=True)),
                ('body', models.TextField(blank=True)),
                ('comment_date', models.DateTimeField(verbose_name=b'comment date')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(unique=True, max_length=255)),
                ('description', models.CharField(max_length=500)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('body', models.TextField(blank=True)),
                ('userId', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.AddField(
            model_name='comment',
            name='postId',
            field=models.ForeignKey(to='blog.Post'),
        ),
    ]
