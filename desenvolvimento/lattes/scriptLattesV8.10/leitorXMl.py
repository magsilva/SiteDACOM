from __future__ import print_function
from subprocess import call
import subprocess
import xml.etree.cElementTree as et
import csv
import sys
import mysql.connector
import sys
import shutil
# import Levenshtein
import os, errno
import warnings

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
    nome, sigla = "", ""

    def __init__(self):
        self.nome = ""
        self.sigla = ""


class Professor(object):
    nome, email, telefone, departamento, funcao, \
    lattes, bolsaProdutividade, enderecoProfissional, \
    nomeEmCitacoesBibliograficas, textoResumo, enderecoProfissional_lat, enderecoProfissional_long = "", "", "", "", "", "", "", "", "", "", "", ""

    def __init__(self):
        self.nome = ""
        self.email = ""
        self.telefone = ""
        self.departamento = None
        self.funcao = ""
        self.lattes = ""
        self.bolsaProdutividade = ""
        self.enderecoProfissional = ""
        self.nomeEmCitacoesBibliograficas = ""
        self.textoResumo = ""


class Formacao(object):
    anoInicio, anoConclusao, tipo, descricao = "", "", "", ""

    def __init__(self):
        self.anoInicio = ""
        self.anoConclusao = ""
        self.tipo = ""
        self.descricao = ""


class AreaDeAtuacao(object):
    descricao = ""

    def __index__(self):
        self.descricao = ""


class Curso(object):
    nome, sigla = "", ""

    def __init__(self):
        self.nome = ""
        self.sigla = ""


class Coordenacao(object):
    coordenador, suplente, curso = "", "", ""

    def __init__(self):
        self.coordenador = ""
        self.suplente = ""
        self.curso = ""


class Artigo(object):
    listaDeAutores, titulo, data, doi, paginas, resumo = "", "", "", "", "", ""

    def __init__(self):
        self.data = ""
        self.doi = ""
        self.listaDeAutores = ""
        self.paginas = ""
        self.resumo = ""
        self.titulo = ""


class ArtigoEmPeriodico(Artigo):
    nomeJournal, ISSN, publisher, numero, volume = "", "", "", "", ""

    def __init__(self):
        super().__init__()
        self.titulo = "",
        self.resumo = ""
        self.paginas = "",
        self.listaDeAutores = ""
        self.data = ""
        self.doi = ""
        self.ISSN = ""
        self.nomeJournal = ""
        self.numero = ""
        self.publisher = ""


class ArtigoEmConferencia(Artigo):
    nomedaConferencia, ISSN, ISBN, local = "", "", "", ""

    def __init__(self):
        super().__init__()
        self.titulo = ""
        self.ISSN = ""
        self.data = ""
        self.doi = ""
        self.listaDeAutores = ""
        self.ISBN = ""
        self.local = ""
        self.paginas = ""
        self.nomedaConferencia = ""
        self.resumo = ""


class Projeto(object):
    listadeCoordenadores, listaColaboradores, dataInicio, datadeFim, \
    AgendaFinanciadora, nome, resumo = "", "", "", "", "", "", ""

    def __init__(self):
        self.listaColaboradores = ""
        self.resumo = ""
        self.AgendaFinanciadora = ""
        self.datadeFim = ""
        self.dataInicio = ""
        self.nome = ""
        self.resumo = ""


class Evento(object):
    doi, autores, titulo, nomeEvento, ano, volume, paginas = "", "", "", "", "", "", ""

    def __init__(self):
        self.doi = ""
        self.autores = ""
        self.titulo = ""
        self.nomeEvento = ""
        self.ano = ""
        self.volume = ""
        self.paginas = ""


def utfpr():
    print("Deu Certo")
    return None


def executeLattes():
    call("python scriptLattes.py ./data/scriptlattes-utfpr-cm-dacom.config", shell=True)


def executeLeitorXML():
    # abrindoCOnexao

    config = {
        'user': 'root',
        'passwd': 'root',
        'database': 'UTFPR'
    }

    connection = mysql.connector.connect(**config)
    conector = connection.cursor()

    fd = open("data/lattes-site/database.xml")
    parsedXML = et.parse(fd)
    curriculo_lattes = parsedXML.findall("pesquisador")
    # definindo Arrays
    professor = []
    projetoPesquisa = []
    artigos = []
    artigosEmPeriodico = []
    artigosEmConferencia = []

    for i in curriculo_lattes:
        # if i.findall('identificacao') is not None:
        # p.lattes = i.attrib['id']
        for a in i.findall('identificacao'):
            if a.find('nome_inicial').text is not None:
                nome_inicial = a.find('nome_inicial').text
            if a.find('nome_completo').text is not None:
                nome_completo = a.find('nome_completo').text
            if a.find('nome_citacao_bibliografica').text is not None:
                nome_citacao_bibliografica = a.find('nome_citacao_bibliografica').text
            if a.find('sexo').text is not None:
                sexo = a.find('sexo').text
                # p = Professor()

                # p.nome = nome_inicial
                # p.nome_completo = nome_completo
                # p.nomeEmCitacoesBibliograficas = nome_citacao_bibliografica
                # p.sexo = sexo
                # p.departamento = 1
                # p.funcao = "Professor"
                #
                # professor.append(p)

        for b in i.find('endereco'):
            if b.find('endereco_profissional') is not None:
                endereco_profissional = b.find('endereco_profissional')
            if b.find('endereco_profissional_lat') is not None:
                endereco_profissional_lat = b.find('endereco_profissional_lat')
            if b.find('endereco_profissional_long') is not None:
                endereco_profissional_long = b.find('endereco_profissional_long')

                # p.enderecoProfissional = endereco_profissional
                # p.enderecoProfissional_lat = endereco_profissional_lat
                # p.enderecoProfissional_long = endereco_profissional_long

                # professor.append(p)

        for c in i.findall('formacao_academica'):
            for d in c.findall('formacao'):
                if d.find('ano_inicio').text is not None:
                    ano_inicio = d.find('ano_inicio').text
                if d.find('ano_conclusao').text is not None:
                    ano_conclusao = d.find('ano_conclusao').text
                if d.find('tipo').text is not None:
                    tipo = d.find('tipo').text
                if d.find('nome_instituicao').text is not None:
                    nome = d.find('nome_instituicao').text
                if d.find('descricao').text is not None:
                    descricao = d.find('descricao').text

        for e in i.findall('projetos_pesquisa'):
            for f in e.findall('projeto'):
                if f.find('ano_inicio').text is not None:
                    ano_inicio = f.find('ano_inicio').text
                if f.find('ano_conclusao').text is not None:
                    ano_conclusao = f.find('ano_conclusao').text
                if f.find('nome').text is not None:
                    nome = f.find('nome').text
                if f.find('descricao').text is not None:
                    descricao = f.find('descricao').text

                projeto = Projeto()
                projeto.dataInicio = ano_inicio
                projeto.datadeFim = ano_conclusao
                projeto.nome = nome
                projeto.resumo = descricao

                # sql = "INSERT INTO desenvolvimento_projeto (nome, resumo, dataInicio, datadeFim,listadeCoordenadores,listaColaboradores,AgendaFinanciadora) VALUES ('%s' , '%s' , '%s', '%s', '%s', '%s', '%s')"  % (projeto.nome, projeto.resumo, projeto.dataInicio, projeto.datadeFim, "", "","")
                # print("INSERT INTO desenvolvimento_projeto (nome, resumo, dataInicio, datadeFim,listadeCoordenadores,listaColaboradores,AgendaFinanciadora) VALUES ('%s' , '%s' , '%s', '%s', '%s', '%s', '%s')"  % (projeto.nome, projeto.resumo, projeto.dataInicio, projeto.datadeFim, "", "","")
                # )

                # print("VACA")
                # conector.execute("Select * from desenvolvimento_projeto")
                # rows = conector.fetchall()
                # for row in rows:
                #     print(row)
                # print ("oi")

                # print(c.execute("select * from desenvolvimento_projeto"))
                conector.execute(
                    "INSERT INTO desenvolvimento_projeto (nome, resumo, dataInicio, datadeFim) VALUES (%s , %s , %s, %s)" % (
                    projeto.nome, projeto.resumo, projeto.dataInicio, projeto.datadeFim))
                connection.commit()

        for g in i.findall('area_atuacao'):
            for h in g.find('descricao'):
                if h.find('descricao').text is not None:
                    descricao = h.find('descricao').text
        for j in i.findall('trabalho_completo_congresso'):  # eventos
            for k in j.findall('trabalho_completo'):
                if k.find('doi').text is not None:
                    doi = k.find('doi').text
                if k.find('autores').text is not None:
                    autores = k.find('autores').text
                if k.find('titulo').text is not None:
                    titulo = k.find('titulo').text
                if k.find('nome_evento').text is not None:
                    nome_evento = k.find('nome_evento').text
                if k.find('ano').text is not None:
                    ano = k.find('ano').text
                if k.find('volume').text is not None:
                    volume = k.find('volume').text
                if k.find('paginas').text is not None:
                    paginas = k.find('paginas').text
        for l in i.findall('resumo_congresso'):
            for m in l.findall('resumo'):
                if m.find('doi').text is not None:
                    doi = m.find('doi').text
                if m.find('autores').text is not None:
                    autores = m.find('autores').text
                if m.find('titulo').text is not None:
                    titulo = m.find('titulo').text
                if m.find('nome_evento').text is not None:
                    nome_evento = m.find('nome_evento').text
                if m.find('ano').text is not None:
                    ano = m.find('ano').text
                if m.find('volume').text is not None:
                    volume = m.find('volume').text
                if m.find('paginas').text is not None:
                    paginas = m.find('paginas').text
                if m.find('numero').text is not None:
                    numero = m.find('numero').text
        for n in i.findall('artigos_em_periodicos'):
            for o in n.findall('artigo'):
                if o.find('doi').text is not None:
                    doi = o.find('doi').text
                if o.find('autores').text is not None:
                    autores = o.find('autores').text
                if o.find('titulo').text is not None:
                    titulo = o.find('titulo').text
                if o.find('revista').text is not None:
                    revista = o.find('revista').text
                if o.find('ano').text is not None:
                    ano = o.find('ano').text
                if o.find('volume').text is not None:
                    volume = o.find('volume').text
                if o.find('paginas').text is not None:
                    paginas = o.find('paginas').text
                if o.find('numero').text is not None:
                    numero = o.find('numero').text


                    # for p in professor:
                    #     print(p.nome)

                    # print(p.nome)

                    # i = 0
                    # for p in professor:
                    #     sql = (
                    #         "UPDATE desenvolvimento_professor SET nome='%s', departamento_id=%d, funcao=%s, lattes=%s, nomeEmCitacoesBibliograficas=%s, enderecoProfissional=%s, endereco_profissional_lat=%s, endereco_profissional_long=%s Where id=%d ",
                    #         (p.nome, p.departamento, p.funcao, p.lattes, p.nomeEmCitacoesBibliograficas, p.enderecoProfissional,
                    #          p.enderecoProfissional_lat, p.enderecoProfissional_long, i))
                    #     i += 1


                    # print(sql)
                    # c.execute(sql)
                    # con.commit()
                    #
                    # % (p.nome, 1, 'Professor', p.lattes, p.nomeEmCitacoesBibliograficas) "
                    # sql= "UPDATE clientes SET nome = 'Rafael', email = 'contato@rlsystem.com.br' WHERE id = 1"



                    # c.close()
                    # con.close()


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



    # print(p.nome)
    # professor.insert(len(professor), p)
    # professor.insert(len(professor), p)

    # professor.append(p)

    # print(p)

    # sql = "INSERT INTO desenvolvimento_professor (nome, departamento_id, funcao, lattes,  nomeEmCitacoesBibliograficas) " \
    #       "VALUES ('%s' , %d , '%s', '%s', '%s')" \
    #       % (p.nome, 1, 'Professor', p.lattes, p.nomeEmCitacoesBibliograficas)
    #
    # print("INSERT INTO desenvolvimento_professor (nome, departamento_id, funcao, lattes,  nomeEmCitacoesBibliograficas) " \
    #   "VALUES ('%s' , %d , '%s', '%s', '%s')" \
    #   % (p.nome, 1, 'Professor', p.lattes, p.nomeEmCitacoesBibliograficas))
    # professor.insert(p,0)
    # c.execute(sql)
    # con.commit()
