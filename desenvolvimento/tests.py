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
        parserDosTestesProjeto.executar("/home/humberto/Documentos/projectUtfpr/desenvolvimento/test/dadosIndividuais/AlessandroKramer/1.xml")
        parserDosTestesProjeto.executar("/home/humberto/Documentos/projectUtfpr/desenvolvimento/test/dadosIndividuais/AlessandroKramer/2.xml")
        parserDosTestesProjeto.executar("/home/humberto/Documentos/projectUtfpr/desenvolvimento/test/dadosIndividuais/AlessandroKramer/3.xml")

        parserDosTestesProjeto.executar("/home/humberto/Documentos/projectUtfpr/desenvolvimento/test/dadosIndividuais/Ana Paula Chaves Steinmacher/1.xml")
        parserDosTestesProjeto.executar("/home/humberto/Documentos/projectUtfpr/desenvolvimento/test/dadosIndividuais/Ana Paula Chaves Steinmacher/2.xml")
        parserDosTestesProjeto.executar("/home/humberto/Documentos/projectUtfpr/desenvolvimento/test/dadosIndividuais/Ana Paula Chaves Steinmacher/3.xml")
        parserDosTestesProjeto.executar("/home/humberto/Documentos/projectUtfpr/desenvolvimento/test/dadosIndividuais/Ana Paula Chaves Steinmacher/4.xml")

        parserDosTestesProjeto.executar("/home/humberto/Documentos/projectUtfpr/desenvolvimento/test/dadosIndividuais/André Luís Schwerz/1.xml")

        parserDosTestesProjeto.executar("/home/humberto/Documentos/projectUtfpr/desenvolvimento/test/dadosIndividuais/Aretha Barbosa Alencar/1.xml")

        parserDosTestesProjeto.executar("/home/humberto/Documentos/projectUtfpr/desenvolvimento/test/dadosIndividuais/Diego Bertolini Gonçalves/1.xml")
        parserDosTestesProjeto.executar("/home/humberto/Documentos/projectUtfpr/desenvolvimento/test/dadosIndividuais/Diego Bertolini Gonçalves/2.xml")
        parserDosTestesProjeto.executar("/home/humberto/Documentos/projectUtfpr/desenvolvimento/test/dadosIndividuais/Diego Bertolini Gonçalves/3.xml")

        parserDosTestesProjeto.executar("/home/humberto/Documentos/projectUtfpr/desenvolvimento/test/dadosIndividuais/Everton Fernando Barros/1.xml")

        parserDosTestesProjeto.executar("/home/humberto/Documentos/projectUtfpr/desenvolvimento/test/dadosIndividuais/Filipe Roseiro Côgo/1.xml")
        parserDosTestesProjeto.executar("/home/humberto/Documentos/projectUtfpr/desenvolvimento/test/dadosIndividuais/Filipe Roseiro Côgo/2.xml")
        parserDosTestesProjeto.executar("/home/humberto/Documentos/projectUtfpr/desenvolvimento/test/dadosIndividuais/Filipe Roseiro Côgo/3.xml")

        parserDosTestesProjeto.executar("/home/humberto/Documentos/projectUtfpr/desenvolvimento/test/dadosIndividuais/Igor Fabio Steinmacher/1.xml")
        parserDosTestesProjeto.executar("/home/humberto/Documentos/projectUtfpr/desenvolvimento/test/dadosIndividuais/Igor Fabio Steinmacher/2.xml")
        parserDosTestesProjeto.executar("/home/humberto/Documentos/projectUtfpr/desenvolvimento/test/dadosIndividuais/Igor Fabio Steinmacher/3.xml")
        parserDosTestesProjeto.executar("/home/humberto/Documentos/projectUtfpr/desenvolvimento/test/dadosIndividuais/Igor Fabio Steinmacher/4.xml")
        parserDosTestesProjeto.executar("/home/humberto/Documentos/projectUtfpr/desenvolvimento/test/dadosIndividuais/Igor Fabio Steinmacher/5.xml")

        parserDosTestesProjeto.executar("/home/humberto/Documentos/projectUtfpr/desenvolvimento/test/dadosIndividuais/Igor Scaliante Wiese/1.xml")
        parserDosTestesProjeto.executar("/home/humberto/Documentos/projectUtfpr/desenvolvimento/test/dadosIndividuais/Igor Scaliante Wiese/2.xml")
        parserDosTestesProjeto.executar("/home/humberto/Documentos/projectUtfpr/desenvolvimento/test/dadosIndividuais/Igor Scaliante Wiese/3.xml")
        parserDosTestesProjeto.executar("/home/humberto/Documentos/projectUtfpr/desenvolvimento/test/dadosIndividuais/Igor Scaliante Wiese/4.xml")

        parserDosTestesProjeto.executar("/home/humberto/Documentos/projectUtfpr/desenvolvimento/test/dadosIndividuais/Juliano Henrique Foleiss/1.xml")
        parserDosTestesProjeto.executar("/home/humberto/Documentos/projectUtfpr/desenvolvimento/test/dadosIndividuais/Juliano Henrique Foleiss/2.xml")

        parserDosTestesProjeto.executar("/home/humberto/Documentos/projectUtfpr/desenvolvimento/test/dadosIndividuais/Lucio Geronimo Valentin/1.xml")

        parserDosTestesProjeto.executar("/home/humberto/Documentos/projectUtfpr/desenvolvimento/test/dadosIndividuais/Luiz Arthur Feitosa dos Santos/1.xml")
        parserDosTestesProjeto.executar("/home/humberto/Documentos/projectUtfpr/desenvolvimento/test/dadosIndividuais/Marco Aurélio Graciotto Silva/1.xml")
        parserDosTestesProjeto.executar("/home/humberto/Documentos/projectUtfpr/desenvolvimento/test/dadosIndividuais/Marco Aurélio Graciotto Silva/2.xml")
        parserDosTestesProjeto.executar("/home/humberto/Documentos/projectUtfpr/desenvolvimento/test/dadosIndividuais/Marco Aurélio Graciotto Silva/3.xml")

        parserDosTestesProjeto.executar("/home/humberto/Documentos/projectUtfpr/desenvolvimento/test/dadosIndividuais/Paulo Cesar Gonçalves/1.xml")
        parserDosTestesProjeto.executar("/home/humberto/Documentos/projectUtfpr/desenvolvimento/test/dadosIndividuais/Paulo Cesar Gonçalves/2.xml")

        parserDosTestesProjeto.executar("/home/humberto/Documentos/projectUtfpr/desenvolvimento/test/dadosIndividuais/Reginaldo Ré/1.xml")
        parserDosTestesProjeto.executar("/home/humberto/Documentos/projectUtfpr/desenvolvimento/test/dadosIndividuais/Reginaldo Ré/2.xml")
        parserDosTestesProjeto.executar("/home/humberto/Documentos/projectUtfpr/desenvolvimento/test/dadosIndividuais/Reginaldo Ré/3.xml")
        parserDosTestesProjeto.executar("/home/humberto/Documentos/projectUtfpr/desenvolvimento/test/dadosIndividuais/Reginaldo Ré/4.xml")
        parserDosTestesProjeto.executar("/home/humberto/Documentos/projectUtfpr/desenvolvimento/test/dadosIndividuais/Reginaldo Ré/5.xml")

        parserDosTestesProjeto.executar("/home/humberto/Documentos/projectUtfpr/desenvolvimento/test/dadosIndividuais/Rodrigo Hübner/1.xml")
        parserDosTestesProjeto.executar("/home/humberto/Documentos/projectUtfpr/desenvolvimento/test/dadosIndividuais/Rodrigo Hübner/2.xml")
        parserDosTestesProjeto.executar("/home/humberto/Documentos/projectUtfpr/desenvolvimento/test/dadosIndividuais/Rodrigo Hübner/3.xml")

        parserDosTestesProjeto.executar("/home/humberto/Documentos/projectUtfpr/desenvolvimento/test/dadosIndividuais/Rogério Aparecido Gonçalves/1.xml")
        parserDosTestesProjeto.executar("/home/humberto/Documentos/projectUtfpr/desenvolvimento/test/dadosIndividuais/Rogério Aparecido Gonçalves/2.xml")
        parserDosTestesProjeto.executar("/home/humberto/Documentos/projectUtfpr/desenvolvimento/test/dadosIndividuais/Rogério Aparecido Gonçalves/3.xml")
        parserDosTestesProjeto.executar("/home/humberto/Documentos/projectUtfpr/desenvolvimento/test/dadosIndividuais/Rogério Aparecido Gonçalves/4.xml")


    def testPossuiProfessor(self):
        # AlessandroKramer
        proj = Projeto.objects.get(nome="CArS - Convergence Area Scheduler")
        self.assertEquals(proj.nome, 'CArS - Convergence Area Scheduler')
        proj = Projeto.objects.get(nome="MOAIS")
        self.assertEquals(proj.nome, 'MOAIS')
        proj = Projeto.objects.get(nome="Construção de Modelo Tecnológico para Implantação de Computação em Nuvem")
        self.assertEquals(proj.nome, 'Construção de Modelo Tecnológico para Implantação de Computação em Nuvem')

        proj = Projeto.objects.get(nome="Uso de Inteligência Coletiva para Melhorar a Mobilidade Urbana em Cidades Inteligentes")
        self.assertEquals(proj.nome, 'Uso de Inteligência Coletiva para Melhorar a Mobilidade Urbana em Cidades Inteligentes')
        proj = Projeto.objects.get(nome="Análise de redes sociais de desenvolvedores para predição de bugs em projetos de software")
        self.assertEquals(proj.nome, 'Análise de redes sociais de desenvolvedores para predição de bugs em projetos de software')
        proj = Projeto.objects.get(nome="UbiBus: Um Sistema de Transporte Público Inteligente, Ubíquo e Sensível ao Contexto")
        self.assertEquals(proj.nome, 'UbiBus: Um Sistema de Transporte Público Inteligente, Ubíquo e Sensível ao Contexto')
        proj = Projeto.objects.get(nome="SIMTUR: Sistema Inteligente para Monitoramento de Tráfego Urbano")
        self.assertEquals(proj.nome, 'SIMTUR: Sistema Inteligente para Monitoramento de Tráfego Urbano')

        proj = Projeto.objects.get(nome="Visualização da evolução semântica e temporal de coleções de artigos científicos")
        self.assertEquals(proj.nome, 'Visualização da evolução semântica e temporal de coleções de artigos científicos')
        proj = Projeto.objects.get(nome="Identificação de Script Indiano usando Descritores de Textura.")
        self.assertEquals(proj.nome, 'Identificação de Script Indiano usando Descritores de Textura.')
        proj = Projeto.objects.get(nome="Identificação de Escritores através de Manuscritos Árabes")
        self.assertEquals(proj.nome, 'Identificação de Escritores através de Manuscritos Árabes')
        proj = Projeto.objects.get(nome="IDENTIFICAÇÃO E VERIFICAÇÃO DE AUTORIA USANDO DESCRITORES DE TEXTURA")
        self.assertEquals(proj.nome, 'IDENTIFICAÇÃO E VERIFICAÇÃO DE AUTORIA USANDO DESCRITORES DE TEXTURA')
        proj = Projeto.objects.get(nome="Algoritmos Heurísticos para Descoberta de Conhecimento em Banco de Dados")
        self.assertEquals(proj.nome, 'Algoritmos Heurísticos para Descoberta de Conhecimento em Banco de Dados')

        proj = Projeto.objects.get(nome="Suporte a desenvolvedores novatos em comunidades de software livre")
        self.assertEquals(proj.nome, 'Suporte a desenvolvedores novatos em comunidades de software livre')
        proj = Projeto.objects.get(nome="Portal para desenvolvedores novatos em comunidades de software livre")
        self.assertEquals(proj.nome, 'Portal para desenvolvedores novatos em comunidades de software livre')
        proj = Projeto.objects.get(nome="Suporte a novatos em projetos de software livre")
        self.assertEquals(proj.nome, 'Suporte a novatos em projetos de software livre')
        proj = Projeto.objects.get(nome="Análise de redes sociais de desenvolvedores para predição de bugs em projetos de software")
        self.assertEquals(proj.nome, 'Análise de redes sociais de desenvolvedores para predição de bugs em projetos de software')
        proj = Projeto.objects.get(nome="Mineração de dados e extração e visualização de informações de repositórios de software livre")
        self.assertEquals(proj.nome, 'Mineração de dados e extração e visualização de informações de repositórios de software livre')
        proj = Projeto.objects.get(nome="Suporte a novatos em projetos de software livre")
        self.assertEquals(proj.nome, 'Suporte a novatos em projetos de software livre')
        proj = Projeto.objects.get(nome="Análise de redes sociais de desenvolvedores para predição de bugs em projetos de software")
        self.assertEquals(proj.nome, 'Análise de redes sociais de desenvolvedores para predição de bugs em projetos de software')
        proj = Projeto.objects.get(nome="Mineração de dados e extração e visualização de informações de repositórios de software livre")
        self.assertEquals(proj.nome, 'Mineração de dados e extração e visualização de informações de repositórios de software livre')
        proj = Projeto.objects.get(nome="Caracterização de dependências de mudança na evolução de software por meio de métricas sociais, de processo e de código")
        self.assertEquals(proj.nome, 'Caracterização de dependências de mudança na evolução de software por meio de métricas sociais, de processo e de código')
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

