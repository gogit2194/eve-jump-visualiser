# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-05-30 18:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sde', '0020_systemjump'),
    ]

    operations = [
        migrations.AlterField(
            model_name='system',
            name='sun',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='sde.Type'),
        ),
    ]
