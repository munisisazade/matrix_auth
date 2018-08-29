# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-08-25 16:23
from __future__ import unicode_literals

import account.models
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_workers_salary'),
    ]

    operations = [
        migrations.AddField(
            model_name='workers',
            name='publish_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='workers',
            name='salary',
            field=models.IntegerField(default=account.models.generate_salary),
        ),
    ]