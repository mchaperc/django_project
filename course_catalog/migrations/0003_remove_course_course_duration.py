# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-08 02:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course_catalog', '0002_course_course_duration'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='course_duration',
        ),
    ]
