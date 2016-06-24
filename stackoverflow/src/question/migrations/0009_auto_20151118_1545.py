# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0008_auto_20151118_1545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='answer',
            field=models.ForeignKey(to='question.Answer'),
        ),
        migrations.AlterField(
            model_name='like',
            name='question',
            field=models.ForeignKey(to='question.Question'),
        ),
    ]
