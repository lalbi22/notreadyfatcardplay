# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-30 20:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fatcard', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='choice_text',
        ),
        migrations.RemoveField(
            model_name='choice',
            name='question',
        ),
        migrations.RemoveField(
            model_name='choice',
            name='votes',
        ),
        migrations.RemoveField(
            model_name='question',
            name='pub_date',
        ),
        migrations.RemoveField(
            model_name='question',
            name='question_text',
        ),
    ]
###