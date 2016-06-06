# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('desenvolvimento', '0020_auto_20160603_1238'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChefiaDoDepartamento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=100, verbose_name=b'Nome')),
                ('email', models.CharField(max_length=200, null=True, verbose_name=b'E-mail', blank=True)),
                ('telefone', models.CharField(max_length=20, null=True, verbose_name=b'Telefone', blank=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='membroeleito',
            name='colegiado',
        ),
        migrations.RemoveField(
            model_name='membroeleito',
            name='razao2',
        ),
        migrations.RemoveField(
            model_name='professor',
            name='bolsaprodutividade',
        ),
        migrations.RemoveField(
            model_name='professor',
            name='departamento',
        ),
        migrations.RemoveField(
            model_name='professor',
            name='email',
        ),
        migrations.RemoveField(
            model_name='professor',
            name='enderecoprofissional',
        ),
        migrations.RemoveField(
            model_name='professor',
            name='funcao',
        ),
        migrations.RemoveField(
            model_name='professor',
            name='id',
        ),
        migrations.RemoveField(
            model_name='professor',
            name='lattes',
        ),
        migrations.RemoveField(
            model_name='professor',
            name='nome',
        ),
        migrations.RemoveField(
            model_name='professor',
            name='nomeemcitacoesbibliograficas',
        ),
        migrations.RemoveField(
            model_name='professor',
            name='profile_image',
        ),
        migrations.RemoveField(
            model_name='professor',
            name='telefone',
        ),
        migrations.RemoveField(
            model_name='professor',
            name='textoResumo',
        ),
        migrations.AddField(
            model_name='infraestrutura',
            name='telefoneDaChefia',
            field=models.CharField(max_length=20, null=True, verbose_name=b'TelefoneDoDepartamento', blank=True),
        ),
        migrations.AddField(
            model_name='infraestrutura',
            name='telefoneDaSalaDosProfessores',
            field=models.CharField(max_length=20, null=True, verbose_name=b'TelefoneDaSala', blank=True),
        ),
        migrations.AddField(
            model_name='membroeleito',
            name='comissao',
            field=models.ForeignKey(related_name='ComissaoDoCurso', blank=True, to='desenvolvimento.Comissao', null=True),
        ),
        migrations.AddField(
            model_name='sala',
            name='infraEstruturaDoDepartamento',
            field=models.ForeignKey(related_name='InfraestuturaDoDepartamento', blank=True, to='desenvolvimento.InfraEstrutura', null=True),
        ),
        migrations.AlterField(
            model_name='calendarioacademico',
            name='data',
            field=models.CharField(max_length=10, null=True, verbose_name=b'Data', blank=True),
        ),
        migrations.AlterField(
            model_name='estagiario',
            name='dataFinal',
            field=models.CharField(max_length=10, null=True, verbose_name=b'DataDeConclusao', blank=True),
        ),
        migrations.AlterField(
            model_name='estagiario',
            name='dataInicial',
            field=models.CharField(max_length=10, null=True, verbose_name=b'DataDeAdmissao', blank=True),
        ),
        migrations.AlterField(
            model_name='membroeleito',
            name='membroEleitos',
            field=models.ForeignKey(related_name='MembroEleito', blank=True, to='desenvolvimento.Pessoa', null=True),
        ),
        migrations.AlterField(
            model_name='membroeleito',
            name='membroSuplentes',
            field=models.ForeignKey(related_name='MembroSuplente', blank=True, to='desenvolvimento.Pessoa', null=True),
        ),
        migrations.AlterField(
            model_name='sala',
            name='departamento',
            field=models.ForeignKey(related_name='DepartamerntoAcademico', blank=True, to='desenvolvimento.DepartamentoAcademico', null=True),
        ),
        migrations.AlterField(
            model_name='sala',
            name='sala',
            field=models.CharField(max_length=100, null=True, verbose_name=b'sala', blank=True),
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
            model_name='chefiadodepartamento',
            name='chefe',
            field=models.ForeignKey(related_name='chefeDeDepartamento', blank=True, to='desenvolvimento.Professor', null=True),
        ),
        migrations.AddField(
            model_name='chefiadodepartamento',
            name='departamentoAcademico',
            field=models.ForeignKey(related_name='departamentoAcademico', blank=True, to='desenvolvimento.DepartamentoAcademico', null=True),
        ),
        migrations.AddField(
            model_name='chefiadodepartamento',
            name='suplente',
            field=models.ForeignKey(related_name='suplenteChefe', blank=True, to='desenvolvimento.Professor', null=True),
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
            model_name='professor',
            name='servidor_ptr',
            field=models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, default='novo', serialize=False, to='desenvolvimento.Servidor'),
            preserve_default=False,
        ),
    ]
