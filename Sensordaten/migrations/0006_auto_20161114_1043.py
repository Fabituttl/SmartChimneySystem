# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-14 09:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Sensordaten', '0005_auto_20161114_1040'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Nutzer',
            new_name='Kunden',
        ),
    ]
