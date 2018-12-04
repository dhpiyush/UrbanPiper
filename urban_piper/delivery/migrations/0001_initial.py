# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-11-23 17:13
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('priority', models.IntegerField(choices=[(0, 'High'), (1, 'Medium'), (2, 'Low')])),
                ('created_on', models.DateField()),
                ('status', models.IntegerField(choices=[(0, 'New'), (1, 'Accepted'), (2, 'Completed'), (3, 'Declined'), (4, 'Cancelled')])),
                ('completed_on', models.DateField(blank=True, null=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]