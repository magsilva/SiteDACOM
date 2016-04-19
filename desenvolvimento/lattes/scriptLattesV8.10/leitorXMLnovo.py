# -*- coding: UTF-8 -*-
# -*- encoding: UTF-8 -*-
from __future__ import absolute_import
from __future__ import print_function

import os
from subprocess import call
import xml.etree.ElementTree as et
import warnings
import sys

from bs4 import BeautifulSoup
from django.conf import settings
from lxml import html
import requests

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
        curso = Curso(nome =nomeDoCurso, sigla = siglaDoCurso, departamentoAcademico = departamento,  perfilDoEgresso=perfilDoEgresso, descricao=descricao, duracao=duracao,  contato=contato)
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
                    print("Professor: "+item.nome+ " Salvo com Sucesso")

                dadosDeCitacaoEmBibliografia =  prof.nomeEmCitacoesBibliograficas.split(";")
                for dado in dadosDeCitacaoEmBibliografia:

                    dadosDeProfessor = DadosDeProfessor(nome=dado, professorDados=Professor.objects.get(nome=prof.nome))
                    dadosDeProfessor.save()
                    print("Dados Do professor salvo com sucesso")

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
                        print("Formacao do Professor salvo com sucesso")

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
                        if proj2.datadefim=="Atual":
                            proj2.datadefim=2016
                        p2.datadefim = proj2.datadefim
                        p2.datainicio = proj2.datainicio
                        p2.situacao = proj2.situacao
                        p2.natureza = proj2.natureza
                        p2.professor = proj2.professor
                        print("Projeto salvo com Sucesso")
                        p2.save()
                        #     criar um classe buscar e faz um mapeamento de dados do professor;


                        for i in parte5[1:parte5.__len__()-1]:
                            i = (i.replace(" / ", ""))

                            if i.__contains__("- Coordenador"):
                                for j in i.split("- Coordenador"):
                                    if Professor.objects.filter(nome=j):
                                        profI = Professor.objects.filter(nome=j)[0]
                                        item=  IntegranteProfessor(nome=j, ehCoordenador =True, professor = profI)
                                        p2.integranteProfessor.add(item)
                                        print("Integrante salvo com Sucesso")
                                    else:
                                        integrante=  Integrante(nome=j, ehCoordenador =True)
                                        integrante.save()
                                        p2.integrante.add(integrante)
                                        print("Integrante salvo com Sucesso")

                            else:
                                if Professor.objects.filter(nome=i):
                                    profI = Professor.objects.filter(nome=i)[0]

                                    item2 = IntegranteProfessor(nome=i, professor = profI)
                                    if IntegranteProfessor.objects.filter(nome=item2.nome).__len__()==0:
                                        item2.save()
                                        p2.integranteProfessor.add(item2)
                                    print("Integrante salvo com Sucesso")
                                else:
                                    integrante=  Integrante(nome=i, ehCoordenador =False)
                                    # integrante.save()
                                    p2.integrante.add(integrante)
                                    print("Integrante salvo com Sucesso")


            for areaatuacao in child1.iter('area_atuacao'):
                descricao = areaatuacao.find('descricao').text

                profDaIteracao =  Professor.objects.get(nome=prof.nome)

                area = AreaDeAtuacao(descricao= descricao, areaProfessor=profDaIteracao)
                if AreaDeAtuacao.objects.filter(descricao=descricao).__len__()==0:
                    area.save()
                    print("Area de Atuação salvo com Sucesso")

            for eventos in child1.iter('trabalho_completo_congresso'):  # eventos

                for evento in eventos.iter('trabalho_completo'):
                    volume1=""
                    paginas= ""
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
                        volume1 = evento.find('volume').text
                    if evento.find('paginas').text is not None:
                        paginas = evento.find('paginas').text
                    e = Evento()
                    e.doi=doi
                    e.autores=autores
                    e.titulo =titulo
                    e.nomeEvento =nome_evento
                    e.ano = ano
                    e.volume = volume1
                    e.paginas = paginas

                    if Evento.objects.filter(titulo=e.titulo).__len__()==0:
                        e.save()
                    else:
                        eventoNovo = Evento.objects.get(titulo =e.titulo)
                        eventoNovo.doi =  e.doi
                        eventoNovo.autores=e.autores
                        eventoNovo.nomeEvento =e.nomeEvento
                        eventoNovo.ano = e.ano
                        eventoNovo.volume =e.volume
                        eventoNovo.paginas = e.paginas
                        eventoNovo.save()
                        print("Evento salvo com Sucesso")
                        e = eventoNovo


                    for i in autores.split(" ; "):
                        i= i.strip()
                        profCurrent = DadosDeProfessor.objects.filter(nome=i);

                        if(profCurrent.__len__()>0):
                            professor = profCurrent[0].professorDados
                            if(professor):
                                e.professoresDoEvento.add(professor)
                        else:
                            print("Professor nao e da DACOM")


            for resumoCongresso in child1.iter('resumo_congresso'):
                for resumCo in resumoCongresso.iter('resumo'):
                    print("titulo")
                    if resumCo.find('doi').text is not None:
                        doi = resumCo.find('doi').text
                        print(doi)
                    if resumCo.find('autores').text is not None:
                        autores = resumCo.find('autores').text
                        print(autores)
                    if resumCo.find('titulo').text is not None:
                        titulo = resumCo.find('titulo').text
                        print(titulo)
                    if resumCo.find('nome_evento').text is not None:
                        nome_evento = resumCo.find('nome_evento').text
                    if resumCo.find('ano').text is not None:
                        ano = resumCo.find('ano').text
                    if resumCo.find('volume').text is not None:
                        volume = resumCo.find('volume').text
                    if resumCo.find('paginas').text is not None:
                        paginas = resumCo.find('paginas').text
                    if resumCo.find('numero').text is not None:
                        numero = resumCo.find('numero').text

            for artigoPeriodico in child1.iter('artigos_em_periodicos'):
                for artigo in artigoPeriodico.iter('artigo'):
                    numero=""
                    if artigo.find('doi').text is not None:
                        doi = artigo.find('doi').text
                    if artigo.find('titulo').text is not None:
                        titulo = artigo.find('titulo').text
                    if artigo.find('autores').text is not None:
                        autores = artigo.find('autores').text
                    if artigo.find('revista').text is not None:
                        revista = artigo.find('revista').text
                    if artigo.find('volume').text is not None:
                        volume = artigo.find('volume').text
                    if artigo.find('paginas').text is not None:
                        paginas = artigo.find('paginas').text
                    if artigo.find('numero').text is not None:
                        numero = artigo.find('numero').text
                    if artigo.find('ano').text is not None:
                        ano = artigo.find('ano').text


                    profDaIteracao =  Professor.objects.get(nome=prof.nome)

                    artigo = ArtigoEmPeriodico()

                    artigo.paginas = paginas
                    artigo.data = ano
                    artigo.doi = doi
                    artigo.titulo= titulo
                    artigo.publisher = revista
                    artigo.volume = volume
                    artigo.listadeautores=autores
                    artigo.numero = numero
                    artigo.professorDoArtigo = profDaIteracao

                    if ArtigoEmPeriodico.objects.filter(titulo=titulo).__len__()==0:
                        artigo.save()

                    else:
                        art= ArtigoEmPeriodico.objects.filter(titulo=titulo)[0]
                        art.titulo = artigo.titulo
                        if art.data=="Atual":
                            art.data=2016
                        art.paginas = artigo.paginas
                        art.doi = artigo.doi
                        art.publisher = artigo.publisher
                        art.volume = artigo.volume
                        art.numero = artigo.numero
                        # art.listadeautores = artigo.listadeautores
                        # art.professor = artigo.professorDoArtigo
                        art.save()
                        artigo=art

                        print("ArtigoEMConferencia salvo com Sucesso")

                    for i in autores.split(" ; "):
                        i= i.strip()
                        profCurrent = DadosDeProfessor.objects.filter(nome=i);

                        if(profCurrent.__len__()>0):
                            professor = profCurrent[0].professorDados
                            if(professor):
                                artigo.professores.add(professor)
                        else:
                            print("Professor nao e da DACOM")


def findProfilePhoto():
    import shutil
    util ="/home/humberto/Documentos/projectUtfpr/desenvolvimento/lattes/scriptLattesV8.10/data/cache-lattes/"
    diretorios = os.listdir(util)

    j=0
    for pasta in diretorios:

        if(pasta.__contains__("_files")):
            print(pasta[0:16])
            idLattes = pasta[0:16]
            print(idLattes)

            indice = os.listdir(util+pasta+"/")
            for i  in indice:
                if (i.__contains__("servletrecuperafoto")):

                    prof = Professor.objects.get(lattes=idLattes)
                    print(prof.nome);
                    print(prof.lattes);
                    print(idLattes);
                    # os.rename(i,util+pasta+"/servletrecuperafoto"+str(j)+".jpg" )
                    shutil.copy(util+pasta+"/servletrecuperafoto"+str(j)+".jpg", "/home/humberto/Documentos/projectUtfpr/desenvolvimento/static/")
                    prof.profile_image="/static/servletrecuperafoto"+str(j)+".jpg"
                    prof.save()
                    j+=1


                    # prof.profile_image.save(name= "servletrecuperafoto.img", File(open("/home/humberto/Documentos/projectUtfpr/desenvolvimento/static/img/profilePhoto")), save()))
                # elif(i.__contains__("servletrecuperafoto")):
                #     try:
                #         shutil.copy(util+pasta+"/servletrecuperafoto"+str(j)+".jpg", "/home/humberto/Documentos/projectUtfpr/desenvolvimento/static/")
                #         j+=1
                #         prof.profile_image="/static/servletrecuperafoto"+str(j)+".jpg"
                #         prof.save()
                #     except  IOError:
                #         print("")

#NAO FAZER
def cadastrarDisciplina():
    url = 'http://www.utfpr.edu.br/campomourao/cursos/bacharelados/Ofertados-neste-Campus/ciencia-da-computacao/ementario-e-carga-horaria-das-disciplinas'
    page = requests.get(url)
    html = page.content
    soup = BeautifulSoup(html)

    materias = soup.find('div', attrs={'id': 'parent-fieldname-text-22101d6136a200e0702b6f79331e3fd7'})
    # print (table.prettify())
    i=0

    for dadosDaMateria in materias.strings:
        # print(dadosDaMateria)
        novaDisciplina = Disciplina()
        if(i%4==0):
            # i=0
            novaDisciplina.nome=dadosDaMateria
            print(dadosDaMateria)
        # if(i%4==1):
        #     cargahoraria = dadosDaMateria.split(" ")
        #     print(cargahoraria)
        #     # novaDisciplina.cargaHorariaTeorica=cargahoraria[0]
        #     # novaDisciplina.cargaHorariaPratica=cargahoraria[1]
        #     # novaDisciplina.cargaHorariaAPS=cargahoraria[2]
        #     # novaDisciplina.cargaHorariaTA=cargahoraria[3]
        # # if(i%4==2):
        #
        # if(i%4==2):
        #       ementa = dadosDaMateria.split("Ementa:")
              # novaDisciplina.ementa = ementa[2]
              # print(ementa)
        i+=1


def cadastrarDisciplinasStatic():
    # pass
    novaDisciplina = Disciplina(nome="Algoritmos", sigla="BCC31A", ementa="Resolução de Problemas. Introdução a algoritmos. Variáveis, constantes, tipos e expressões. Entrada e saída simples. Estruturas de controle. Modularização e passagem de parâmetro. Estruturas de dados homogêneas. Cadeias de caracteres.",
                                descricao="Pré-requisito: Sem pré-requisito",cargaHorariaPratica="34",  cargaHorariaTeorica="85",
                                cargaHorariaAPS="7", cargaHorariaTotal="126", cursoDaDisciplina=1, departamentoAcademico=1)
    novaRelacao = RelacaoDisciplinaCurso(periodo="1", tipo="FP", cursoRelacao=1, disciplina=1)

    novaDisciplina.save()
    novaRelacao.save()

if __name__ == "__main__":
    # executeLattes()
    initSistem()
    executeLeitorXML()
    findProfilePhoto()
    cadastrarDisciplinasStatic()
    cadastrarDisciplina()
