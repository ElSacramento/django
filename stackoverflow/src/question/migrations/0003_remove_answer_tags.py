# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0002_auto_20151106_1647'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='tags',
        ),
    ]
