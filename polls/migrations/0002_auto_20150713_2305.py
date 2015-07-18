# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='choice_text',
            new_name='achoice_text',
        ),
        migrations.RenameField(
            model_name='choice',
            old_name='question',
            new_name='aquestion',
        ),
        migrations.RenameField(
            model_name='choice',
            old_name='votes',
            new_name='avotes',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='pub_date',
            new_name='apub_date',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='question_text',
            new_name='aquestion_text',
        ),
    ]
