# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0006_auto_20151117_2047'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='answers',
            field=models.IntegerField(default=0),
        ),
    ]
