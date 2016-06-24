# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0004_auto_20151117_1835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='creation_date',
            field=models.DateTimeField(default=django.utils.timezone.now, blank=True),
        ),
    ]
