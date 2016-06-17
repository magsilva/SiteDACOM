# -*- coding: UTF-8 -*-
# -*- encoding: UTF-8 -*-
# Create your tests here.
from desenvolvimento.models import Projeto
#
import parserDosTestesProjeto
from django.test import TestCase


class ProfessorTestCase(TestCase):
    def setUp(self):
      parserDosTestesProjeto.executar("/home/humberto/Documentos/projectUtfpr/desenvolvimento/test/dadosIndividuais/AlessandroKramer/AlessandroKramer1.xml")

    def testPossuiProfessor(self):
        proj = Projeto.objects.get(nome="CArS - Convergence Area Scheduler")
        self.assertEquals(proj.nome, 'CArS - Convergence Area Scheduler')
