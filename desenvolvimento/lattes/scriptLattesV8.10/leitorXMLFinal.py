# -*- coding: UTF-8 -*-
# -*- encoding: UTF-8 -*-
from __future__ import absolute_import
from __future__ import print_function

import os
from distutils.command.config import config
from subprocess import call
import xml.etree.ElementTree as et
import warnings
import sys
import re

from bs4 import BeautifulSoup
from django.conf import settings
from lxml import html
import requests
from scipy.weave.base_info import info_list

import desenvolvimento

settings.configure(DEBUG=True)
settings.DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'UTFPR',
        'USER': 'root',
        'PASSWORD': 'Humberto1!',
        'HOST': '',
        'PORT': '',
    }
}

import django
django.setup()

from desenvolvimento.models import *
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
        cargaHoraria ="3.655 horas"
        perfilDoEgresso="<p><b>Perfil: </b>O profissional formado em Ciência da Computação na UTFPR, Campus Campo Mourão, estará capacitado para modelar, arquitetar, desenvolver, implementar, adaptar, produzir, industrializar, instalar e manter sistemas computacionais. Este profissional poderá atuar como:</p><ol><li><b>1. Desenvolvedor de soluções computacionais</b>: desempenhar os papéis de analista de sistemas, programador, gerente de desenvolvimento, gerente de projetos, entre outros.</li><li><b>2. Gerente de infraestrutura de tecnologia da informação</b>: exercer funções como a de analista de suporte, administrador de banco de dados, gerente de tecnologia da informação, consultor/auditor na área de infraestrutura, entre outros.</li><li><b>3. Gestor de Sistemas de Informação</b>: assumir papel como gerente de sistemas de informação, consultor/auditor em gestão de sistemas de informação, entre outros.</li><li><b>4. Analista de Negócios</b>: identificar oportunidades competitivas, a partir da aplicação de novas tecnologias, avaliando e identificando melhores práticas nos processos de negócio da empresa e do mercado; propor implementações para a melhoria da qualidade, eficiência e eficácia dos processos; dimensionar o impacto de alterações de negócio nos sistemas sob sua responsabilidade; apoiar a integração de sistemas e dados dentro de sua área e com as demais áreas; sustentar o cumprimento e disseminar os padrões corporativos de computação.</li><li><b>5. Profissional liberal</b>: prestar consultoria no desenvolvimento de produtos na área de computação.</li><li><b>6. Pesquisador</b>: desenvolver pesquisas científicas agindo como um agente transformador que cria novos paradigmas e desenvolve novas tecnologias na área de sistemas computacionais, promovendo o desenvolvimento científico, ou aplicando os conhecimentos científicos, promovendo o desenvolvimento tecnológico na área de Computação.</li></ol>"
        descricao = "<p>Desta forma, o curso prepara o aluno para as áreas de: inovação, planejamento e gerenciamento de informação e infraestrutura dos sistemas computacionais; desenvolvimento e evolução de sistemas para o uso de processos organizacionais, departamentais e/ou individuais; e por fim, atuar como um empreendedor.</p><p>Como se pode observar, o egresso do curso de Bacharelado em Ciência da Computação pode atuar em muitas áreas, constituindo-se um profissional versátil e preparado para o dinamismo do mercado de trabalho.</p><p> </p>"

        duracao = "8 semestres"
        turno = "Integral (vespertino e noturno)"
        contato = "cocic-cm@utfpr.edu.br"

        curso = Curso(nome =nomeDoCurso, sigla = siglaDoCurso, departamentoAcademico = departamento,  perfilDoEgresso=perfilDoEgresso, descricao=descricao, contato=contato)
        curso.save()
        matriz = Matriz(curso = curso,turno=turno, cargaHoraria=cargaHoraria, duracao=duracao )
        matriz.save()
        curso.matrizAtual=matriz

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
                print("Registro de cursos com sucesso :)")

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

            for projetospesquisa in child1.iter('projetos_pesquisa'):
                for projeto in projetospesquisa.iter('projeto'):
                    descricao = u"Descrição:"
                    resumo = u""
                    situacao = u"Situação:"
                    natureza = u"Natureza:"
                    integrantes = u"Integrantes:"
                    alunosEnvolvidos =u"Alunos envolvidos:"
                    financiadores = u"Financiador(es):"
                    nProducao =u"Número de produções C, T A:"
                    nOrientacao= u"Número de orientações:"
                    proj = None

                    if projeto.find('ano_inicio').text is not None:
                        ano_inicio = projeto.find('ano_inicio').text
                    if projeto.find('ano_conclusao').text is not None:
                        ano_conclusao = projeto.find('ano_conclusao').text

                    if projeto.find('nome').text is not None:
                        nome = projeto.find('nome').text
                    if projeto.find('descricao').text is not None:
                        descricaodoprojeto = projeto.find('descricao').text
                    posDescricao =descricaodoprojeto.find(descricao)
                    posSituacao =descricaodoprojeto.find(situacao)
                    posNatureza =descricaodoprojeto.find(natureza)
                    posAlunosEnvolvidos =descricaodoprojeto.find(alunosEnvolvidos)
                    posIntegrantes =descricaodoprojeto.find(integrantes)
                    posFincanciadores =descricaodoprojeto.find(financiadores)
                    posProducao = descricaodoprojeto.find(nProducao)
                    posOrientacao = descricaodoprojeto.find(nOrientacao)

                    if posDescricao!=-1 and posSituacao!=-1:
                        descricao  = descricaodoprojeto[posDescricao:posSituacao]
                    if posSituacao!=-1 and posNatureza!=-1:
                        situacao =descricaodoprojeto[posSituacao:posNatureza]
                    if posNatureza!=-1 and posAlunosEnvolvidos != -1:
                        natureza= descricaodoprojeto[posNatureza:posAlunosEnvolvidos]
                    if posAlunosEnvolvidos != -1  and posIntegrantes != -1:
                        alunosEnvolvidos =descricaodoprojeto[posAlunosEnvolvidos:posIntegrantes]
                    if posIntegrantes != -1 and posFincanciadores != -1:
                        integrantes = descricaodoprojeto[posIntegrantes:posFincanciadores]
                    elif posIntegrantes != -1 and posFincanciadores == -1:
                        integrantes = descricaodoprojeto[posIntegrantes:len(descricaodoprojeto)]

                    posInicial = 0
                    posFinal = integrantes.find(".")
                    if ano_conclusao=="Atual":
                        ano_conclusao="2016"
                    proj = Projeto(nome= nome,datadefim = ano_conclusao, datainicio = ano_inicio, situacao =situacao[10:situacao.__len__()], natureza=natureza[10:natureza.__len__()], resumo=descricao[11:descricao.__len__()])

                    if(Projeto.objects.filter(nome=nome).__len__()==0):
                        proj.save()
                        integranteApenas = integrantes[posInicial:posFinal]
                        integranteApenas = integranteApenas.replace("Integrantes: ", "")
                        match = integranteApenas.split("/")
                        # print(match)
                        for item  in match:
                                print(item)
                                if item.__contains__(u"Integrante"):
                                    print("ADD prof")
                                    novo = item.replace(u" - Integrante ", u"")
                                    novo = novo.replace(u" - Integrante", u"")
                                    if(Professor.objects.filter(nome=novo).__len__()>0):
                                        if IntegranteProfessor.objects.filter(nome=novo).__len__()>0:
                                            integProf = IntegranteProfessor.objects.get(nome=novo)
                                            proj.integrantesProfessor.add(integProf)
                                        else:
                                            prof = Professor.objects.get(nome=novo)
                                            integProf = IntegranteProfessor(nome=novo, ehCoordenador=False, professor=prof)
                                            integProf.save()
                                            proj.integrantesProfessor.add(integProf)
                                    else:
                                        if Integrante.objects.filter(nome=novo).__len__()>0:
                                            integProf = Integrante.objects.get(nome=novo)
                                            proj.integrantes.add(integProf)
                                        else:
                                            integranteNovo = Integrante(nome =novo, ehCoordenador=False)
                                            integranteNovo.save()
                                            proj.integrantes.add(integranteNovo)
                                elif item.__contains__(u"Coordenador"):
                                    novo =  item.replace(u" - Coordenador ", u"")
                                    novo = novo.replace(u" - Coordenador", u"")
                                    if(Professor.objects.filter(nome=novo).__len__()>0):
                                        if IntegranteProfessor.objects.filter(nome=novo).__len__()>0:
                                            integProf = IntegranteProfessor.objects.get(nome=novo)
                                            proj.integrantesProfessor.add(integProf)
                                        else:
                                            prof = Professor.objects.get(nome=novo)
                                            integProf = IntegranteProfessor(nome=novo, ehCoordenador=True, professor=prof)
                                            integProf.save()
                                            proj.integrantesProfessor.add(integProf)
                                    else:
                                        if Integrante.objects.filter(nome=novo).__len__()>0:
                                            integProf = Integrante.objects.get(nome=novo)
                                            proj.integrantes.add(integProf)
                                        else:
                                            integranteNovo = Integrante(nome =novo, ehCoordenador=True)
                                            integranteNovo.save()
                                            proj.integrantes.add(integranteNovo)
                                else:
                                    if (Professor.objects.filter(nome=novo).__len__() > 0):
                                      if IntegranteProfessor.objects.filter(nome=novo).__len__() > 0:
                                        integProf = IntegranteProfessor.objects.get(nome=novo)
                                        proj.integrantesProfessor.add(integProf)
                                      else:
                                        prof = Professor.objects.get(nome=novo)
                                        integProf = IntegranteProfessor(nome=novo, ehCoordenador=False, professor=prof)
                                        integProf.save()
                                        proj.integrantesProfessor.add(integProf)
                                    else:
                                      if Integrante.objects.filter(nome=novo).__len__() > 0:
                                        integProf = Integrante.objects.get(nome=novo)
                                        proj.integrantes.add(integProf)
                                      else:
                                        integranteNovo = Integrante(nome=novo, ehCoordenador=False)
                                        integranteNovo.save()
                                        proj.integrantes.add(integranteNovo)


if __name__ == "__main__":
    # executeLattes()
    initSistem()
    executeLeitorXML()
    # findProfilePhoto()
