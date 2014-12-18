import sys, os, errno, shutil, Levenshtein
#sys.path.append('lattes/scriptLattes/')
from django.db import models
#Django cron
#scheduler ver 
# __eq__ #metodo de comparacao


# Create your models here.
class DepartamentoAcademico(models.Model):
        nome = models.CharField('Nome', max_length=100)
        sigla = models.CharField('Sigla', max_length=100)
        #chefe = models.ForeignKey(Professor)
        #suplente = models.ForeignKey(Professor)
        #funcionario = [Funcionario]


class Funcionario(models.Model):
	nome = models.CharField('Nome', max_length=100)
	email = models.CharField('E-mail', max_length=200)
	telefone = models.CharField('Telefone', max_length=20)
	departamento = models.ForeignKey(DepartamentoAcademico)
	funcao = models.CharField('Funcao', max_length=100)

class Professor(Funcionario, models.Model):
	lattes = models.CharField('Link do Lattes', max_length=50)
	#foto

class Curso(models.Model):
        nome = models.CharField('Curso',max_length=50)
        sigla = models.CharField('Sigla', max_length=20)
        disciplina = models.CharField('Disciplina', max_length=100)

class Coordenacao(models.Model):
	coordenador = models.ForeignKey(Professor, related_name = 'coordenadorCoo')
	suplente = models.ForeignKey(Professor, related_name = 'suplenteCoo')
	curso = models.ForeignKey(Curso)

class Artigos(models.Model):
	nomeCompleto = models.ForeignKey(Professor, related_name = 'NomeProfessor')
	bolsaProdutividade = models.CharField('bolsaProdutividade', max_length=100)        
	enderecoProfissional  = models.CharField('bolsaProdutividade', max_length=100)        
	nomeEmCitacoesBibliograficas  =  models.CharField('bolsaProdutividade', max_length=255)
	textoResumo = models.CharField('bolsaProdutividade', max_length=500)
# 	foto




# class Artigo(models.Model):
# 	listadeAutore;
# 	titulo
# 	data;
# 	doi;#identificador de artigo nao necessario;
# 	pagina inicial;
# 	paginafinal;
# 	Resumo; #Nao vai ter no lattes


# class ArtigoEmPeriodico(Artigo):
# 	nomeJournal;
# 	ISSN; #identificador;
# 	publisher;
# 	numero, e volume;
		
# class ArtigoEmConferencia(Artigo):
# 	nomedaConferencia
# 	ISSN #nao necessario
# 	ISBN #necesaario
# 	local

# class Projeto(models)
# 	listadeCoordenadores
# 	listaColaboradores
# 	nome
# 	dataInicio
# 	DatadeFim
# 	AgendaFinanciadora
# 	Resumo

		# nomeCompleto = models.ForeignKey(Professor, related_name = 'NomeProfessor')
		# bolsaProdutividade = models.CharField('bolsaProdutividade', max_length=100)        
		# enderecoProfissional  = models.CharField('bolsaProdutividade', max_length=100)        
		# nomeEmCitacoesBibliograficas  =  models.CharField('bolsaProdutividade', max_length=255)
		# textoResumo = models.CharField('bolsaProdutividade', max_length=500)
		


		#self.foto 
		
		#def __unicode__(self):      
        #		return self.nomeCompleto, bolsaProdutividade, enderecoProfissional, sexo, nomeEmCitacoesBibliograficas, textoResumo #self.foto
        