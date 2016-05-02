# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('desenvolvimento', '0010_auto_20160502_1503'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='disciplina',
            name='descricao',
        ),
    ]
