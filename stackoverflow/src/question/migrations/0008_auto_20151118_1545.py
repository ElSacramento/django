# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0007_question_answers'),
    ]

    operations = [
        migrations.AddField(
            model_name='like',
            name='answer',
            field=models.ForeignKey(default=0, to='question.Answer'),
        ),
        migrations.AddField(
            model_name='like',
            name='question',
            field=models.ForeignKey(default=0, to='question.Question'),
        ),
    ]
