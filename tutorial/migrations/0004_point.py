# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-03-10 19:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tutorial', '0003_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Point',
            fields=[
                ('slug', models.CharField(max_length=500, primary_key=True, serialize=False)),
                ('point', models.CharField(max_length=20)),
                ('form', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tutorial.FormChoice')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tutorial.Student')),
            ],
        ),
    ]