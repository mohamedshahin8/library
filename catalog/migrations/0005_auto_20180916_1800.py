# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-09-16 18:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_auto_20180902_2234'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookinstance',
            options={'ordering': ['due_back']},
        ),
        migrations.RenameField(
            model_name='bookinstance',
            old_name='due_book',
            new_name='due_back',
        ),
    ]