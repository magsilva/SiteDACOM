# -*- coding: UTF-8 -*-
# -*- encoding: UTF-8 -*-
from __future__ import absolute_import
from __future__ import print_function

from _mysql import NULL
from string import split
from subprocess import call
import subprocess
import xml.etree.cElementTree as et
import csv
import sys

import django
from dateutil.parser import parser
import mysql.connector
import shutil
import os, errno
import warnings
import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from django.conf import settings
settings.configure(DEBUG=True)

settings.DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'UTFPR',  # Or path to database file if using sqlite3.
        'USER': 'root',
        'PASSWORD': 'Humberto1!',
        'HOST': '',  # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',  # Set to empty string for default.
    }
}

from desenvolvimento.models import Artigo, Professor, ArtigoEmConferencia, AreaDeAtuacao, \
    Integrante, DepartamentoAcademico, ArtigoEmPeriodico, Projeto, Evento, Curso, Formacao

warnings.filterwarnings('ignore')

sys.path.append('desenvolvimento/lattes/scriptLattesV8.10/scriptLattes')
sys.path.append('desenvolvimento/lattes/scriptLattesV8.10/scriptLattes/producoesBibliograficas/')
sys.path.append('desenvolvimento/lattes/scriptLattesV8.10/scriptLattes/producoesTecnicas/')
sys.path.append('desenvolvimento/lattes/scriptLattesV8.10/scriptLattes/producoesArtisticas/')
sys.path.append('desenvolvimento/lattes/scriptLattesV8.10/scriptLattes/producoesUnitarias/')
sys.path.append('desenvolvimento/lattes/scriptLattesV8.10/scriptLattes/orientacoes/')
sys.path.append('desenvolvimento/lattes/scriptLattesV8.10/scriptLattes/eventos/')
sys.path.append('desenvolvimento/lattes/scriptLattesV8.10/scriptLattes/charts/')
sys.path.append('desenvolvimento/lattes/scriptLattesV8.10/scriptLattes/internacionalizacao/')
sys.path.append('desenvolvimento/lattes/scriptLattesV8.10/scriptLattes/qualis/')
sys.path.append('desenvolvimento/lattes/scriptLattesV8.10/scriptLattes/patentesRegistros/')


def initSistem():

    boolean = 1

    departamento = None

    try:
        if DepartamentoAcademico.objects.all().__len__()==0:
            nomeDepartamento = "Departamento Acadêmico de Computação"
            siglaDepartamento = "DACOM"

            departamento =  DepartamentoAcademico(nome=nomeDepartamento, sigla=siglaDepartamento)
            departamento.save()

            print( "Foi adicionado o " + nomeDepartamento + " - " + siglaDepartamento )

            while boolean ==1:
                print("Quer adicionar outros departamentos?")
                # print("1 - para sim adicionar outros departamentos, 2 - para não adicionar outros departamentos")
                boolean  =  int(raw_input('1 - para sim adicionar outros departamentos, 2 - para não adicionar outros departamentos:'))

                if boolean==1:
                    nomeDepartamento = str(raw_input('Digite o nome do departamento academico: '))
                    siglaDepartamento = str(raw_input('Digite o sigla do departamento academico: '))
                    departamento =  DepartamentoAcademico(nome=nomeDepartamento, sigla=siglaDepartamento)
                    departamento.save()

                if boolean == 2:
                    print("Registro de departamento acadêmicos com sucesso :)")

                if boolean != 1 and boolean != 2:
                    print("Valor incorreto, por favor preste atenção nas intruções")
    except DepartamentoAcademico.DoesNotExist:
        nomeDepartamento = "Departamento Acadêmico de Computação"
        siglaDepartamento = "DACOM"
        departamento =  DepartamentoAcademico(nome=nomeDepartamento, sigla=siglaDepartamento)
        departamento.save()

    boolean =1
    if Curso.objects.all().__len__()==0:
        nomeDoCurso =  "Bacharelado de Ciência da Computação"
        siglaDoCurso = "BCC"
        departamento = DepartamentoAcademico.objects.get(sigla="DACOM")
        curso = Curso(nome =nomeDoCurso, sigla = siglaDoCurso, departamentoAcademico = departamento)
        curso.save()
        print( "Foi adicionado o " + nomeDoCurso+ " - " + siglaDoCurso )

        while boolean ==1:
            print("Quer adicionar outros cursos?")
            # print("1 - para sim adicionar outros cursos, 2 - para não adicionar outros cursos")
            boolean  =  int(raw_input('1 - para sim adicionar outros cursos, 2 - para não adicionar outros cursos:'))

            if boolean==1:
                nomeDoCurso = str(raw_input('Digite o nome do curso: '))
                siglaDoCurso = str(raw_input('Digite o sigla do curso: '))
                curso = Curso(nome =nomeDoCurso, siglaDoCurso = siglaDoCurso, departamentoAcademico = departamento)
                curso.save()
            if boolean == 2:
                print("Registro de departamento cursos com sucesso :)")

            if  boolean != 1 and boolean != 2:
                print("Valor incorreto, por favor preste atenção nas intruções")

def executeLattes():
    call("python scriptLattes.py ./data/scriptlattes-utfpr-cm-dacom.config", shell=True)




def executeLeitorXML():

    tree = et.parse("data/lattes-site/database.xml")
    root = tree.getroot()

    for child in root:

        prof = Professor()
        prof.lattes = child.get('id')

        for child1 in child:

            for identificacao in child1.iter('identificacao'):
                if identificacao.find('nome_inicial').text is not None:
                    nome_inicial = identificacao.find('nome_inicial').text
                if identificacao.find('nome_completo').text is not None:
                    nome_completo = identificacao.find('nome_completo').text
                if identificacao.find('nome_citacao_bibliografica').text is not None:
                    nome_citacao_bibliografica = identificacao.find('nome_citacao_bibliografica').text
                if identificacao.find('sexo').text is not None:
                    sexo = identificacao.find('sexo').text

                prof.nome = nome_inicial
                prof.nome_completo = nome_completo
                prof.nomeEmCitacoesBibliograficas = nome_citacao_bibliografica
                prof.sexo = sexo
                departamento = DepartamentoAcademico.objects.get(sigla='DACOM')
                prof.departamento = departamento
                prof.funcao = "Professor"

                if Professor.objects.filter(nome=prof.nome).__len__()==0:
                    prof.save()
                if Professor.objects.get(nome=prof.nome) is not None:
                    item = Professor.objects.get(nome=prof.nome)
                    item.nome = prof.nome
                    item.nome_completo = prof.nome_completo
                    item.nomeEmCitacoesBibliograficas = prof.nomeEmCitacoesBibliograficas
                    item.departamento = prof.departamento
                    item.funcao = "Professor"
                    item.save()


            for formacao in child1.iter('formacao_academica'):
                for formacao1 in formacao.iter('formacao'):
                    ano_conclusao = ""
                    nome = ""
                    descricao =""
                    if formacao1.find('ano_inicio').text is not None:
                        ano_inicio = formacao1.find('ano_inicio').text
                    if formacao1.find('ano_conclusao').text is not None:
                        ano_conclusao = formacao1.find('ano_conclusao').text
                    if formacao1.find('tipo').text is not None:
                        tipo = formacao1.find('tipo').text
                    if formacao1.find('nome_instituicao').text is not None:
                        nome = formacao1.find('nome_instituicao').text
                    if formacao1.find('descricao').text is not None:
                        descricao = formacao1.find('descricao').text

                    profDaIteracao =  Professor.objects.get(nome=prof.nome)
                    formacao = Formacao(ano_inicio=ano_inicio[0:4], ano_conclusao=ano_conclusao, tipo=tipo, descricao=descricao, nome= nome, formacaoProfessor=profDaIteracao)
                    if Formacao.objects.filter(nome=nome).__len__()==0:
                        formacao.save()

            for projetospesquisa in child1.iter('projetos_pesquisa'):
                for projeto in projetospesquisa.iter('projeto'):

                    if projeto.find('ano_inicio').text is not None:
                        ano_inicio = projeto.find('ano_inicio').text
                    if projeto.find('ano_conclusao').text is not None:
                        ano_conclusao = projeto.find('ano_conclusao').text
                    if projeto.find('nome').text is not None:
                        nome = projeto.find('nome').text
                    if projeto.find('descricao').text is not None:
                        descricao = projeto.find('descricao').text

                    parte1 = descricao.encode("utf-8").split("Descrição: ")
                    try :
                        parte2 = parte1[1].split("Situação: ")
                    except IndexError:
                        parte2 = parte1[0].split("Situação: ")
                    try:
                        parte3 =  parte2[1].split("Natureza: ")
                    except IndexError:
                        parte3 =  parte2[0].split("Natureza: ")
                    try:
                        parte4 =  parte3[1].split("Integrantes: ")
                    except IndexError:
                        parte4 =  parte3[0].split("Integrantes: ")
                    try:
                        parte5 =  parte4[1].split("- Integrante")
                    except IndexError:
                        parte5 =  parte4[0].split("- Integrante")
                    profDaIteracao =  Professor.objects.get(nome=prof.nome)
                    # print(parte1[1])

                    try:
                      if(parte1[1].__contains__("Situação:")):

                        proj2 = Projeto(nome=nome, resumo = parte1[1].split("Situação:")[0], datadefim = ano_conclusao, datainicio = ano_inicio, situacao = parte2[1].split(";")[0], natureza = parte3[1].split(".")[0], professor = profDaIteracao)
                      else:
                        proj2 = Projeto(nome=nome, resumo = parte1[1].split("Integrantes:")[0], datadefim = ano_conclusao, datainicio = ano_inicio, situacao = parte2[1].split(";")[0], natureza = parte3[1].split(".")[0], professor = profDaIteracao)

                    except IndexError:
                      if (parte1[0].__contains__("Situação:")):
                        proj2 = Projeto(nome=nome, resumo = parte1[0].split("Situação:")[0], datadefim = ano_conclusao, datainicio = ano_inicio, situacao = " ", natureza = parte3[0].split(".")[0], professor = profDaIteracao)
                      else:
                        proj2 = Projeto(nome=nome, resumo = parte1[0].split("Integrantes:")[0], datadefim = ano_conclusao, datainicio = ano_inicio, situacao = " ", natureza = parte3[0].split(".")[0], professor = profDaIteracao)

                    if Projeto.objects.filter(nome=nome).__len__()==0:
                        proj2.save()
                    else:
                        p2 = Projeto.objects.get(nome=nome)
                        p2.nome = proj2.nome
                        p2.resumo = proj2.resumo
                        p2.datadefim = proj2.datadefim
                        p2.datainicio = proj2.datainicio
                        p2.situacao = proj2.situacao
                        p2.natureza = proj2.natureza
                        p2.professor = proj2.professor
                        # p2.save()

                        for i in parte5[1:parte5.__len__()-1]:
                            # print(i.replace("/", ""))
                            if i.__contains__("- Coordenador"):
                                for j in i.replace("/", "").split("- Coordenador"):
                                    if Professor.objects.filter(nome=j):
                                        profI = Professor.objects.filter(nome=j)[0]
                                        item=  Integrante(nome=j, ehCoordenador =True, ehProfessor = True,professor = profI)
                                        item.save()
                                    else:
                                        item=  Integrante(nome=j, ehCoordenador =True, ehProfessor = False, professor = None)
                                        item.save()

                            else:
                                if Professor.objects.filter(nome=i):
                                    profI = Professor.objects.filter(nome=i)[0]
                                    item=  Integrante(nome=i, ehCoordenador =False, ehProfessor = True,professor = profI)
                                    item.save()
                                else:
                                    item=  Integrante(nome=i, ehCoordenador =False, ehProfessor = False, professor = None)
                                    item.save()


            for areaatuacao in child1.iter('area_atuacao'):
                descricao = areaatuacao.find('descricao').text
                profDaIteracao =  Professor.objects.get(nome=prof.nome)
                area = AreaDeAtuacao(descricao= descricao, areaProfessor=profDaIteracao)

                if AreaDeAtuacao.objects.filter(descricao=descricao).__len__()==0:
                    area.save()



            for eventos in child1.iter('trabalho_completo_congresso'):  # eventos
                e = Evento()
                for evento in eventos.iter('trabalho_completo'):
                    if evento.find('doi').text is not None:
                        doi = evento.find('doi').text
                    if evento.find('autores').text is not None:
                        autores = evento.find('autores').text
                    if evento.find('titulo').text is not None:
                        titulo = evento.find('titulo').text
                    if evento.find('nome_evento').text is not None:
                        nome_evento = evento.find('nome_evento').text
                    if evento.find('ano').text is not None:
                        ano = evento.find('ano').text
                    if evento.find('volume').text is not None:
                        volume = evento.find('volume').text
                    if evento.find('paginas').text is not None:
                        paginas = evento.find('paginas').text

                    e.doi=doi
                    e.autores=autores
                    e.titulo =titulo
                    e.nomeEvento =nome_evento
                    e.ano = ano
                    e.volume = volume
                    e.paginas = paginas

                    if Evento.object.get(titulo =e.titulo).__len__()==0:
                        e.save()
                    else:
                        eventoNovo = Evento.object.get(titulo =e.titulo)
                        eventoNovo.doi =  e.doi
                        eventoNovo.autores=e.autores
                        eventoNovo.nomeEvento =e.nomeEvento
                        eventoNovo.ano = e.ano
                        eventoNovo.volume =e.olume
                        eventoNovo.paginas = e.paginas
                        eventoNovo.save()

                    # Eventos.append(e)

            #         # print(2)
            #
            # for resumoCongresso in child1.iter('resumo_congresso'):
            #     for resumCo in resumoCongresso.iter('resumo'):
            #         if resumCo.find('doi').text is not None:
            #             doi = resumCo.find('doi').text
            #         if resumCo.find('autores').text is not None:
            #             autores = resumCo.find('autores').text
            #         if resumCo.find('titulo').text is not None:
            #             titulo = resumCo.find('titulo').text
            #         if resumCo.find('nome_evento').text is not None:
            #             nome_evento = resumCo.find('nome_evento').text
            #         if resumCo.find('ano').text is not None:
            #             ano = resumCo.find('ano').text
            #         if resumCo.find('volume').text is not None:
            #             volume = resumCo.find('volume').text
            #         if resumCo.find('paginas').text is not None:
            #             paginas = resumCo.find('paginas').text
            #         if resumCo.find('numero').text is not None:
            #             numero = resumCo.find('numero').text
            # #
            #         artigo = Artigo()
            #         artigo.paginas = paginas
            #         artigo.data = ano
            #         artigo.doi = doi
            #         artigo.listaDeAutores = autores
            #         artigo.titulo= titulo
            #
            #
            #
            #         artigo.save()
            #         artigosScriptLattes.append(artigo)
            #
            #
            # #
            # for artigoPeriodico in child1.iter('artigos_em_periodicos'):
            #     for artigo in artigoPeriodico.iter('artigo'):
            #         if artigo.find('doi').text is not None:
            #             doi = artigo.find('doi').text
            #         if artigo.find('autores').text is not None:
            #             autores = artigo.find('autores').text
            #         if artigo.find('titulo').text is not None:
            #             titulo = artigo.find('titulo').text
            #         if artigo.find('revista').text is not None:
            #             revista = artigo.find('revista').text
            #         if artigo.find('ano').text is not None:
            #             ano = artigo.find('ano').text
            #         if artigo.find('volume').text is not None:
            #             volume = artigo.find('volume').text
            #         if artigo.find('paginas').text is not None:
            #             paginas = artigo.find('paginas').text
            #         if artigo.find('numero').text is not None:
            #             numero = artigo.find('numero').text
            #
            #


if __name__ == "__main__":
    executeLattes()
    initSistem()
    executeLeitorXML()


    #lixo utilizavel

    #
    # config = {
    #     'user': 'root',
    #     'passwd': 'Humberto1!',
    #     'database': 'UTFPR'
    # }
    #
    #
    # connection = mysql.connector.connect(**config)
    # conector = connection.cursor()
         # conector.execute("SELECT * FROM desenvolvimento_professor")
    # professoresCadastrados = conector.fetchall()
    #
    # conector.execute("SELECT * FROM desenvolvimento_artigo")
    # artigosCadastrados = conector.fetchall()
    #
    # conector.execute ("SELECT * FROM desenvolvimento_artigoemconferencia")
    # resultAritgoEmConferencia = conector.fetchall()
    #
    # conector.execute ("SELECT * FROM desenvolvimento_artigoemperiodico")
    # resultArtigoEmPeriodico = conector.fetchall()
    #
    # conector.execute ("SELECT * FROM desenvolvimento_formacao")
    # resultFormacao = conector.fetchall()
    #
    # conector.execute ("SELECT * FROM desenvolvimento_projeto")
    # projetosCadastrados = conector.fetchall()
