# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('desenvolvimento', '0018_oferecimento_sala'),
    ]

    operations = [
        migrations.CreateModel(
            name='InfraEstrutura',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('chefiaDeDepartamento', models.CharField(max_length=100, verbose_name=500)),
                ('salaDeProfessores', models.CharField(max_length=100, verbose_name=500)),
                ('secretaria', models.CharField(max_length=100, verbose_name=500)),
            ],
        ),
        migrations.CreateModel(
            name='Sala',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sala', models.CharField(max_length=10, verbose_name=b'sala')),
                ('ehLaboratorio', models.BooleanField(default=False)),
                ('departamento', models.ForeignKey(related_name='DepartamerntoAcademico', to='desenvolvimento.DepartamentoAcademico')),
            ],
        ),
    ]
