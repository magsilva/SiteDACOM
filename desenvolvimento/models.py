from django.db import models
# Create your models here.

CATEGORIAS = (
    ('0', 'Adm, Contabeis e Turismo'),
    ('1', 'Antropologia / Arqueologia'),
    ('2', 'Arquitetura e Urbanismo'),
    ('3', 'Artes / Musica'),
    ('4', 'Astronomia / Fisica'),
    ('5', 'Biodiversidade'),
    ('6', 'Biotecnologia'),
    ('7', 'Ciencia da Computacao'),
    ('8', 'Ciencia de Alimentos'),
    ('9', 'Ciencia Politica e Relacoes Internacionais'),
    ('10', 'Ciencias Agrarias'),
    ('11', 'Ciencias Ambientais'),
    ('12', 'Ciencias Biologicas I'),
    ('13', 'Ciencias Biologicas II'),
    ('14', 'Ciencias Biologicas III'),
    ('15', 'Ciencias Sociais Aplicadas I'),
    ('16', 'Direito'),
    ('17', 'Economia'),
    ('18', 'Educacao'),
    ('19', 'Educacao Fisica'),
    ('20', 'Enfermagem'),
    ('21', 'Engenharias I'),
    ('22', 'Engenharias II'),
    ('23', 'Engenharias III'),
    ('24', 'Engenharias IV'),
    ('25', 'Ensino'),
    ('26', 'Farmacia'),
    ('27', 'Filosofia/Teologia - Filosofia'),
    ('28', 'Filosofia/Teologia - Teologia'),
    ('29', 'Geociencias'),
    ('30', 'Geografia'),
    ('31', 'Historia'),
    ('32', 'Interdisciplinar'),
    ('33', 'Letras / Linguistica'),
    ('34', 'Matematica / Probabilidade e Estatistica'),
    ('35', 'Materiais'),
    ('36', 'Medicina I'),
    ('37', 'Medicina II'),
    ('38', 'Medicina III'),
    ('39', 'Medicina Veterinaria'),
    ('40', 'Nutricao'),
    ('41', 'Odontologia'),
    ('42', 'Planejamento Urbano e Regional / Demografia'),
    ('43', 'Psicologia'),
    ('44', 'Quimica'),
    ('45', 'Saude Coletiva'),
    ('46', 'Servico Social'),
    ('47', 'Sociologia'),
    ('48', 'Zootecnia / Recursos Pesqueiros'),

)


class DepartamentoAcademico(models.Model):
    nome = models.CharField('Nome', max_length=100)
    sigla = models.CharField('Sigla', max_length=100)
    # chefe = models.ForeignKey(Professor)
    # suplente = models.ForeignKey(Professor)
    #funcionario = [Funcionario]


class Funcionario(models.Model):
    nome = models.CharField('Nome', max_length=100)
    email = models.CharField('E-mail', max_length=200)
    telefone = models.CharField('Telefone', max_length=20)
    departamento = models.ForeignKey(DepartamentoAcademico)
    funcao = models.CharField('Funcao', max_length=100)


class Professor(Funcionario, models.Model):
    lattes = models.CharField('Link do Lattes', max_length=50)
    # nomeCompleto = models.ForeignKey(Professor, related_name = 'NomeProfessor')
    bolsaProdutividade = models.CharField('Bolsa Produtividade', max_length=100)
    enderecoProfissional = models.CharField('Endereco Profissional', max_length=255)
    nomeEmCitacoesBibliograficas = models.CharField('nomeEmCitacoesBibliograficas', max_length=255)
    textoResumo = models.CharField('bolsaProdutividade', max_length=500)


# enderecoProfissionalLat = models.CharField('Endereco Profissional Latitude ', max_length=255)
# enderecoProfissionalLon = models.CharField('Endereco Profissional Longitude', max_length=255)
#foto


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

