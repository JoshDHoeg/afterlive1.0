# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-29 08:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_photographer_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='profile',
            field=models.TextField(blank=True, null=True),
        ),
    ]
