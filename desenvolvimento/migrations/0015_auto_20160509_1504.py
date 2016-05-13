# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('desenvolvimento', '0014_auto_20160509_1501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disciplina',
            name='equivalencia2',
            field=models.ManyToManyField(related_name='equivalencia', null=True, to='desenvolvimento.Disciplina', blank=True),
        ),
        migrations.AlterField(
            model_name='disciplina',
            name='prerequisito1',
            field=models.ManyToManyField(related_name='prerequisito', null=True, to='desenvolvimento.Disciplina', blank=True),
        ),
    ]
