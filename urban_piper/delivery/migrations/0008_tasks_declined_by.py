# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-11-24 10:39
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('delivery', '0007_auto_20181124_1355'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='declined_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assignee_declined', to=settings.AUTH_USER_MODEL),
        ),
    ]
