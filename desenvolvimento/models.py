from django.db import models
# Create your models here.


class DepartamentoAcademico(models.Model):
    nome = models.CharField('Nome', max_length=100)
    sigla = models.CharField('Sigla', max_length=100)
    # chefe = models.ForeignKey(Professor)
    # suplente = models.ForeignKey(Professor)
    # funcionario = [Funcionario]


class Funcionario(models.Model):
    nome = models.CharField('Nome', max_length=100)
    email = models.CharField('E-mail', max_length=200)
    telefone = models.CharField('Telefone', max_length=20)
    departamento = models.ForeignKey(DepartamentoAcademico)
    funcao = models.CharField('Funcao', max_length=100)


class Formacao(models.Model):
    ano_inicio = models.CharField('Ano de Inicio', max_length=4)
    ano_conclusao = models.CharField('Ano de Conclusao', max_length=4)
    tipo =  models.CharField('Tipo', max_length=511)
    descricao= models.CharField('Descricao', max_length=5000)

class areadeAtuacao(models.Model):
    descricao = models.CharField('Area de Atuacao', max_length=511)

class Professor(Funcionario, models.Model):
    lattes = models.CharField('Link do Lattes', max_length=50)
    bolsaProdutividade = models.CharField('Bolsa Produtividade', max_length=100)
    enderecoProfissional = models.CharField('Endereco Profissional', max_length=255)
    nomeEmCitacoesBibliograficas = models.CharField('nomeEmCitacoesBibliograficas', max_length=255)
    textoResumo = models.CharField('bolsaProdutividade', max_length=500)
    formacao_academica = [Formacao]
    areadeAtuacao = [areadeAtuacao]

class Curso(models.Model):
    nome = models.CharField('Curso', max_length=50)
    sigla = models.CharField('Sigla', max_length=20)
    disciplina = models.CharField('Disciplina', max_length=100)


class Coordenacao(models.Model):
    coordenador = models.ForeignKey(Professor, related_name='coordenadorCoo')
    suplente = models.ForeignKey(Professor, related_name='suplenteCoo')
    curso = models.ForeignKey(Curso)


class Artigo(models.Model):
    listadeAutores = [Professor]
    titulo = models.CharField('Titulo do Artigo', max_length=255)
    data = models.DateField('Data do Artigo')
    doi = models.CharField('DOI', max_length=255)
    paginaInicial = models.CharField('Pagina Inicial', max_length=10)
    paginaFinal = models.CharField('Pagina Final', max_length=10)
    Resumo = models.CharField('Resumo', max_length=5000)


class ArtigoEmPeriodico(Artigo):
    nomeJournal = models.CharField('Nome Journal', max_length=255)
    ISSN = models.CharField('Codigo ISSN', max_length=255)  # identificador;models.CharField()
    publisher = models.CharField('Editora', max_length=255)
    numero = models.CharField('Numero', max_length=10)
    volume = models.CharField('Volume', max_length=10)


class ArtigoEmConferencia(Artigo):
    nomedaConferencia = models.CharField('Nome da Conferencia', max_length=255)
    ISSN = models.CharField('Codigo ISSN', max_length=50)
    ISBN = models.CharField('Codigo ISBN', max_length=50)  # obrigatorio
    local = models.CharField('Local da Conferencia', max_length=255)


class Projeto(models.Model):
    listadeCoordenadores = [Professor]
    listaColaboradores = [Professor]
    dataInicio = models.DateField()
    datadeFim = models.DateField()
    AgendaFinanciadora = models.CharField('Agencia Financiadora', max_length=255)
    nome =  models.CharField('Nome do Projeto', max_length=1000)
    resumo = models.CharField('Resumo', max_length=5000)

