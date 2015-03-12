__author__ = 'root'


# from django.core.management import setup_environ
# from utfpr import settings
# from desenvolvimento.models import Artigo, ArtigoEmPeriodico, ArtigoEmConferencia, Projeto
# sys.path.append("lattes/scriptLattes/scriptLattes")
# from compiladorDeListas import *
#
# def add_Artigo(titulo, data, doi, paginaInicial, paginaFinal, Resumo):
# a = Artigo.objects.get_or_create(titulo = titulo,
#                                    data = data,
#                                    doi = doi,
#                                    paginaInicial = paginaInicial,
#                                    paginaFinal = paginaFinal,
#                                    Resumo = Resumo
#     )
#     return a
#
# def add_ArtigoEmPeriodico(nomeJournal ,ISSN , publisher, numero, volume):
#
#     p = ArtigoEmPeriodico.objects.get_or_create(nomeJournal = nomeJournal,
#                                    ISSN = ISSN,
#                                    publisher = publisher,
#                                    numero = numero,
#                                    volume = volume
#     )
#     return p
#
#
# def add_ArtigoEmConferencia(nomedaConferencia, ISSN, ISBN,local):
#
#     c =ArtigoEmConferencia.objects.get_or_create(nomedaConferencia = nomedaConferencia,
#                                     ISSN = ISSN,
#                                     ISBN= ISBN,
#                                     local = local
#     )
#     return c
#
#
# def populate():
#
#     for listadeArtigo in compiladorDeListas.grupo.compilador.listaDeArtigo.Objects.all():
#         add_Artigo( titulo = listadeArtigo.titulo,
#             data = listadeArtigo.ano,
#             doi = listadeArtigo.doi,
#             paginaInicial = listadeArtigo.paginas,
#             paginaFinal = listadeArtigo.paginas,
#             Resumo = listadeArtigo.resumo
#             )
#
# # Start execution here!
# if __name__ == '__main__':
#     print "Comecando a Popular o Banco de Dados Projeto Sites dos Departamentos..."
#     import os
#    # os.environ.setdefault("DJANGO_SETTINGS_MODULE", "desenvolvimento.settings")
#     desenvolvimento.models.os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'desenvolvimento.settings')
#     populate()
#
#
