# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-13 22:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bigbrother_sniper', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LabelGuardList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label_value', models.CharField(max_length=32)),
                ('drop_on_flag', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='TextGuardList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_value', models.CharField(max_length=32)),
                ('drop_on_flag', models.BooleanField(default=False)),
            ],
        ),
    ]
