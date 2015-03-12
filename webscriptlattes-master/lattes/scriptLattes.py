#!/usr/bin/python
# encoding: utf-8
#
#
#  scriptLattes V8
#  Copyright 2005-2013: Jesús P. Mena-Chalco e Roberto M. Cesar-Jr.
#  http://scriptlattes.sourceforge.net/
#
#
#  Este programa é um software livre; você pode redistribui-lo e/ou 
#  modifica-lo dentro dos termos da Licença Pública Geral GNU como 
#  publicada pela Fundação do Software Livre (FSF); na versão 2 da 
#  Licença, ou (na sua opinião) qualquer versão.
#
#  Este programa é distribuído na esperança que possa ser util, 
#  mas SEM NENHUMA GARANTIA; sem uma garantia implicita de ADEQUAÇÂO a qualquer
#  MERCADO ou APLICAÇÃO EM PARTICULAR. Veja a
#  Licença Pública Geral GNU para maiores detalhes.
#
#  Você deve ter recebido uma cópia da Licença Pública Geral GNU
#  junto com este programa, se não, escreva para a Fundação do Software
#  Livre(FSF) Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
#

import sys
import shutil
import os, errno

#sys.path.append('scriptLattes')
#sys.path.append('scriptLattes/producoesBibliograficas/')
#sys.path.append('scriptLattes/producoesTecnicas/')
#sys.path.append('scriptLattes/producoesArtisticas/')
#sys.path.append('scriptLattes/producoesUnitarias/')
#sys.path.append('scriptLattes/orientacoes/')
#sys.path.append('scriptLattes/eventos/')
#sys.path.append('scriptLattes/charts/')
#sys.path.append('scriptLattes/internacionalizacao/')
#sys.path.append('scriptLattes/qualis/')

from scriptLattes import *
from scriptLattes.producoesBibliograficas import *
from scriptLattes.producoesTecnicas import *
from scriptLattes.producoesArtisticas import *
from scriptLattes.producoesUnitarias import *
from scriptLattes.orientacoes import *
from scriptLattes.eventos import *
from scriptLattes.internacionalizacao import *
from scriptLattes.qualis import *

from scriptLattes.grupo import *
from utils import *

if __name__ == "__main__":
	arquivoConfiguracao = sys.argv[1]

	if len(sys.argv) > 4:
		novoGrupo = Grupo(arquivoConfiguracao, sys.argv[2], sys.argv[3], sys.argv[4])
	else:
		novoGrupo = Grupo(arquivoConfiguracao)

	novoGrupo.imprimirListaDeParametros()
	novoGrupo.imprimirListaDeRotulos()

	if criarDiretorio(novoGrupo.obterParametro('global-diretorio_de_saida')):
		existe = novoGrupo.carregarDadosCVLattes() #obrigatorio
		print existe

		if existe is not None:
			sys.exit('cv nao exite')

		novoGrupo.compilarListasDeItems() # obrigatorio
		novoGrupo.identificarQualisEmPublicacoes() # obrigatorio
		novoGrupo.calcularInternacionalizacao() # obrigatorio
		novoGrupo.imprimirMatrizesDeFrequencia() 

		novoGrupo.gerarGrafosDeColaboracoes() # obrigatorio
		print "[ROTULOS]"
		print "- "+str(novoGrupo.listaDeRotulos)
		print "- "+str(novoGrupo.listaDeRotulosCores)

		novoGrupo.gerarGraficosDeBarras() # obrigatorio
		novoGrupo.gerarMapaDeGeolocalizacao() # obrigatorio
		novoGrupo.gerarPaginasWeb() # obrigatorio

		novoGrupo.gerarXMLdeGrupo()
		novoGrupo.gerarCSVdeQualisdeGrupo()
		novoGrupo.gerarRISdeGrupo()

		# copiar imagens e css
		copiarArquivos(novoGrupo.obterParametro('global-diretorio_de_saida'))

		# finalizando o processo
		#print '[AVISO] Quem vê \'Lattes\', não vê coração! B-)'
		#print '[AVISO] Por favor, cadastre-se na página: http://scriptlattes.sourceforge.net\n'
		print '\n\n\n[COMO REFERENCIAR ESTE TRABALHO]'
		print '    Jesus P. Mena-Chalco e Roberto M. Cesar-Jr.'
		print '    scriptLattes: An open-source knowledge extraction system from the Lattes Platform.'
		print '    Journal of the Brazilian Computer Society, vol.15, n.4, páginas 31-39, 2009.'

		print '\n\nscriptLattes executado!'

