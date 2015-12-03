from django.db import models

class DepartamentoAcademico(models.Model):
    nome = models.CharField('Nome', max_length=100)
    sigla = models.CharField('Sigla', max_length=100)
    # chefe = models.ForeignKey(Professor)
    # suplente = models.ForeignKey(Professor)


class Professor(models.Model):
    nome = models.CharField('Nome', max_length=100)
    email = models.CharField('E-mail', max_length=200, null=True, blank=True)
    telefone = models.CharField('Telefone', max_length=20, null=True, blank=True)
    departamento = models.ForeignKey(DepartamentoAcademico)
    funcao = models.CharField('Funcao', max_length=100)
    lattes = models.CharField('Link do Lattes', max_length=50, null=True, blank=True)
    bolsaProdutividade = models.CharField('Bolsa Produtividade', max_length=100, null=True, blank=True)
    enderecoProfissional = models.CharField('Endereco Profissional', max_length=5000, null=True, blank=True)
    endereco_profissional_lat= models.CharField('Endereco Profissional_lat', max_length=5000, null=True, blank=True)
    endereco_profissional_long= models.CharField('Endereco Profissional_long', max_length=5000, null=True, blank=True)
    nomeEmCitacoesBibliograficas = models.CharField('nomeEmCitacoesBibliograficas', max_length=255, null=True, blank=True)
    textoResumo = models.CharField('bolsaProdutividade', max_length=500, null=True, blank=True)
    # funcionario = [Funcionario]

    def __unicode__(self):
        return self.nome

    def __init__(self):
        return Professor()


# class Funcionario(models.Model):
#     nome = models.CharField('Nome', max_length=100)
#     email = models.CharField('E-mail', max_length=200)
#     telefone = models.CharField('Telefone', max_length=20)
#     departamento = models.ForeignKey(DepartamentoAcademico)
#     funcao = models.CharField('Funcao', max_length=100)


class Formacao(models.Model):
    ano_inicio = models.CharField('Ano de Inicio', max_length=4)
    ano_conclusao = models.CharField('Ano de Conclusao', max_length=4)
    tipo = models.CharField('Tipo', max_length=511)
    descricao = models.CharField('Descricao', max_length=5000)
     # chave estrangeira do professor;

class areadeAtuacao(models.Model):
    descricao = models.CharField('Area de Atuacao', max_length=511)
    # chave estrangeira do professor; muito pra muitos;

class Curso(models.Model):
    nome = models.CharField('Curso', max_length=50)
    sigla = models.CharField('Sigla', max_length=20, null=True, blank=True)
    # disciplina = models.CharField('Disciplina', max_length=100)


class Coordenacao(models.Model):
    coordenador = models.ForeignKey(Professor, related_name='coordenadorCoo')
    suplente = models.ForeignKey(Professor, related_name='suplenteCoo')
    curso = models.ForeignKey(Curso)


class Artigo(models.Model):
    listadeAutores = models.CharField('Lista de Autores', max_length=5000)
    titulo = models.CharField('Titulo do Artigo', max_length=255)
    data = models.CharField('Data do Artigo', max_length=5)
    doi = models.CharField('DOI', max_length=255, null=True, blank=True)
    paginas = models.CharField('Paginas', max_length=10, null=True, blank=True)
    resumo = models.CharField('Resumo', max_length=5000)


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
    listadeCoordenadores = models.CharField('Lista de Coordenadores', max_length=5000, null=True, blank=True)
    listaColaboradores = models.CharField('Lista de Colaboradores', max_length=5000, null=True, blank=True)
    dataInicio = models.CharField('Data Inicio', max_length=5, null=True, blank=True)
    datadeFim = models.CharField('Data de Fim', max_length=5, null=True, blank=True)
    AgendaFinanciadora = models.CharField('Agencia Financiadora', max_length=255, null=True, blank=True)
    nome = models.CharField('Nome do Projeto', max_length=1000)
    resumo = models.CharField('Resumo', max_length=10000)

    def __unicode__(self):
        return self.nome

class Evento(models.Model):
    doi = models.CharField('DOI', max_length=255)
    autores = models.CharField('Autores', max_length=5000)
    titulo = models.CharField('Titulo', max_length=5000)
    nomeEvento = models.CharField('Nome do Evento', max_length=5000, null=True, blank=True)
    ano = models.CharField('Ano', max_length=4)
    volume = models.CharField('Volume', max_length=10)
    paginas = models.CharField('Paginas', max_length=255)
