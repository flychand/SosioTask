# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-24 01:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                
                ('fullname', models.CharField(max_length=40)),
                ('food', models.CharField(max_length=40)),
                ('clothes', models.CharField(max_length=40)),
                ('housekeeping', models.CharField(max_length=40)),
                ('medicine', models.CharField(max_length=40)),
                ('fun', models.CharField(max_length=40)),

            ],
        ),
    ]