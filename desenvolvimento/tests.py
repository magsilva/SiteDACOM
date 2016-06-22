# -*- coding: UTF-8 -*-
# -*- encoding: UTF-8 -*-
# Create your tests here.
from desenvolvimento.models import Projeto
#
import parserDosTestesProjeto
from django.test import TestCase


class ProfessorTestCase(TestCase):
    def setUp(self):
        # AlessandroKramer
        parserDosTestesProjeto.executar("/home/humberto/Documentos/projectUtfpr/desenvolvimento/test/dadosIndividuais/AlessandroKramer/1")
        parserDosTestesProjeto.executar("/home/humberto/Documentos/projectUtfpr/desenvolvimento/test/dadosIndividuais/AlessandroKramer/2")
        parserDosTestesProjeto.executar("/home/humberto/Documentos/projectUtfpr/desenvolvimento/test/dadosIndividuais/AlessandroKramer/3")

        parserDosTestesProjeto.executar("/home/humberto/Documentos/projectUtfpr/desenvolvimento/test/dadosIndividuais/Ana Paula Chaves Steinmacher/1")
        parserDosTestesProjeto.executar("/home/humberto/Documentos/projectUtfpr/desenvolvimento/test/dadosIndividuais/Ana Paula Chaves Steinmacher/2")
        parserDosTestesProjeto.executar("/home/humberto/Documentos/projectUtfpr/desenvolvimento/test/dadosIndividuais/Ana Paula Chaves Steinmacher/3")
        parserDosTestesProjeto.executar("/home/humberto/Documentos/projectUtfpr/desenvolvimento/test/dadosIndividuais/Ana Paula Chaves Steinmacher/4")

        # parserDosTestesProjeto.executar("/home/humberto/Documentos/projectUtfpr/desenvolvimento/test/dadosIndividuais/André Luís Schwerz/1")

        parserDosTestesProjeto.executar("/home/humberto/Documentos/projectUtfpr/desenvolvimento/test/dadosIndividuais/Aretha Barbosa Alencar/1")

        parserDosTestesProjeto.executar("/home/humberto/Documentos/projectUtfpr/desenvolvimento/test/dadosIndividuais/Diego Bertolini Gonçalves/1")
        parserDosTestesProjeto.executar("/home/humberto/Documentos/projectUtfpr/desenvolvimento/test/dadosIndividuais/Diego Bertolini Gonçalves/2")
        parserDosTestesProjeto.executar("/home/humberto/Documentos/projectUtfpr/desenvolvimento/test/dadosIndividuais/Diego Bertolini Gonçalves/3")

        parserDosTestesProjeto.executar("/home/humberto/Documentos/projectUtfpr/desenvolvimento/test/dadosIndividuais/Everton Fernando Barros/1")

        # parserDosTestesProjeto.executar("/home/humberto/Documentos/projectUtfpr/desenvolvimento/test/dadosIndividuais/Filipe Roseiro Côgo/1")
        # parserDosTestesProjeto.executar("/home/humberto/Documentos/projectUtfpr/desenvolvimento/test/dadosIndividuais/Filipe Roseiro Côgo/2")
        parserDosTestesProjeto.executar("/home/humberto/Documentos/projectUtfpr/desenvolvimento/test/dadosIndividuais/Filipe Roseiro Côgo/3")

        parserDosTestesProjeto.executar("/home/humberto/Documentos/projectUtfpr/desenvolvimento/test/dadosIndividuais/Igor Fabio Steinmacher/1")
        parserDosTestesProjeto.executar("/home/humberto/Documentos/projectUtfpr/desenvolvimento/test/dadosIndividuais/Igor Fabio Steinmacher/2")
        parserDosTestesProjeto.executar("/home/humberto/Documentos/projectUtfpr/desenvolvimento/test/dadosIndividuais/Igor Fabio Steinmacher/3")
        # parserDosTestesProjeto.executar("/home/humberto/Documentos/projectUtfpr/desenvolvimento/test/dadosIndividuais/Igor Fabio Steinmacher/4")
        # parserDosTestesProjeto.executar("/home/humberto/Documentos/projectUtfpr/desenvolvimento/test/dadosIndividuais/Igor Fabio Steinmacher/5")

        parserDosTestesProjeto.executar("/home/humberto/Documentos/projectUtfpr/desenvolvimento/test/dadosIndividuais/Igor Scaliante Wiese/1")
        # parserDosTestesProjeto.executar("/home/humberto/Documentos/projectUtfpr/desenvolvimento/test/dadosIndividuais/Igor Scaliante Wiese/2")
        # parserDosTestesProjeto.executar("/home/humberto/Documentos/projectUtfpr/desenvolvimento/test/dadosIndividuais/Igor Scaliante Wiese/3")
        # parserDosTestesProjeto.executar("/home/humberto/Documentos/projectUtfpr/desenvolvimento/test/dadosIndividuais/Igor Scaliante Wiese/3")
        parserDosTestesProjeto.executar("/home/humberto/Documentos/projectUtfpr/desenvolvimento/test/dadosIndividuais/Igor Scaliante Wiese/4")

        parserDosTestesProjeto.executar("/home/humberto/Documentos/projectUtfpr/desenvolvimento/test/dadosIndividuais/Juliano Henrique Foleiss/1")
        parserDosTestesProjeto.executar("/home/humberto/Documentos/projectUtfpr/desenvolvimento/test/dadosIndividuais/Juliano Henrique Foleiss/2")

        parserDosTestesProjeto.executar("/home/humberto/Documentos/projectUtfpr/desenvolvimento/test/dadosIndividuais/Lucio Geronimo Valentin/1")

        parserDosTestesProjeto.executar("/home/humberto/Documentos/projectUtfpr/desenvolvimento/test/dadosIndividuais/Luiz Arthur Feitosa dos Santos/1")
        parserDosTestesProjeto.executar("/home/humberto/Documentos/projectUtfpr/desenvolvimento/test/dadosIndividuais/Marco Aurélio Graciotto Silva/1")
        parserDosTestesProjeto.executar("/home/humberto/Documentos/projectUtfpr/desenvolvimento/test/dadosIndividuais/Marco Aurélio Graciotto Silva/2")
        parserDosTestesProjeto.executar("/home/humberto/Documentos/projectUtfpr/desenvolvimento/test/dadosIndividuais/Marco Aurélio Graciotto Silva/3")

        parserDosTestesProjeto.executar("/home/humberto/Documentos/projectUtfpr/desenvolvimento/test/dadosIndividuais/Paulo Cesar Gonçalves/1")
        parserDosTestesProjeto.executar("/home/humberto/Documentos/projectUtfpr/desenvolvimento/test/dadosIndividuais/Paulo Cesar Gonçalves/2")

        parserDosTestesProjeto.executar("/home/humberto/Documentos/projectUtfpr/desenvolvimento/test/dadosIndividuais/Reginaldo Ré/1")
        # parserDosTestesProjeto.executar("/home/humberto/Documentos/projectUtfpr/desenvolvimento/test/dadosIndividuais/Reginaldo Ré/2")
        # parserDosTestesProjeto.executar("/home/humberto/Documentos/projectUtfpr/desenvolvimento/test/dadosIndividuais/Reginaldo Ré/3")
        # parserDosTestesProjeto.executar("/home/humberto/Documentos/projectUtfpr/desenvolvimento/test/dadosIndividuais/Reginaldo Ré/4")
        # parserDosTestesProjeto.executar("/home/humberto/Documentos/projectUtfpr/desenvolvimento/test/dadosIndividuais/Reginaldo Ré/5")

        parserDosTestesProjeto.executar("/home/humberto/Documentos/projectUtfpr/desenvolvimento/test/dadosIndividuais/Rodrigo Hübner/1")
        parserDosTestesProjeto.executar("/home/humberto/Documentos/projectUtfpr/desenvolvimento/test/dadosIndividuais/Rodrigo Hübner/2")
        parserDosTestesProjeto.executar("/home/humberto/Documentos/projectUtfpr/desenvolvimento/test/dadosIndividuais/Rodrigo Hübner/3")

        parserDosTestesProjeto.executar("/home/humberto/Documentos/projectUtfpr/desenvolvimento/test/dadosIndividuais/Rogério Aparecido Gonçalves/1")
        parserDosTestesProjeto.executar("/home/humberto/Documentos/projectUtfpr/desenvolvimento/test/dadosIndividuais/Rogério Aparecido Gonçalves/2")
        parserDosTestesProjeto.executar("/home/humberto/Documentos/projectUtfpr/desenvolvimento/test/dadosIndividuais/Rogério Aparecido Gonçalves/3")
        parserDosTestesProjeto.executar("/home/humberto/Documentos/projectUtfpr/desenvolvimento/test/dadosIndividuais/Rogério Aparecido Gonçalves/4")



    def testAlessandroKramerProjeto1(self):
        proj = Projeto.objects.get(nome=u"CArS - Convergence Area Scheduler")
        self.assertEquals(proj.nome, u"CArS - Convergence Area Scheduler")

    def testAlessandroKramerProjeto2(self):
        proj = Projeto.objects.get(nome=u"MOAIS")
        self.assertEquals(proj.nome, u"MOAIS")

    def testAlessandroKramerProjeto3(self):
        proj = Projeto.objects.get(nome=u"Construção de Modelo Tecnológico para Implantação de Computação em Nuvem")
        self.assertEquals(proj.nome, u"Construção de Modelo Tecnológico para Implantação de Computação em Nuvem")



    def testAnaPaulaChavesSteinmacherProjeto1(self):

        proj = Projeto.objects.get(nome=u"Uso de Inteligência Coletiva para Melhorar a Mobilidade Urbana em Cidades Inteligentes")
        self.assertEquals(proj.nome, u'Uso de Inteligência Coletiva para Melhorar a Mobilidade Urbana em Cidades Inteligentes')

    def testAnaPaulaChavesSteinmacherProjeto2(self):
        proj = Projeto.objects.get(nome=u"Análise de redes sociais de desenvolvedores para predição de bugs em projetos de software")
        self.assertEquals(proj.nome, u'Análise de redes sociais de desenvolvedores para predição de bugs em projetos de software')

    def testAnaPaulaChavesSteinmacherProjeto3(self):

        proj = Projeto.objects.get(nome=u"UbiBus: Um Sistema de Transporte Público Inteligente, Ubíquo e Sensível ao Contexto")
        self.assertEquals(proj.nome, u'UbiBus: Um Sistema de Transporte Público Inteligente, Ubíquo e Sensível ao Contexto')

    def testAnaPaulaChavesSteinmacherProjeto4(self):
        proj = Projeto.objects.get(nome=u"SIMTUR: Sistema Inteligente para Monitoramento de Tráfego Urbano")
        self.assertEquals(proj.nome, u'SIMTUR: Sistema Inteligente para Monitoramento de Tráfego Urbano')



    def testArethaBarbosaAlencar1(self):
        proj = Projeto.objects.get(nome=u"Visualização da evolução semântica e temporal de coleções de artigos científicos")
        self.assertEquals(proj.nome, u'Visualização da evolução semântica e temporal de coleções de artigos científicos')



    def testDiegoBertoliniGoncalves1(self):
        proj = Projeto.objects.get(nome=u"Identificação de Script Indiano usando Descritores de Textura.")
        self.assertEquals(proj.nome, u'Identificação de Script Indiano usando Descritores de Textura.')

    def testDiegoBertoliniGoncalves2(self):
        proj = Projeto.objects.get(nome=u"Identificação de Escritores através de Manuscritos Árabes")
        self.assertEquals(proj.nome, u'Identificação de Escritores através de Manuscritos Árabes')

    def testDiegoBertoliniGoncalves3(self):
        proj = Projeto.objects.get(nome=u"IDENTIFICAÇÃO E VERIFICAÇÃO DE AUTORIA USANDO DESCRITORES DE TEXTURA")
        self.assertEquals(proj.nome, u'IDENTIFICAÇÃO E VERIFICAÇÃO DE AUTORIA USANDO DESCRITORES DE TEXTURA')



    def testEvertonFernandoBarros1(self):
        proj = Projeto.objects.get(nome=u"Algoritmos Heurísticos para Descoberta de Conhecimento em Banco de Dados")
        self.assertEquals(proj.nome, u'Algoritmos Heurísticos para Descoberta de Conhecimento em Banco de Dados')



    def testIgorFabioSteinmacher1(self):
        proj = Projeto.objects.get(nome=u"Suporte a desenvolvedores novatos em comunidades de software livre")
        self.assertEquals(proj.nome, u'Suporte a desenvolvedores novatos em comunidades de software livre')

    def testIgorFabioSteinmacher2(self):
        proj = Projeto.objects.get(nome=u"Portal para desenvolvedores novatos em comunidades de software livre")
        self.assertEquals(proj.nome, u'Portal para desenvolvedores novatos em comunidades de software livre')

    def testIgorFabioSteinmacher1(self):
        proj = Projeto.objects.get(nome=u"Suporte a novatos em projetos de software livre")
        self.assertEquals(proj.nome, u'Suporte a novatos em projetos de software livre')



    def testIgorScalianteWiese1(self):
        proj = Projeto.objects.get(nome=u"Mineração de dados e extração e visualização de informações de repositórios de software livre")
        self.assertEquals(proj.nome, u'Mineração de dados e extração e visualização de informações de repositórios de software livre')

    def testIgorScalianteWiese2(self):
        proj = Projeto.objects.get(nome=u"Suporte a novatos em projetos de software livre")
        self.assertEquals(proj.nome, u'Suporte a novatos em projetos de software livre')

    def testIgorScalianteWiese3(self):
        proj = Projeto.objects.get(nome=u"Mineração de dados e extração e visualização de informações de repositórios de software livre")
        self.assertEquals(proj.nome, u'Mineração de dados e extração e visualização de informações de repositórios de software livre')


        # proj = Projeto.objects.get(nome=u"Caracterização de dependências de mudança na evolução de software por meio de métricas sociais, de processo e de código")
        # self.assertEquals(proj.nome, u'Caracterização de dependências de mudança na evolução de software por meio de métricas sociais, de processo e de código')
        # proj = Projeto.objects.get(nome="")
        # self.assertEquals(proj.nome, '')
        # proj = Projeto.objects.get(nome="")
        # self.assertEquals(proj.nome, '')
        # proj = Projeto.objects.get(nome="")
        # self.assertEquals(proj.nome, '')
        # proj = Projeto.objects.get(nome="")
        # self.assertEquals(proj.nome, '')
        # proj = Projeto.objects.get(nome="")
        # self.assertEquals(proj.nome, '')
        # proj = Projeto.objects.get(nome="")
        # self.assertEquals(proj.nome, '')
        # proj = Projeto.objects.get(nome="")
        # self.assertEquals(proj.nome, '')
        # proj = Projeto.objects.get(nome="")
        # self.assertEquals(proj.nome, '')
        #

        def testPossuiProjetoIntegrante(self):
            proj = Projeto.objects.get(nome=u"CArS - Convergence Area Scheduler")
            # self.assertEquals(proj.nome, )
            self.assertEquals(proj.proj__integrantesProfessor__nome, u"Alessandro Kraemer")
            self.assertEquals(proj.proj__integrantesProfessor__nome, u"Olivier Richard")
