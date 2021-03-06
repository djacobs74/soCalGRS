# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-01 19:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import sorl.thumbnail.fields
import website.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Railway',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=255)),
                ('description', models.CharField(default='', max_length=255)),
            ],
            options={
                'ordering': ['title'],
                'verbose_name': 'Railway',
                'verbose_name_plural': 'Railways',
            },
        ),
        migrations.CreateModel(
            name='RailwayImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(default='', max_length=255)),
                ('image', sorl.thumbnail.fields.ImageField(blank=True, null=True, upload_to=website.models.story_upload)),
                ('position', models.IntegerField(blank=True, default=1, null=True)),
                ('railway', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='website.Railway')),
            ],
            options={
                'verbose_name': 'RailwayImage',
                'verbose_name_plural': 'RailwayImages',
            },
        ),
    ]
