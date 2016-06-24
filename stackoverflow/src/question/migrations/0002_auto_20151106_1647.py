# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='user',
            field=models.ForeignKey(to='user_page.User'),
        ),
        migrations.AlterField(
            model_name='like',
            name='user',
            field=models.ForeignKey(to='user_page.User'),
        ),
        migrations.AlterField(
            model_name='question',
            name='user',
            field=models.ForeignKey(to='user_page.User'),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
