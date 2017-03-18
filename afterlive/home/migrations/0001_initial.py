# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-01 07:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Facebook', models.CharField(max_length=512)),
                ('Instagram', models.CharField(max_length=512)),
                ('Youtube', models.CharField(max_length=512)),
                ('Twitter', models.CharField(max_length=512)),
                ('Tumblr', models.CharField(max_length=512)),
                ('Flickr', models.CharField(max_length=512)),
                ('Pinterest', models.CharField(max_length=512)),
                ('Website', models.CharField(max_length=512)),
            ],
        ),
    ]