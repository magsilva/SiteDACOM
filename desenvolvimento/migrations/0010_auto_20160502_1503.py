# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('desenvolvimento', '0009_auto_20160502_0957'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='disciplina',
            name='objetivo',
        ),
        migrations.AddField(
            model_name='disciplina',
            name='objetivo',
            field=models.CharField(max_length=5000, null=True, verbose_name=b'objetivo', blank=True),
        ),
    ]
