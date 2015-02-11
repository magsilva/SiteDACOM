from numpy.distutils.fcompiler import none

__author__ = 'root'


import sys
import shutil
import Levenshtein
import os, errno

sys.path.append("../../scriptLattes")

from compiladorDeListas import *
from scriptLattes  import *


def add_Artigo(titulo, data, doi, paginaInicial, paginaFinal, Resumo):
    a = Artigo.objects.get_or_create(titulo = titulo,
                                   data = data,
                                   doi = doi,
                                   paginaInicial = paginaInicial,
                                   paginaFinal = paginaFinal,
                                   Resumo = Resumo
    )
    return a

def add_ArtigoEmPeriodico(nomeJournal ,ISSN , publisher, numero, volume):

    p = ArtigoEmPeriodico.objects.get_or_create(nomeJournal = nomeJournal,
                                   ISSN = ISSN,
                                   publisher = publisher,
                                   numero = numero,
                                   volume = volume
    )
    return p


def add_ArtigoEmConferencia(nomedaConferencia, ISSN, ISBN,local):

    c = ArtigoEmConferencia.objects.get_or_create(nomedaConferencia = nomedaConferencia,
                                    ISSN = ISSN,
                                    ISBN= ISBN,
                                    local = local
    )
    return c


def populate():

    for listadeArtigo in compiladorDeListas.grupo.compilador.listaDeArtigo.Objects.all():
        add_Artigo( titulo = listadeArtigo.titulo,
            data = listadeArtigo.ano,
            doi = listadeArtigo.doi,
            paginaInicial = listadeArtigo.paginas,
            paginaFinal = listadeArtigo.paginas,
            Resumo = listadeArtigo.resumo
            )

#    for listadeArtigoEmPeriodico in compiladorDeListas.grupo.compilador.listaDeArtigoEmPeriodico.Objects.all():
 #        add_ArtigoEmPeriodico(

            #nomeJournal = listadeArtigo.revista,
            #ISSN = listadeArtigo.
   #         publisher = listadeArtigoEmPeriodico.revista,
  #          numero = listadeArtigoEmPeriodico.numero,
   #         volume = listadeArtigoEmPeriodico.volume
    #    )

    #for listadeArtigoEmConferencia in  compiladorDeListas.grupo.compilador.listaDeArtigo.Objects.all()
      #  add_ArtigoEmConferencia(nomedaConferencia =
    #            ISSN  =
    #            ISBN =
    #            local =

     #   pub = ResumoEmCongresso(self.idMembro)
	#			pub.autores  = self.autores
#				pub.titulo   = self.titulo
#				pub.nomeDoEvento=self.nomeDoEvento
##				pub.ano      = self.ano
#				pub.volume   = self.volume
#				pub.numero   = self.numero
#				pub.paginas  = self.paginas
#				pub.chave   = self.autores
#				pub.doi     = 'http://dx.doi.org/'+self.doi if not self.doi==0 else ''
#				self.listaResumoEmCongresso.append(pub)
#				return
 #       )


#def add_page(cat, title, url, views=0):
#    p = Page.objects.get_or_create(category=cat, title=title, url=url, views=views)[0]
#    return p
#
#def add_Artigo(name):
#    c = Artigo.objects.get_or_create(name=name)[0]
#    return c

# Start execution here!
if __name__ == '__main__':
    print "Começando a Popular o Banco de Dados Projeto Sites dos Departamentos..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
    from desenvolvimento.models import Artigo, ArtigoEmConferencia, ArtigoEmPeriodico, Projeto, Professor
    populate()


