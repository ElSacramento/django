# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0003_remove_answer_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime.now, blank=True),
        ),
    ]
