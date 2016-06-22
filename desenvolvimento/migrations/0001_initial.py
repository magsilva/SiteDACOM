# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
import desenvolvimento.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Colegiado',
            fields=[
                ('comissao_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='desenvolvimento.Comissao')),
            ],
            bases=('desenvolvimento.comissao',),
        ),
        migrations.CreateModel(
            name='IntegranteProfessor',
            fields=[
                ('integrante_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='desenvolvimento.Integrante')),
            ],
            bases=('desenvolvimento.integrante',),
        ),
        migrations.CreateModel(
            name='NDE',
            fields=[
                ('comissao_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='desenvolvimento.Comissao')),
            ],
            bases=('desenvolvimento.comissao',),
        ),
        migrations.CreateModel(
            name='Servidor',
            fields=[
                ('pessoa_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='desenvolvimento.Pessoa')),
                ('funcao', models.CharField(max_length=100, null=True, verbose_name=b'Funcao', blank=True)),
                ('lattes', models.CharField(max_length=50, null=True, verbose_name=b'Link do Lattes', blank=True)),
                ('bolsaprodutividade', models.CharField(max_length=100, null=True, verbose_name=b'Bolsa Produtividade', blank=True)),
                ('enderecoprofissional', models.CharField(max_length=5000, null=True, verbose_name=b'Endereco Profissional', blank=True)),
                ('nomeemcitacoesbibliograficas', models.CharField(max_length=255, null=True, verbose_name=b'Nome em Citacoes Bibliograficas', blank=True)),
                ('textoResumo', models.CharField(max_length=500, null=True, verbose_name=b'bolsaProdutividade', blank=True)),
                ('profile_image', models.ImageField(null=True, upload_to=b'', blank=True)),
            ],
            bases=('desenvolvimento.pessoa',),
        ),
        migrations.AddField(
            model_name='projeto',
            name='integrantes',
            field=models.ManyToManyField(related_name='integrante', null=True, to='desenvolvimento.Integrante', blank=True),
        ),
        migrations.AddField(
            model_name='oferecimento',
            name='disciplina',
            field=models.ForeignKey(related_name='Disciplinaoferecida', to='desenvolvimento.RelacaoDisciplinaCurso'),
        ),
        migrations.AddField(
            model_name='oferecimento',
            name='relacaoDiaHorarioAula',
            field=models.ManyToManyField(related_name='relacaoDoDiadaSemanaHorario', to='desenvolvimento.RelacaoDiaDaSemanaHorarioDeAula'),
        ),
        migrations.AddField(
            model_name='membroeleito',
            name='colegiado',
            field=models.ForeignKey(related_name='ComissaoDoCurso', blank=True, to='desenvolvimento.Comissao', null=True),
        ),
        migrations.AddField(
            model_name='membroeleito',
            name='membroEleitos',
            field=models.ForeignKey(related_name='MembroEleito', blank=True, to='desenvolvimento.Pessoa', null=True),
        ),
        migrations.AddField(
            model_name='membroeleito',
            name='membroSuplentes',
            field=models.ForeignKey(related_name='MembroSuplente', blank=True, to='desenvolvimento.Pessoa', null=True),
        ),
        migrations.AddField(
            model_name='curso',
            name='departamentoAcademico',
            field=models.ForeignKey(related_name='DepartamentoAcademico', to='desenvolvimento.DepartamentoAcademico'),
        ),
        migrations.AddField(
            model_name='curso',
            name='matrizAtual',
            field=models.ForeignKey(related_name='matrizNome', blank=True, to='desenvolvimento.Matriz', null=True),
        ),
        migrations.AddField(
            model_name='coordenacao',
            name='curso',
            field=models.ForeignKey(related_name='Curso', to='desenvolvimento.Curso'),
        ),
        migrations.AddField(
            model_name='chefiadodepartamento',
            name='departamentoAcademico',
            field=models.ForeignKey(related_name='departamentoAcademico', blank=True, to='desenvolvimento.DepartamentoAcademico', null=True),
        ),
        migrations.AddField(
            model_name='centroacademico',
            name='curso',
            field=models.ForeignKey(to='desenvolvimento.Curso', max_length=500),
        ),
        migrations.AddField(
            model_name='aluno',
            name='cursoDoAluno',
            field=models.ForeignKey(related_name='CursodoAluno', to='desenvolvimento.Curso'),
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('servidor_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='desenvolvimento.Servidor')),
            ],
            bases=('desenvolvimento.servidor',),
        ),
        migrations.CreateModel(
            name='TecnicoAdm',
            fields=[
                ('servidor_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='desenvolvimento.Servidor')),
            ],
            bases=('desenvolvimento.servidor',),
        ),
        migrations.AddField(
            model_name='servidor',
            name='departamento',
            field=models.ForeignKey(to='desenvolvimento.DepartamentoAcademico'),
        ),
        migrations.AddField(
            model_name='projeto',
            name='integrantesProfessor',
            field=models.ManyToManyField(related_name='integranteProfessor', null=True, to='desenvolvimento.IntegranteProfessor', blank=True),
        ),
        migrations.AddField(
            model_name='artigoemperiodico',
            name='integrantes',
            field=models.ManyToManyField(related_name='integrantes', to='desenvolvimento.Integrante'),
        ),
        migrations.AddField(
            model_name='artigoemperiodico',
            name='integrantesProfessor',
            field=models.ManyToManyField(related_name='integrantesProfessor', to='desenvolvimento.IntegranteProfessor'),
        ),
        migrations.AddField(
            model_name='oferecimento',
            name='OferecidaPeloProfessor',
            field=models.ManyToManyField(related_name='Oferecida', to='desenvolvimento.Professor'),
        ),
        migrations.AddField(
            model_name='nde',
            name='professorCoordenador',
            field=models.ForeignKey(related_name='ProfessorCoordenador', to='desenvolvimento.Professor'),
        ),
        migrations.AddField(
            model_name='integranteprofessor',
            name='professor',
            field=models.ForeignKey(related_name='ProfessorIntegrante', to='desenvolvimento.Professor'),
        ),
        migrations.AddField(
            model_name='formacao',
            name='formacaoProfessor',
            field=models.ForeignKey(related_name='FormacaoProfessor', to='desenvolvimento.Professor'),
        ),
        migrations.AddField(
            model_name='evento',
            name='professoresDoEvento',
            field=models.ManyToManyField(related_name='professoresDoEvento', to='desenvolvimento.Professor'),
        ),
        migrations.AddField(
            model_name='dadosdeprofessor',
            name='professorDados',
            field=models.ForeignKey(related_name='DadosDeProfessor', to='desenvolvimento.Professor'),
        ),
        migrations.AddField(
            model_name='coordenacao',
            name='coordenador',
            field=models.ForeignKey(related_name='coordenadorCoo', to='desenvolvimento.Professor'),
        ),
        migrations.AddField(
            model_name='coordenacao',
            name='suplente',
            field=models.ForeignKey(related_name='suplenteCoo', to='desenvolvimento.Professor'),
        ),
        migrations.AddField(
            model_name='colegiado',
            name='profCoordenador',
            field=models.ForeignKey(related_name='professorCoordenador', to='desenvolvimento.Professor'),
        ),
        migrations.AddField(
            model_name='colegiado',
            name='profResponsavelPelasAtividadesCompl',
            field=models.ForeignKey(related_name='professorResponsavelPelasAtividadesCompl', to='desenvolvimento.Professor'),
        ),
        migrations.AddField(
            model_name='colegiado',
            name='profResponsavelPeloEstagio',
            field=models.ForeignKey(related_name='professorResponsavelPeloEstagio', to='desenvolvimento.Professor'),
        ),
        migrations.AddField(
            model_name='colegiado',
            name='profResponsavelPeloTCC',
            field=models.ForeignKey(related_name='professorResponsavelPeloTCC', to='desenvolvimento.Professor'),
        ),
        migrations.AddField(
            model_name='chefiadodepartamento',
            name='chefe',
            field=models.ForeignKey(related_name='chefeDeDepartamento', blank=True, to='desenvolvimento.Professor', null=True),
        ),
        migrations.AddField(
            model_name='chefiadodepartamento',
            name='suplente',
            field=models.ForeignKey(related_name='suplenteChefe', blank=True, to='desenvolvimento.Professor', null=True),
        ),
        migrations.AddField(
            model_name='artigo',
            name='professores',
            field=models.ManyToManyField(related_name='ArtigoProfessor', to='desenvolvimento.Professor'),
        ),
        migrations.AddField(
            model_name='areadeatuacao',
            name='areaProfessor',
            field=models.ForeignKey(related_name='AreaProfessor', to='desenvolvimento.Professor'),
        ),
    ]
