from __future__ import print_function
import mysql.connector
from xml.dom import minidom
if __name__ == "__main__":
    x = minidom.parse('lattes/data/lattes-site/database.xml')
    CurriculoLattes = x.documentElement
    pesquisador = [Prof for Prof in CurriculoLattes.childNodes if Prof.nodeType == x.ELEMENT_NODE]
    for prof in pesquisador:
        id = prof.getAttribute('id')
        nome_inicial = prof.getElementsByTagName("nome_inicial")[0]
        sexo = prof.getElementsByTagName("sexo")[0]
        endereco_profissional = prof.getElementsByTagName("endereco_profissional")[0]
        # print('--> %s' % id)
        # print("---> %s" % nome_inicial.firstChild.data)

        projeto = prof.getElementsByTagName("projeto")
        for proj in projeto:
            try:
                ano_inicio = proj.getElementsByTagName('ano_inicio')[0]
            except IndexError:
                ano_inicio =""
            try:
                ano_conclusao= proj.getElementsByTagName('ano_conclusao')[0]
            except IndexError:
                ano_conclusao =""
            try:
               nome = proj.getElementsByTagName('nome')[0]
            except IndexError:
                nome =""
            try:
                desc = proj.getElementsByTagName('descricao')[0]
            except IndexError:
                desc =""

            # con = mysql.connector.connect(user='root', passwd='root', database='UTFPR')
            # c = con.cursor()
            # sql = "INSERT INTO desenvolvimento_projeto (dataInicio, datadeFim, nome, resumo) VALUES ('%s' , '%s', '%s' , '%s')" % (ano_inicio.firstChild.data, ano_conclusao.firstChild.data, nome.firstChild.data, desc.firstChild.data)
            # c.execute(sql)
            # con.commit()
            # c.close()
            # con.close()

        artigos = prof.getElementsByTagName("artigos_em_periodicos")
        for art in artigos:
            try:
                doi = art.getElementsByTagName('doi')[0]
            except IndexError:
                doi =""
            try:
                titulo =  art.getElementsByTagName('titulo')[0]
            except IndexError:
                titulo =""
            try:
               autores = art.getElementsByTagName('autores')[0]
            except IndexError:
                nome =""
            try:
                revista = art.getElementsByTagName('revista')[0]
            except IndexError:
                revista =""
            try:
                volume= art.getElementsByTagName('volume')[0]
            except IndexError:
                volume =""
            try:
                paginas = art.getElementsByTagName('paginas')[0]
                paginaInicial= ''
                paginaFinal=''
                for a in paginas.firstChild.data:
                    paginaInicial = paginas+a
                for a in paginas.firstChild.data:
                         paginaInicial = paginaInicial+a

                    # print("--->  %s" % paginaInicial)
                    # else:
                        # num = len(paginaInicial)
                        # paginaFinal = paginas[num+1:]
                        # print("---> %s " %  paginaFinal
            except IndexError:
                paginas =""

            try:
                numero = art.getElementsByTagName('numero')[0]
            except IndexError:
                numero =""
            try:
                ano = art.getElementsByTagName('ano')[0]
            except IndexError:
                ano =""

            # paginaInicio = paginas.__getslice__()
            # con = mysql.connector.connect(user='root', passwd='root', database='UTFPR')
            # c = con.cursor()
            # sql = "INSERT INTO desenvolvimento_artigo (titulo, data, doi, paginaInicial, paginaFinal, Resumo) VALUES ('%s' , '%s', '%s' , '%s')" % (ano_inicio.firstChild.data, ano_conclusao.firstChild.data, nome.firstChild.data, desc.firstChild.data)
            # c.execute(sql)
            # con.commit()
            # c.close()
            # con.close()

                # con = mysql.connector.connect(user='root', passwd='root', database='UTFPR')
                # c = con.cursor()
                # sql = "INSERT INTO desenvolvimento_projeto (dataInicio, datadeFim, nome, resumo) VALUES ('%s' , '%s', '%s' , '%s')" % (ano_inicio.firstChild.data, ano_conclusao.firstChild.data, nome.firstChild.data, desc.firstChild.data)
                # c.execute(sql)
                # con.commit()
                # c.close()
                # con.close()

            #print ("%s" %titulo.childNodes[0].data)
            # print ("%s" %ano_inicio.childNodes[0].data)
            #
            # print ("%s" %ano_conclusao.childNodes[0].data)
            #
            # print ("%s" %nome.childNodes[0].data)
            #
            # print ("%s" %desc.childNodes[0].data)



        # projetos_pesquisa = [p for p in prof.childNodes if  p.nodeType == prof.ELEMENT_NODE]
        # for po in projetos_pesquisa:
        #     projeto = [pr for pr in po.childNodes if pr.nodeType == po.ELEMENT_NODE]
        #     print("%s" %po)
        #
        #     for pa in projeto:
        #         #print("%s" %pa)
        #
        #         ano  = pa.getElementsByTagName("ano_inicio")[0]
        #         print("%s" %ano.firstChild.data)
        #              # projeto = prof.getElementsByTagName("projeto")[0]
        # #print("%s" % ano.firstChild.data)
        # # for pr in projeto:
        # #
        # #     ano = pr.projeto.getElementsByTagName("ano_inicio")[0]
        # #     #ano  = projeto.getElementsByTagName("ano_inicio")[0]
        #     for a in projeto:
        #         print("%s" % a.getElementsByTagName("ano_inicio")[0].getfirstChild.data)
    # except IndexError:
    #     ano_inicio = ""
        # ano_inicio:


        # projeto = prof.getElementsByTagName("projeto")[0]
        # for p in projeto :
        #     ano_inicio = p.getElementsByTagName("ano_inicio")[0]
        # #for p  in ano_inicio:
        #     print("%s" % ano_inicio.firstChild.data)

        # print'-----> %s' % sexo.firstChild.data
        # print '---->%s' % endereco_profissional.firstChild.data
        # print '-->'




        #  projeto=CurriculoLattes.documentElement

        #projetos_pesquisa = prof.getElementsByTagName("projetos_pesquisa")
        #print ("%s") %projetos_pesquisa.childNodes.data
        #
        # projeto  = [ p for p in CurriculoLattes.childNodes if p.nodeType == x.ELEMENT_NODE]
        # #projeto = [projs for projs in prof.childNodes if projs.nodeType == CurriculoLattes.ELEMENT_NODE]
        #
        # for projet in projeto:
        #     #projetos_pesquisa = CurriculoLattes.documentElement
        #     projetos_pesquisa = projet.getElementsByTagName("projetos_pesquisa")
        #
        #     #projeto = projet.firstChild.childNodes
        #     # for p in projeto:
        #     #projs = projeto.getElementsByTagName('projetos_pesquisa')
        #     ano_inicio = projetos_pesquisa.getElementsByTagName("ano_inicio")[0]
        #     #.getAttribute("ano_inicio")
        #     #
        #     #try:
        #     #   ano_conclusao = projeto.getElementsBytagName("ano_conclusao")
        #     #catch():
        #     #ano_conclusao = ""
        #     # nomeDoProjeto = p.getElementsByTagName("nome")
        #     # descricao = p.getElementsByTagName("descricao")
        #
        #     #    print
        #     #print("%s") % p.firstChild.data
        #     print("%s" % ano_inicio.firstChild.data)
        #     # print(  "---> %s" % ano_conclusao.firstChild.data)
        #     # print ('-----> %s' % nomeDoProjeto)
        #     # print ('---->%s' % descricao)
        #     #     # nome_completo = ident.getElementsBytagName('nome_completo')
        #     # staff.getElementsByTagName("salary")[0]
        #     # print "----> %s" % ident