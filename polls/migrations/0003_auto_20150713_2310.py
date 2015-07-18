# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20150713_2305'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='achoice_text',
            new_name='choice_text',
        ),
        migrations.RenameField(
            model_name='choice',
            old_name='aquestion',
            new_name='question',
        ),
        migrations.RenameField(
            model_name='choice',
            old_name='avotes',
            new_name='votes',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='apub_date',
            new_name='pub_date',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='aquestion_text',
            new_name='question_text',
        ),
    ]
