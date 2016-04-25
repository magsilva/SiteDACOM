# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('desenvolvimento', '0003_curso_matrizatual'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projeto',
            name='professor',
        ),
        migrations.AddField(
            model_name='projeto',
            name='integrantes',
            field=models.ManyToManyField(related_name='integrante', null=True, to='desenvolvimento.Integrante', blank=True),
        ),
        migrations.AddField(
            model_name='projeto',
            name='integrantesProfessor',
            field=models.ManyToManyField(related_name='integranteProfessor', null=True, to='desenvolvimento.IntegranteProfessor', blank=True),
        ),
    ]
