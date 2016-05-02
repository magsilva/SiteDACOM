# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('desenvolvimento', '0011_remove_disciplina_descricao'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='disciplina',
            name='matriz',
        ),
        migrations.AddField(
            model_name='disciplina',
            name='matriz',
            field=models.ManyToManyField(related_name='matrizNome', null=True, to='desenvolvimento.Curso', blank=True),
        ),
    ]
