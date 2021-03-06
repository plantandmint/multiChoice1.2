# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-04 14:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorial', '0002_formchoice_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=50)),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('year', models.CharField(max_length=100)),
                ('grade', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')], max_length=100)),
                ('level', models.CharField(choices=[('\u0e1b\u0e23\u0e30\u0e16\u0e21', '\u0e1b\u0e23\u0e30\u0e16\u0e21'), ('\u0e21\u0e31\u0e18\u0e22\u0e21', '\u0e21\u0e31\u0e18\u0e22\u0e21')], max_length=100)),
                ('room', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], max_length=50)),
            ],
        ),
    ]
