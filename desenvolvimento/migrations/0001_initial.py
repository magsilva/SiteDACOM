# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AreaDeAtuacao',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descricao', models.CharField(max_length=511, verbose_name=b'Area de Atuacao')),
            ],
        ),
        migrations.CreateModel(
            name='Artigo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('listadeautores', models.CharField(max_length=5000, verbose_name=b'Lista de Autores')),
                ('titulo', models.CharField(max_length=255, verbose_name=b'Titulo do Artigo')),
                ('data', models.CharField(max_length=5, verbose_name=b'Data do Artigo')),
                ('doi', models.CharField(max_length=255, null=True, verbose_name=b'DOI', blank=True)),
                ('paginas', models.CharField(max_length=10, null=True, verbose_name=b'Paginas', blank=True)),
                ('resumo', models.CharField(max_length=5000, verbose_name=b'Resumo')),
            ],
        ),
        migrations.CreateModel(
            name='Coordenacao',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=50, verbose_name=b'Curso')),
                ('sigla', models.CharField(max_length=20, null=True, verbose_name=b'Sigla', blank=True)),
                ('perfilDoEgresso', models.CharField(max_length=10000, null=True, verbose_name=b'perfilDoEgresso', blank=True)),
                ('descricao', models.CharField(max_length=5000, null=True, verbose_name=b'Descricao', blank=True)),
                ('contato', models.CharField(max_length=100, null=True, verbose_name=b'Contato', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='DadosDeProfessor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=100, verbose_name=b'nome do professor')),
            ],
        ),
        migrations.CreateModel(
            name='DepartamentoAcademico',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=100, verbose_name=b'Nome')),
                ('sigla', models.CharField(max_length=100, verbose_name=b'Sigla')),
            ],
        ),
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=50, null=True, verbose_name=b'Nome da Disciplina', blank=True)),
                ('sigla', models.CharField(max_length=50, null=True, verbose_name=b'Sigla da Disciplina', blank=True)),
                ('ementa', models.CharField(max_length=5000, null=True, verbose_name=b'Ementa', blank=True)),
                ('descricao', models.CharField(max_length=50, null=True, verbose_name=b'Descricao', blank=True)),
                ('cargaHorariaPratica', models.CharField(max_length=50, verbose_name=b'Carga Horaria Pratica')),
                ('cargaHorariaTeorica', models.CharField(max_length=50, verbose_name=b'Carga Horaria Teorica')),
                ('cargaHorariaAPS', models.CharField(max_length=50, verbose_name=b'Carga Horaria Atividade Pratica Supervisionada')),
                ('cargaHorariaTotal', models.CharField(max_length=50, verbose_name=b'Carga Horaria Total')),
                ('departamentoAcademico', models.ForeignKey(related_name='NomeDepartamentoAcademico', blank=True, to='desenvolvimento.DepartamentoAcademico', null=True)),
                ('matriz', models.ForeignKey(related_name='matrizNome', blank=True, to='desenvolvimento.Curso', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('doi', models.CharField(max_length=255, verbose_name=b'DOI')),
                ('autores', models.CharField(max_length=5000, verbose_name=b'Autores')),
                ('titulo', models.CharField(max_length=5000, verbose_name=b'Titulo')),
                ('nomeevento', models.CharField(max_length=5000, null=True, verbose_name=b'Nome do Evento', blank=True)),
                ('ano', models.CharField(max_length=4, verbose_name=b'Ano')),
                ('volume', models.CharField(max_length=10, verbose_name=b'Volume')),
                ('paginas', models.CharField(max_length=255, verbose_name=b'Paginas')),
            ],
        ),
        migrations.CreateModel(
            name='Formacao',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ano_inicio', models.CharField(max_length=4, verbose_name=b'Ano de Inicio')),
                ('ano_conclusao', models.CharField(max_length=4, verbose_name=b'Ano de Conclusao')),
                ('tipo', models.CharField(max_length=511, verbose_name=b'Tipo')),
                ('descricao', models.CharField(max_length=5000, verbose_name=b'Descricao')),
                ('nome', models.CharField(max_length=5000, verbose_name=b'Nome')),
            ],
        ),
        migrations.CreateModel(
            name='Integrante',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=255, verbose_name=b'nome')),
                ('ehCoordenador', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Matriz',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('atividadeComplementar', models.CharField(max_length=256, null=True, verbose_name=b'Atividade Complementar', blank=True)),
                ('cargaHoraria', models.CharField(max_length=50, null=True, verbose_name=b'CargaHoraria', blank=True)),
                ('estagio', models.CharField(max_length=256, null=True, verbose_name=b'Estagio', blank=True)),
                ('tcc', models.CharField(max_length=10000, null=True, verbose_name=b'tcc', blank=True)),
                ('duracao', models.CharField(max_length=50, null=True, verbose_name=b'Duracao', blank=True)),
                ('turno', models.CharField(max_length=50, null=True, verbose_name=b'Turno', blank=True)),
                ('curso', models.ForeignKey(to='desenvolvimento.Curso')),
            ],
        ),
        migrations.CreateModel(
            name='PlanoDeAula',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('upload', models.FileField(null=True, upload_to=b'/home/humberto/Documentos/projectUtfpr/desenvolvimento/static/%c/planoDeAula/%y/%s', blank=True)),
                ('ano', models.CharField(max_length=4, null=True, verbose_name=b'Ano', blank=True)),
                ('semestre', models.CharField(max_length=20, null=True, verbose_name=b'semestre', blank=True)),
                ('codigodeTurma', models.CharField(max_length=15, null=True, verbose_name=b'codigodaTurma', blank=True)),
                ('disciplina', models.ForeignKey(related_name='Disciplina', to='desenvolvimento.Disciplina')),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=100, verbose_name=b'Nome')),
                ('email', models.CharField(max_length=200, null=True, verbose_name=b'E-mail', blank=True)),
                ('telefone', models.CharField(max_length=20, null=True, verbose_name=b'Telefone', blank=True)),
                ('funcao', models.CharField(max_length=100, verbose_name=b'Funcao')),
                ('lattes', models.CharField(max_length=50, null=True, verbose_name=b'Link do Lattes', blank=True)),
                ('bolsaprodutividade', models.CharField(max_length=100, null=True, verbose_name=b'Bolsa Produtividade', blank=True)),
                ('enderecoprofissional', models.CharField(max_length=5000, null=True, verbose_name=b'Endereco Profissional', blank=True)),
                ('nomeemcitacoesbibliograficas', models.CharField(max_length=255, null=True, verbose_name=b'Nome em Citacoes Bibliograficas', blank=True)),
                ('textoResumo', models.CharField(max_length=500, null=True, verbose_name=b'bolsaProdutividade', blank=True)),
                ('profile_image', models.ImageField(null=True, upload_to=b'', blank=True)),
                ('departamento', models.ForeignKey(to='desenvolvimento.DepartamentoAcademico')),
            ],
        ),
        migrations.CreateModel(
            name='Projeto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('datainicio', models.CharField(max_length=5, null=True, verbose_name=b'Data Inicio', blank=True)),
                ('datadefim', models.CharField(max_length=5, null=True, verbose_name=b'Data de Fim', blank=True)),
                ('agendafinanciadora', models.CharField(max_length=255, null=True, verbose_name=b'Agencia Financiadora', blank=True)),
                ('nome', models.CharField(max_length=1000, verbose_name=b'Nome do Projeto')),
                ('resumo', models.CharField(max_length=10000, verbose_name=b'Resumo')),
                ('situacao', models.CharField(max_length=100, null=True, verbose_name=b'Situacao', blank=True)),
                ('natureza', models.CharField(max_length=100, null=True, verbose_name=b'Natureza', blank=True)),
                ('professor', models.ForeignKey(related_name='Professor', to='desenvolvimento.Professor')),
            ],
        ),
        migrations.CreateModel(
            name='RelacaoDisciplinaCurso',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('periodo', models.IntegerField(verbose_name=b'Periodo')),
                ('tipo', models.CharField(default=b'FP', max_length=2, choices=[(b'OH', b'Optativa Humanas'), (b'OP', b'Optativa Profissionalizante'), (b'NC', b'Nucleo Comum'), (b'FP', b'Formacao Profissionalizante')])),
                ('cursoRelacao', models.ForeignKey(related_name='CursoRelacionado', blank=True, to='desenvolvimento.Curso', null=True)),
                ('disciplina', models.ForeignKey(related_name='DisciplinaRelacionada', blank=True, to='desenvolvimento.Disciplina', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ArtigoEmConferencia',
            fields=[
                ('artigo_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='desenvolvimento.Artigo')),
                ('nomedaConferencia', models.CharField(max_length=255, verbose_name=b'Nome da Conferencia')),
                ('ISSN', models.CharField(max_length=50, verbose_name=b'Codigo ISSN')),
                ('ISBN', models.CharField(max_length=50, verbose_name=b'Codigo ISBN')),
                ('local', models.CharField(max_length=255, verbose_name=b'Local da Conferencia')),
                ('ano', models.CharField(max_length=4, verbose_name=b'Ano')),
            ],
            bases=('desenvolvimento.artigo',),
        ),
        migrations.CreateModel(
            name='ArtigoEmPeriodico',
            fields=[
                ('artigo_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='desenvolvimento.Artigo')),
                ('nomejournal', models.CharField(max_length=255, verbose_name=b'Nome Journal')),
                ('ISSN', models.CharField(max_length=255, verbose_name=b'Codigo ISSN')),
                ('publisher', models.CharField(max_length=255, verbose_name=b'Editora')),
                ('numero', models.CharField(max_length=100, verbose_name=b'Numero')),
                ('volume', models.CharField(max_length=100, verbose_name=b'Volume')),
            ],
            bases=('desenvolvimento.artigo',),
        ),
        migrations.CreateModel(
            name='IntegranteProfessor',
            fields=[
                ('integrante_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='desenvolvimento.Integrante')),
                ('professor', models.ForeignKey(related_name='ProfessorIntegrante', to='desenvolvimento.Professor')),
            ],
            bases=('desenvolvimento.integrante',),
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
            model_name='curso',
            name='departamentoAcademico',
            field=models.ForeignKey(related_name='DepartamentoAcademico', to='desenvolvimento.DepartamentoAcademico'),
        ),
        migrations.AddField(
            model_name='coordenacao',
            name='coordenador',
            field=models.ForeignKey(related_name='coordenadorCoo', to='desenvolvimento.Professor'),
        ),
        migrations.AddField(
            model_name='coordenacao',
            name='curso',
            field=models.ForeignKey(related_name='Curso', to='desenvolvimento.Curso'),
        ),
        migrations.AddField(
            model_name='coordenacao',
            name='suplente',
            field=models.ForeignKey(related_name='suplenteCoo', to='desenvolvimento.Professor'),
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
    ]
