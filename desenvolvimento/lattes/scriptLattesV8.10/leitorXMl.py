from __future__ import print_function
from subprocess import call
import subprocess
from xml.etree import ElementTree as ET
import xml.etree.cElementTree as et
import csv
import sys
import mysql.connector
import sys
import shutil
import Levenshtein
import os, errno
import warnings
# from MySQL import *


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


class Departamento(object):
    nome, sigla = None, None

    def __init__(self):
        self.nome = None
        self.sigla = None

        # def __lt__(self, other):
        #     if self.nome!=other.nome:
        #         return self.nome
        #     if self.sigla!=other.sigla:
        #         return self.sigla


class Professor(object):
    nome, email, telefone, departamento, funcao, \
    lattes, bolsaProdutividade, enderecoProfissional, \
    nomeEmCitacoesBibliograficas, textoResumo = None, None, None, \
                                                None, None, None, None, None, None, None

    def __init__(self):
        self.nome = None
        self.email = None
        self.telefone = None
        self.departamento = None
        self.funcao = None
        self.lattes = None
        self.bolsaProdutividade = None
        self.enderecoProfissional = None
        self.nomeEmCitacoesBibliograficas = None
        self.textoResumo = None


class Formacao(object):
    anoInicio, anoConclusao, tipo, descricao = None, None, None, None

    def __init__(self):
        self.ano_inicio = None
        self.ano_conclusao = None


class AreaDeAtuacao(object):
    descricao = None

    def __index__(self):
        self.descricao = None


class Curso(object):
    nome, sigla = None, None

    def __init__(self):
        self.nome = None
        self.sigla = None


class Coordenacao(object):
    coordenador, suplente, curso = None, None, None

    def __init__(self):
        self.coordenador = None
        self.suplente = None
        self.curso = None


class Artigo(object):
    listaDeAutores, titulo, data, doi, paginas, resumo = None, None, None, None, None, None

    def __init__(self):
        self.data = None
        self.doi = None
        self.listaDeAutores = None
        self.paginas = None
        self.resumo = None
        self.titulo = None


class ArtigoEmPeriodico(Artigo):
    nomeJournal, ISSN, publisher, numero, volume = None, None, None, None, None

    def __init__(self):
        super().__init__()
        self.titulo = None
        self.resumo = None
        self.paginas = None
        self.listaDeAutores = None
        self.data = None
        self.doi = None
        self.ISSN = None
        self.nomeJournal = None
        self.numero = None
        self.publisher = None


class ArtigoEmConferencia(Artigo):
    nomedaConferencia, ISSN, ISBN, local = None, None, None, None

    def __init__(self):
        super().__init__()
        self.titulo = None
        self.ISSN = None
        self.data = None
        self.doi = None
        self.listaDeAutores = None
        self.ISBN = None
        self.local = None
        self.paginas = None
        self.nomedaConferencia = None
        self.resumo = None


class Projeto(object):
    listadeCoordenadores, listaColaboradores, dataInicio, datadeFim, \
    AgendaFinanciadora, nome, resumo = None, None, None, None, None, None, None

    def __init__(self):
        self.listaColaboradores = None
        self.resumo = None
        self.AgendaFinanciadora = None
        self.datadeFim = None

        self.dataInicio = None
        self.nome = None
        self.resumo = None


class Evento(object):
    doi, autores, titulo, nomeEvento, ano, volume, paginas = None, None, None, None, None, None, None

    def __init__(self):
        self.doi
        self.autores
        self.titulo
        self.nomeEvento
        self.ano
        self.volume
        self.paginas


def utfpr():
    print("Deu Certo")
    return None


def executeLattes():
    call("python scriptLattes.py ./data/scriptlattes-utfpr-cm-dacom.config", shell=True)


def executeLeitorXML():

	# xmldoc = ET.parse("data/lattes-site/database.xml")
	# root = xmldoc.getroot()
     #    tm = root.find('curriculo_lattes')
    fd = open('data/lattes-site/database.xml')
    parsedXML = et.parse(fd)
    pesquisador = parsedXML.find('curriculo_lattes')
    print(pesquisador)
    # for pesquisadorNode  in pesquisador:
    #     s = pesquisadorNode.attr('nome_inicial')
    #     print(s)
        # print(pesquisadorNode)
        # print(pesquisadorNode)
        # # pesquisadorNode2 = dict((attr.tag, attr.text) for attr in pesquisadorNode)
        # print ('-----------')
        # print ('Nome:' + pesquisadorNode2['nome_inicial'])
    # print(alunos)
    # print(tm)

        # for i in tm.findAll():
        #     print(i)

        # for i  in fg.find
     #  tm = roo
     # tm = roota.find('curriculo_lattes')

            # print(i)
    # print(tm)
    # for i  in parsedXML.findall('pesquisador'):
    #     s =i.
    #     print(s)
        # print(i)
    # alunos = parsedXML.findall('')
    #     id = prof.prof.getElementsByTagName("nome_inicial")[0]
    #     print(id)
    # id = prof.getAttribute('id')
    # print(id.firstChild.data)
    # p =  dict((attr.tag, attr.text) for attr in prof)
    # print ('-----------')
    # print( 'Nome:', p['id'])

if __name__ == "__main__":
    # abrindoCOnexao
    # con = mysql.connector.connect(user='root', passwd='root', database='UTFPR')
    # c = con.cursor()
    # c.close();
    # con.close();
    # executeLattes()
    executeLeitorXML()






    # print ("python scriptLattesV8.10/scriptLattes.py ./desenvolvimento/lattes/data/scriptLattes.config")



    # if len(sys.argv) != 1:
    #     print
    #     "Parametros insuficientes. Informe o nome de arquivo de entrada e o nome do arquivo de saida"
    #     sys.exit(1)
    # utfpr()
    # print("Deu certo")
    # converter = utfpr()
    # converter.convert(sys.argv[1], sys.argv[2], "epsilon")
#
# if __name__ == "__main__":
#     # # x = .parse('lattes/data/lattes-site/database.xml')
# CurriculoLattes = x.documentElement
# pesquisador = [Prof for Prof in CurriculoLattes.childNodes if Prof.nodeType == x.ELEMENT_NODE]
#
# # AbrindoConexao
# con = mysql.connector.connect(user='root', passwd='root', database='UTFPR')
# c = con.cursor()
#
# for prof in pesquisador:
#     id = prof.getAttribute('id')
#     nome_inicial = prof.getElementsByTagName("nome_inicial")[0]
#     sexo = prof.getElementsByTagName("sexo")[0]
#     nomeemCItacoes = prof.getElementsByTagName("nome_citacao_bibliografica")[0]
#


# sql = "INSERT INTO desenvolvimento_funcionario(nome, email, telefone, departamento_id, funcao) " \
#       "VALUES ( '%s', '%s', '%s', '%d', '%s' )" % (nome_inicial.firstChild.data, ' ', ' ', 1, 'Professor')
# c.execute(sql)
# con.commit()




# sql="INSERT INTO desenvolvimento_funcionario(nome, email, telefone, departamento_id, funcao) " \
# "VALUES ( '%s', '%s', '%s', '%d', '%s' )"  %(nome_inicial.firstChild.data, ' ', ' ', 1, 'Professor')
# c.execute(sql);
# # c.commit();
# con.commit();
# c.close();
# con.close()


# c.execute(
# sql = "INSERT INTO desenvolvimento_professor (nome, departamento_id, funcao, lattes,  nomeEmCitacoesBibliograficas) VALUES ('%s' , %d , '%s', '%s', '%s')" % (
#     nome_inicial.firstChild.data, 1, 'Professor', id, nomeemCItacoes.firstChild.data)
# c.execute(sql)
#
# # nome = models.CharField('Nome', max_length=100)
# #    email = models.CharField('E-mail', max_length=200)
# #    telefone = models.CharField('Telefone', max_length=20)
# #    departamento = models.ForeignKey(DepartamentoAcademico)
# #    funcao = models.CharField('Funcao', max_length=100)
# #    lattes = models.CharField('Link do Lattes', max_length=50)
# #    bolsaProdutividade = models.CharField('Bolsa Produtividade', max_length=100)
# #    enderecoProfissional = models.CharField('Endereco Profissional', max_length=5000)
# #    nomeEmCitacoesBibliograficas = models.CharField('nomeEmCitacoesBibliograficas', max_length=255)
# #    textoRe
# # print(sql)
# con.commit()
#
# # c.close()
# # con.close()
# projeto = prof.getElementsByTagName("projeto")
# for proj in projeto:
#     try:
#         ano_inicio = proj.getElementsByTagName('ano_inicio')[0]
#         print('--> %s' % ano_inicio.firstChild.data)
#     except IndexError:
#         ano_inicio = ""
#     try:
#         ano_conclusao = proj.getElementsByTagName('ano_conclusao')[0]
#     except IndexError:
#         ano_conclusao = ""
#     try:
#         nome = proj.getElementsByTagName('nome')[0]
#     except IndexError:
#         nome = ""
#     try:
#         desc = proj.getElementsByTagName('descricao')[0]
#     except IndexError:
#         desc = ""
#         # print('--> %s' % ano_inicio.firstChild.data)
#
#         # con = mysql.connector.connect(user='root', passwd='root', database='UTFPR')
#         # c = con.cursor()
#         # # sql = "INSERT INTO desenvolvimento_projeto (dataInicio, datadeFim, nome, resumo) VALUES ('%s' , '%s', '%s' , '%s')" % (
#         # #     ano_inicio.firstChild.data, ano_conclusao.firstChild.data, nome.firstChild.data, desc.firstChild.data)
#         # c.execute(
#         # "INSERT INTO desenvolvimento_projeto (dataInicio, listadeCoordenadores,listaColaboradores, AgendaFinanciadora,"
#         # " datadeFim, nome, resumo)"
#         #     " VALUES ('%s' , '%s', '%s', '%s',  '%s', '%s' , '%s')"
#     % ( ano_inicio.firstChild.data, '', '', '', ano_conclusao.firstChild.data, nome.firstChild.data,
#             #         desc.firstChild.data))
# con.commit()
# c.close()
# con.close()  # artigos = prof.getElementsByTagName("artigos_em_periodicos")  # for art in artigos:  # # try:  # doi = art.getElementsByTagName('doi')[0]
# # # except IndexError, TypeError:
# # #     doi. = ""
# # # try:
#     titulo = art.getElementsByTagName('titulo')[0]
#     # except IndexError,  TypeError:
#     #     titulo = ""
#     # try:
#     autores = art.getElementsByTagName('autores')[0]
#     # except IndexError,  TypeError:
#     #     nome = ""
#     # try:
#     revista = art.getElementsByTagName('revista')[0]
#     # except IndexError,  TypeError:
#     #     revista = ""
#     # try:
#     volume = art.getElementsByTagName('volume')[0]
#     # except IndexError,  TypeError:
#     #     volume = ""
#     # try:
#     paginas = art.getElementsByTagName('paginas')[0]
#     # except IndexError,  TypeError:
#     #     paginas = ""
#     # try:
#     numero = art.getElementsByTagName('numero')[0]
#     # except IndexError,  TypeError:
#     #     numero = ""
#     # try:
#     ano = art.getElementsByTagName('ano')[0]
#     # except IndexError,  TypeError:
#     #     ano = ""
#
# # con = mysql.connector.connect(user='root', passwd='root', database='UTFPR')
# # c = con.cursor()
# # sql = "INSERT INTO desenvolvimento_artigo (titulo, listadeAutores, data, doi, paginas) VALUES ( '%s', '%s' ,'%s', '%s', '%s')" % \
# #       titulo.firstChild.data, autores.firstChild.data, ano.firstChild.data, doi.firstChild.data, paginas.firstChild.data
# #
# # sql2 = "SELECT id FROM desenvolvimento_artigo WHERE '%s " % titulo.firstChild.data
# #
# # sql3 = "INSERT INTO desenvolvimento_artigoemperiodico (artigo_ptr_id, nomeJournal, numero, volume) VALUES ('%s' , '%s', '%s' , '%s')" % (
# #     sql2, revista.firstChild.data, numero.firstChil.data, volume.firstChild.data)
# #
# # c.execute(sql)
# # con.commit()
# # c.execute(sql2)
# # con.commit()
# # c.execute(sql3)
# # con.commit()
# # c.close()
# # con.close()
#
#
#
# # paginaInicio = paginas.__getslice__()
# # con = mysql.connector.connect(user='root', passwd='root', database='UTFPR')
# # c = con.cursor()
# # sql = "INSERT INTO desenvolvimento_artigo (titulo, data, doi, paginaInicial, paginaFinal, Resumo) VALUES ('%s' , '%s', '%s' , '%s')" % (ano_inicio.firstChild.data, ano_conclusao.firstChild.data, nome.firstChild.data, desc.firstChild.data)
# # c.execute(sql)
# # con.commit()
# # c.close()
# # con.close()
#
# # con = mysql.connector.connect(user='root', passwd='root', database='UTFPR')
# # c = con.cursor()
# # sql = "INSERT INTO desenvolvimento_projeto (dataInicio, datadeFim, nome, resumo) VALUES ('%s' , '%s', '%s' , '%s')" % (ano_inicio.firstChild.data, ano_conclusao.firstChild.data, nome.firstChild.data, desc.firstChild.data)
# # c.execute(sql)
# # con.commit()
# # c.close()
# # con.close()
#
# # print ("%s" %titulo.childNodes[0].data)
# # print ("%s" %ano_inicio.childNodes[0].data)
# #
# # print ("%s" %ano_conclusao.childNodes[0].data)
# #
# # print ("%s" %nome.childNodes[0].data)
# #
# # print ("%s" %desc.childNodes[0].data)
#
#
#
# # projetos_pesquisa = [p for p in prof.childNodes if  p.nodeType == prof.ELEMENT_NODE]
# # for po in projetos_pesquisa:
# # projeto = [pr for pr in po.childNodes if pr.nodeType == po.ELEMENT_NODE]
# # print("%s" %po)
# #
# # for pa in projeto:
# #         #print("%s" %pa)
# #
# #         ano  = pa.getElementsByTagName("ano_inicio")[0]
# #         print("%s" %ano.firstChild.data)
# #              # projeto = prof.getElementsByTagName("projeto")[0]
# # #print("%s" % ano.firstChild.data)
# # # for pr in projeto:
# # #
# # #     ano = pr.projeto.getElementsByTagName("ano_inicio")[0]
# # #     #ano  = projeto.getElementsByTagName("ano_inicio")[0]
# #     for a in projeto:
# #         print("%s" % a.getElementsByTagName("ano_inicio")[0].getfirstChild.data)
# # except IndexError:
# #     ano_inicio = ""
# # ano_inicio:
#
#
# # projeto = prof.getElementsByTagName("projeto")[0]
# # for p in projeto :
# #     ano_inicio = p.getElementsByTagName("ano_inicio")[0]
# # #for p  in ano_inicio:
# #     print("%s" % ano_inicio.firstChild.data)
#
# # print'-----> %s' % sexo.firstChild.data
# # print '---->%s' % endereco_profissional.firstChild.data
# # print '-->'
#
#
#
#
# #  projeto=CurriculoLattes.documentElement
#
# #projetos_pesquisa = prof.getElementsByTagName("projetos_pesquisa")
# #print ("%s") %projetos_pesquisa.childNodes.data
# #
# # projeto  = [ p for p in CurriculoLattes.childNodes if p.nodeType == x.ELEMENT_NODE]
# # #projeto = [projs for projs in prof.childNodes if projs.nodeType == CurriculoLattes.ELEMENT_NODE]
# #
# # for projet in projeto:
# #     #projetos_pesquisa = CurriculoLattes.documentElement
# #     projetos_pesquisa = projet.getElementsByTagName("projetos_pesquisa")
# #
# #     #projeto = projet.firstChild.childNodes
# #     # for p in projeto:
# #     #projs = projeto.getElementsByTagName('projetos_pesquisa')
# #     ano_inicio = projetos_pesquisa.getElementsByTagName("ano_inicio")[0]
# #     #.getAttribute("ano_inicio")
# #     #
# #     #try:
# #     #   ano_conclusao = projeto.getElementsBytagName("ano_conclusao")
# #     #catch():
# #     #ano_conclusao = ""
# #     # nomeDoProjeto = p.getElementsByTagName("nome")
# #     # descricao = p.getElementsByTagName("descricao")
# #
# #     #    print
# #     #print("%s") % p.firstChild.data
# #     print("%s" % ano_inicio.firstChild.data)
# #     # print(  "---> %s" % ano_conclusao.firstChild.data)
# #     # print ('-----> %s' % nomeDoProjeto)
# #     # print ('---->%s' % descricao)
# #     #     # nome_completo = ident.getElementsBytagName('nome_completo')
# #     # staff.getElementsByTagName("salary")[0]
# #     # print "----> %s" % ident
