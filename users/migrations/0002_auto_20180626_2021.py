# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-26 12:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookinfo',
            options={'verbose_name': '图书', 'verbose_name_plural': '图书'},
        ),
        migrations.AlterModelTable(
            name='bookinfo',
            table='tb_books',
        ),
    ]