# -*- coding: UTF-8 -*-
# -*- encoding: UTF-8 -*-
from django.test import TestCase

# Create your tests here.
from desenvolvimento.models import Projeto
import re

from django.test import TestCase
from desenvolvimento.models import Professor

class ProfessorTestCase(TestCase):
    def setUp(self):
        Professor.objects.create(nome="Marco Aurelio Graciotto Silva", email="magsilva@utfpr.edu.br")

    def testPossuiProfessor(self):
        prof = Professor.objects.get(nome="Marco Aurelio Graciotto Silva")
        self.assertEquals(prof.nome, 'Marco Aurelio Graciotto Silva')

#
#
#
#
# class ProjetoTestCase(TestCase):
#     # def setUp(self):
#     #
#     #     Projeto.objects.create(nome="CArS - Convergence Area Scheduler", datadefim="2016", datainicio="2015",
#     #                            situacao="Em andamento;",natureza="Pesquisa.",
#     #                            resumo="Convergence Area Scheduler is a simulator to evaluate jobs scheduling on scenarios where"
#     #                                   " jobs come from Cloud and are performed within some HPC platform's processors..")
#
#     def testProjetoQueEstaoNaBaseDeDados(self):
#         import xml.etree.ElementTree as et
#         tree = et.parse("test/dadosIndividuais/AlessandroKramer/AlessandroKramer1.xml")
#         root = tree.getroot()
#         for child in root.iter("projeto"):
#             if child.find('ano_inicio').text is not None:
#                 ano_inicio = child.find('ano_inicio').text
#             if child.find('ano_conclusao').text is not None:
#                 ano_conclusao = child.find('ano_conclusao').text
#             if child.find('nome').text is not None:
#                 nome = child.find('nome').text
#             if child.find('descricao').text is not None:
#                 descricaodoprojeto = child.find('descricao').text
#
#             m = re.search("(Descrição: (?P<desc>.*))? (Situação: (?P<status>.*))? (Natureza: (?P<nat>.*))? (?:Alunos envolvidos: (?P<envolvidos>.*))? (Integrantes: (?P<integrantes>.*))? (?:Financiador\(es\): (?P<financ>.*))?", descricaodoprojeto.encode("utf-8"))
#
#             proj = None
#             if ano_conclusao =='Atual':
#                 ano_conclusao='2016'
#             if ano_inicio == 'Atual':
#                 ano_inicio='2016'
#                 proj = Projeto.objects.create(nome= nome,datadefim = ano_conclusao, datainicio = ano_inicio)
#
#
#             print(nome)
#
#             if m is not None:
#                 print(m.groups())
#                 desc = m.group('desc')
#                 situacao = m.group('status')
#                 natureza = m.group('nat')
#                 integrantes = m.group('integrantes')
#
#                 proj = Projeto.objects.filter(nome =nome)[0]
#                 proj.resumo = desc
#                 proj.situacao = situacao
#                 proj.natureza =natureza
#
#             self.assertEquals(proj.nome,self.nome )
#             self.assertEquals(proj.datainicio, self.datainicio)
#             self.assertEquals(proj.datadefim, self.datadefim)
#             self.assertEquals(proj.situacao, self.situacao)
#             self.assertEquals(proj.natureza, self.natureza)
#             self.assertEquals(proj.resumo, self.resumo)
#
#
#
#
