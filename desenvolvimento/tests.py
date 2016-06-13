# -*- coding: UTF-8 -*-
# -*- encoding: UTF-8 -*-
from django.test import TestCase

# Create your tests here.
from desenvolvimento.models import Projeto

import parserDosTestesProjeto
from django.test import TestCase


class ProfessorTestCase(TestCase):
    def setUp(self):
        parserDosTestesProjeto()

    def testPossuiProfessor(self):
        proj = Projeto.objects.get(nome="Alessandro Kramer")
        self.assertEquals(proj.nome, 'Alessandro Kramer')
