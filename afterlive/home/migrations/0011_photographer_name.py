# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-24 06:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20170323_2320'),
    ]

    operations = [
        migrations.AddField(
            model_name='photographer',
            name='Name',
            field=models.CharField(blank=True, max_length=140, null=True),
        ),
    ]