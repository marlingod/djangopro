# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0003_useranswer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='useranswer',
            old_name='Question',
            new_name='question',
        ),
        migrations.AddField(
            model_name='useranswer',
            name='my_points',
            field=models.IntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='useranswer',
            name='thier_points',
            field=models.IntegerField(default=-1),
        ),
    ]
