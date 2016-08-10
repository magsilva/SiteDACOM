
# -*- coding: UTF-8 -*-
# -*- encoding: UTF-8 -*-
from __future__ import absolute_import
from __future__ import print_function

import re
from desenvolvimento.models import Projeto

def executar(file):
    descricao = u"Descrição:"
    resumo = u""
    situacao=u"Situação:"
    natureza =u"Natureza:"
    integrantes=u"Integrantes:"

    proj = None
    nome = ""
    ano_conclusao = ""
    ano_inicio = ""
    resumo = ""
    situacao = "0"
    natureza = ""
    integrantes = ""
    desc = ""

    import xml.etree.ElementTree as et
    tree = et.parse(file)
    root = tree.getroot()
    for child in root.iter("projeto"):
        if child.find('ano_inicio').text is not None:
            ano_inicio = child.find('ano_inicio').text
        if child.find('ano_conclusao').text is not None:
            ano_conclusao = child.find('ano_conclusao').text
        if child.find('nome').text is not None:
            nome = child.find('nome').text
        if child.find('descricao').text is not None:
            descricaodoprojeto = child.find('descricao').text
          # print(descricao.find(descricao))
            m = re.search("(Descrição: (?P<desc>.*))? (Situação: (?P<status>.*))? (Natureza: (?P<nat>.*))? (?:Alunos envolvidos: (?P<envolvidos>.*))? (Integrantes: (?P<integrantes>.*))? (?:Financiador\(es\): (?P<financ>.*))?", descricaodoprojeto.encode("utf-8"))

            # projeto = Projeto(nome= nome,datadefim = ano_conclusao, datainicio = ano_inicio)
            # projeto.save()

            proj = None
            nome= ""
            ano_conclusao=""
            ano_inicio =""
            resumo =""
            situacao="0"
            natureza =""
            integrantes=""
            desc=""

            if ano_conclusao =='Atual':
                ano_conclusao='2016'
            if ano_inicio == 'Atual':
                ano_inicio='2016'


            if m is not None:
                desc = m.group('desc')
                situacao = m.group('status')
                natureza = m.group('nat')
                integrantes = m.group('integrantes')

                # Projeto.objects.create(nome= nome,datadefim = ano_conclusao, datainicio = ano_inicio, resumo=desc, situacao=situacao, natureza=natureza)
                projeto = Projeto(nome= nome,datadefim = ano_conclusao, datainicio = ano_inicio, resumo=desc, situacao=situacao, natureza=natureza)
                projeto.save()
