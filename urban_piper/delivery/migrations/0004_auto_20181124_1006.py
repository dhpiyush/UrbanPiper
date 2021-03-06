# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-11-24 04:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0003_auto_20181124_1004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.IntegerField(choices=[(0, 'High'), (1, 'Medium'), (2, 'Low')]),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.IntegerField(choices=[(0, 'New'), (1, 'Accepted'), (2, 'Completed'), (3, 'Declined'), (4, 'Cancelled')]),
        ),
    ]
