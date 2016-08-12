# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('desenvolvimento', '0021_auto_20160613_1422'),
    ]

    operations = [
        migrations.AddField(
            model_name='calendarioacademico',
            name='dataFim',
            field=models.DateField(max_length=10, null=True, verbose_name=b'DataFim', blank=True),
        ),
        migrations.AddField(
            model_name='calendarioacademico',
            name='dataInicio',
            field=models.DateField(max_length=10, null=True, verbose_name=b'DataInicio', blank=True),
        ),
        migrations.AddField(
            model_name='matriz',
            name='cargaHorariaObrigatoria',
            field=models.CharField(max_length=50, null=True, verbose_name=b'CargaHorariaObrigatoria', blank=True),
        ),
        migrations.AddField(
            model_name='matriz',
            name='cargaHorariaOptDoCurso',
            field=models.CharField(max_length=50, null=True, verbose_name=b'CargaHoraria do curso', blank=True),
        ),
        migrations.AddField(
            model_name='matriz',
            name='cargaHorariaOptHumanas',
            field=models.CharField(max_length=50, null=True, verbose_name=b'CargaHorariaOptativaHumanas', blank=True),
        ),
        migrations.AlterField(
            model_name='infraestrutura',
            name='chefiaDeDepartamento',
            field=models.CharField(max_length=100, verbose_name=b'chefiaDoDepartamento'),
        ),
        migrations.AlterField(
            model_name='infraestrutura',
            name='salaDeProfessores',
            field=models.CharField(max_length=100, verbose_name=b'salaDosProfessores'),
        ),
        migrations.AlterField(
            model_name='infraestrutura',
            name='secretaria',
            field=models.CharField(max_length=100, verbose_name=b'secretaria'),
        ),
        migrations.AlterField(
            model_name='matriz',
            name='atividadeComplementar',
            field=models.CharField(max_length=10000, null=True, verbose_name=b'Atividade Complementar', blank=True),
        ),
        migrations.AlterField(
            model_name='matriz',
            name='estagio',
            field=models.CharField(max_length=10000, null=True, verbose_name=b'Estagio', blank=True),
        ),
        migrations.AlterField(
            model_name='membroeleito',
            name='colegiado',
            field=models.ForeignKey(related_name='ComissaoDoCurso', blank=True, to='desenvolvimento.Colegiado', null=True),
        ),
    ]
