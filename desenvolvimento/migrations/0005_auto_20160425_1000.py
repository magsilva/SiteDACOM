# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('desenvolvimento', '0004_auto_20160425_0854'),
    ]

    operations = [
        migrations.AddField(
            model_name='disciplina',
            name='equivalencia',
            field=models.ManyToManyField(related_name='_equivalencia_+', null=True, to='desenvolvimento.Disciplina', blank=True),
        ),
        migrations.AddField(
            model_name='disciplina',
            name='objetivo',
            field=models.ManyToManyField(related_name='_objetivo_+', null=True, to='desenvolvimento.Disciplina', blank=True),
        ),
        migrations.AddField(
            model_name='disciplina',
            name='prerequisito',
            field=models.ManyToManyField(related_name='_prerequisito_+', null=True, to='desenvolvimento.Disciplina', blank=True),
        ),
    ]
