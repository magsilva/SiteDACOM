# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import desenvolvimento.models


class Migration(migrations.Migration):

    dependencies = [
        ('desenvolvimento', '0013_matriz_numero'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='disciplina',
            name='equivalencia',
        ),
        migrations.RemoveField(
            model_name='disciplina',
            name='prerequisito',
        ),
        migrations.AddField(
            model_name='disciplina',
            name='equivalencia2',
            field=models.ManyToManyField(related_name='equivalencia', to='desenvolvimento.Disciplina'),
        ),
        migrations.AddField(
            model_name='disciplina',
            name='prerequisito1',
            field=models.ManyToManyField(related_name='prerequisito', to='desenvolvimento.Disciplina'),
        ),
        migrations.AlterField(
            model_name='planodeaula',
            name='upload',
            field=models.FileField(null=True, upload_to=desenvolvimento.models.user_directory_path, blank=True),
        ),
    ]
