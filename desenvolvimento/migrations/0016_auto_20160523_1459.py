# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('desenvolvimento', '0015_auto_20160509_1504'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=500, verbose_name=b'nomeDoAluno')),
                ('RA', models.IntegerField(default=0)),
                ('periodo', models.IntegerField(default=1)),
                ('cursoDoAluno', models.ForeignKey(related_name='CursodoAluno', to='desenvolvimento.Curso')),
            ],
        ),
        migrations.CreateModel(
            name='CalendarioAcademico',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('evento', models.CharField(max_length=10000, verbose_name=b'evento')),
            ],
        ),
        migrations.CreateModel(
            name='CentroAcademico',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=500, verbose_name=b'nome Do CA')),
                ('descricao', models.CharField(max_length=500, verbose_name=b'descricao')),
                ('informacao', models.CharField(max_length=500, verbose_name=b'informacao')),
                ('curso', models.ForeignKey(to='desenvolvimento.Curso', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Comissao',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='DiaDaSemana',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('diaDaSemana', models.CharField(default=b'SE', max_length=2, choices=[(b'SE', b'Segunda'), (b'TE', b'Terca'), (b'QA', b'Quarta'), (b'QI', b'Quinta'), (b'SX', b'Sexta'), (b'SA', b'Sabado')])),
            ],
        ),
        migrations.CreateModel(
            name='EmpresaJunior',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=100, verbose_name=b'nomeDaEmpresaJunior')),
                ('descricao', models.CharField(max_length=500, verbose_name=b'descricao')),
                ('informacao', models.CharField(max_length=500, verbose_name=b'informacao')),
                ('departamento', models.ForeignKey(related_name='Departamento', to='desenvolvimento.DepartamentoAcademico')),
            ],
        ),
        migrations.CreateModel(
            name='Estagiario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=500, verbose_name=b'nomeDoEstagiario')),
                ('funcao', models.CharField(max_length=500, verbose_name=b'Funcao')),
                ('dataInicial', models.DateTimeField()),
                ('dataFinal', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='HorarioDaAula',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('horarioDeAula', models.CharField(default=b'M1', max_length=13, choices=[(b'M1', b'07h30 - 08h20'), (b'M2', b'08h20 - 09h10'), (b'M3', b'09h10 - 10h00'), (b'M4', b'10h20 - 11h10'), (b'M5', b'11h10 - 12h00'), (b'M6', b'12h00 - 12h50'), (b'T1', b'13h00 - 13h50'), (b'T2', b'13h50 - 14h40'), (b'T3', b'14h40 - 15h30'), (b'T4', b'15h50 - 16h40'), (b'T5', b'16h40 - 17h30'), (b'T6', b'17h30 - 18h20'), (b'N1', b'18h40 - 19h30'), (b'N2', b'19h30 - 20h20'), (b'N3', b'20h20 - 21h10'), (b'N4', b'21h20 - 22h10'), (b'N5', b'22h10 - 23h00')])),
            ],
        ),
        migrations.CreateModel(
            name='MembroEleito',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('razao2', models.CharField(default=b'SR', max_length=10, choices=[(b'Al', b'Aluno'), (b'SR', b'Servidor')])),
                ('observacao', models.CharField(max_length=500, verbose_name=b'Observacao')),
                ('dataInicio', models.DateTimeField()),
                ('dataFim', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Oferecimento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('turma', models.CharField(max_length=50, verbose_name=b'Turma')),
                ('OferecidaPeloProfessor', models.ManyToManyField(related_name='Oferecida', to='desenvolvimento.Professor')),
                ('disciplina', models.ForeignKey(related_name='Disciplinaoferecida', to='desenvolvimento.RelacaoDisciplinaCurso')),
            ],
        ),
        migrations.CreateModel(
            name='RelacaoDiaDaSemanaHorarioDeAula',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dia', models.ForeignKey(related_name='diadaaula', to='desenvolvimento.DiaDaSemana')),
                ('horario', models.ForeignKey(related_name='Horariodaaula', to='desenvolvimento.HorarioDaAula')),
            ],
        ),
        migrations.CreateModel(
            name='Colegiado',
            fields=[
                ('comissao_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='desenvolvimento.Comissao')),
                ('profCoordenador', models.ForeignKey(related_name='professorCoordenador', to='desenvolvimento.Professor')),
                ('profResponsavelPelasAtividadesCompl', models.ForeignKey(related_name='professorResponsavelPelasAtividadesCompl', to='desenvolvimento.Professor')),
                ('profResponsavelPeloEstagio', models.ForeignKey(related_name='professorResponsavelPeloEstagio', to='desenvolvimento.Professor')),
                ('profResponsavelPeloTCC', models.ForeignKey(related_name='professorResponsavelPeloTCC', to='desenvolvimento.Professor')),
            ],
            bases=('desenvolvimento.comissao',),
        ),
        migrations.CreateModel(
            name='NDE',
            fields=[
                ('comissao_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='desenvolvimento.Comissao')),
                ('professorCoordenador', models.ForeignKey(related_name='ProfessorCoordenador', to='desenvolvimento.Professor')),
            ],
            bases=('desenvolvimento.comissao',),
        ),
        migrations.AddField(
            model_name='oferecimento',
            name='relacaoDiaHorarioAula',
            field=models.ManyToManyField(related_name='relacaoDoDiadaSemanaHorario', to='desenvolvimento.RelacaoDiaDaSemanaHorarioDeAula'),
        ),
        migrations.AddField(
            model_name='membroeleito',
            name='colegiado',
            field=models.ForeignKey(related_name='ColegiadodoCurso', to='desenvolvimento.Comissao'),
        ),
        migrations.AddField(
            model_name='membroeleito',
            name='membroEleitos',
            field=models.ForeignKey(related_name='MembroEleito', to='desenvolvimento.Professor'),
        ),
        migrations.AddField(
            model_name='membroeleito',
            name='membroSuplentes',
            field=models.ForeignKey(related_name='MembroSuplente', to='desenvolvimento.Professor'),
        ),
    ]
