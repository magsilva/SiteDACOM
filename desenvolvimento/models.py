import os


from django.db import models
from django.db.models import ImageField

from projectUtfpr.settings import STATIC_ROOT, MEDIA_ROOT


class DepartamentoAcademico(models.Model):
    nome = models.CharField('Nome', max_length=100)
    sigla = models.CharField('Sigla', max_length=100)


    def __unicode__(self):
        return self.nome

class Pessoa(models.Model):
    nome = models.CharField('Nome', max_length=100)
    email = models.CharField('E-mail', max_length=200, null=True, blank=True)
    telefone = models.CharField('Telefone', max_length=20, null=True, blank=True)

class Servidor(Pessoa):
    departamento = models.ForeignKey(DepartamentoAcademico)
    funcao = models.CharField('Funcao', max_length=100, blank=True, null=True)
    lattes = models.CharField('Link do Lattes', max_length=50, null=True, blank=True)
    bolsaprodutividade = models.CharField('Bolsa Produtividade', max_length=100, null=True, blank=True)
    enderecoprofissional = models.CharField('Endereco Profissional', max_length=5000, null=True, blank=True)
    nomeemcitacoesbibliograficas = models.CharField('Nome em Citacoes Bibliograficas', max_length=255, null=True, blank=True)
    textoResumo = models.CharField('bolsaProdutividade', max_length=500, null=True, blank=True)
    profile_image = ImageField(upload_to="", blank=True, null=True)

    def __unicode__(self):
        return self.nome

class TecnicoAdm(Servidor):
    pass

class Professor(Servidor):
    pass


class DadosDeProfessor(models.Model):
    nome = models.CharField('nome do professor', max_length=100)
    professorDados =  models.ForeignKey(Professor, related_name='DadosDeProfessor')

class Formacao(models.Model):
    ano_inicio = models.CharField('Ano de Inicio', max_length=4)
    ano_conclusao = models.CharField('Ano de Conclusao', max_length=4)
    tipo = models.CharField('Tipo', max_length=511)
    descricao = models.CharField('Descricao', max_length=5000)
    nome = models.CharField('Nome', max_length=5000)
    formacaoProfessor = models.ForeignKey(Professor, related_name='FormacaoProfessor')
    def __unicode__(self):
        return self.nome

class AreaDeAtuacao(models.Model):
    descricao = models.CharField('Area de Atuacao', max_length=511)
    areaProfessor = models.ForeignKey(Professor, related_name='AreaProfessor')
    def __unicode__(self):
        return self.descricao

class Curso(models.Model):
    nome = models.CharField('Curso', max_length=50)
    sigla = models.CharField('Sigla', max_length=20, null=True, blank=True)
    departamentoAcademico = models.ForeignKey(DepartamentoAcademico, related_name="DepartamentoAcademico")
    perfilDoEgresso=models.CharField('perfilDoEgresso',  max_length=10000, null=True, blank=True)
    descricao = models.CharField('Descricao', max_length=5000, null=True, blank=True)
    contato = models.CharField('Contato', max_length=100, null=True, blank=True)
    matrizAtual = models.ForeignKey('Matriz', related_name="matrizNome",  null=True, blank=True)
    regulamentacao  =  models.CharField('Regulamentacao',  max_length=1000, null=True, blank=True )

     # PPP = models.CharField("Projeto Politico Pedagogico Institucional")
    # PDI = models.CharField("Plano de Desenvolvimento Institucional")
    # Regulamento =
    def __unicode__(self):
        return self.nome



class Matriz(models.Model):
    atividadeComplementar = models.CharField('Atividade Complementar', max_length=256, null=True, blank=True)
    cargaHoraria =  models.CharField('CargaHoraria', max_length=50, null=True, blank=True)
    estagio =  models.CharField('Estagio',  max_length=256, null=True, blank=True)
    tcc =  models.CharField('tcc',  max_length=10000, null=True, blank=True)
    duracao = models.CharField('Duracao', max_length=50, null=True, blank=True)
    turno = models.CharField('Turno', max_length=50, null=True, blank=True)
    curso =  models.ForeignKey("curso")
    numero =  models.IntegerField(default=0)
    # projetoPedagogico =  models.CharField("Projeto pedagogico")

    def __unicode__(self):
        return self.curso.nome
    # matrizAtual = models.ForeignKey('self', related_name="matrizatual",  null=True, blank=True)#comentar
    #

# class Colegiado(models.Model):
#     professores = models.ManyToManyField(Professor, related_name='colegiado', blank=True)
#


class Disciplina(models.Model):
    nome = models.CharField('Nome da Disciplina', max_length=50, null=True, blank=True)
    sigla = models.CharField('Sigla da Disciplina', max_length=50, null=True, blank=True)
    objetivo = models.CharField('objetivo', max_length=5000,  null=True, blank=True)
    ementa = models.CharField('Ementa', max_length=5000, null=True, blank=True)
    cargaHorariaTeorica =models.CharField('Carga Horaria Teorica', max_length=50)
    cargaHorariaPratica = models.CharField('Carga Horaria Pratica', max_length=50)
    cargaHorariaAPS =models.CharField('Carga Horaria Atividade Pratica Supervisionada', max_length=50)
    cargaHorariaTotal =models.CharField('Carga Horaria Total', max_length=50)
    matriz = models.ManyToManyField(Curso, related_name="matrizNome", null=True, blank=True)
    departamentoAcademico = models.ForeignKey(DepartamentoAcademico, related_name="NomeDepartamentoAcademico", null=True, blank=True)
    prerequisito1 = models.ManyToManyField('self', related_name="prerequisito", symmetrical=False, null=True, blank=True)
    equivalencia2 = models.ManyToManyField('self', related_name="equivalencia", symmetrical=False, null=True, blank=True)

    def __unicode__(self):
        return self.nome

class RelacaoDisciplinaCurso(models.Model):

    periodo = models.IntegerField('Periodo')

    OptativaHumanas = 'OH'
    OptativaProfissionalizante  = 'OP'
    NucleoComum = 'NC'
    FormacaoProfissionalizante = 'FP'

    TIPODEDISCIPLINA = (
        (OptativaHumanas, 'Optativa Humanas'),
        (OptativaProfissionalizante, 'Optativa Profissionalizante'),
        (NucleoComum, 'Nucleo Comum'),
        (FormacaoProfissionalizante, 'Formacao Profissionalizante'),
    )
    tipo  = models.CharField(max_length=2,
                                      choices=TIPODEDISCIPLINA,
                                      default=FormacaoProfissionalizante)
    matriz =  models.ForeignKey(Matriz, related_name='matrizAtual', null=True, blank=True)
    cursoRelacao = models.ForeignKey(Curso, related_name="CursoRelacionado", null=True, blank=True)
    disciplina = models.ForeignKey(Disciplina, related_name="DisciplinaRelacionada",null=True, blank=True)

    def __unicode__(self):
        return self.disciplina.nome

class Coordenacao(models.Model):
    coordenador = models.ForeignKey(Professor, related_name='coordenadorCoo')
    suplente = models.ForeignKey(Professor, related_name='suplenteCoo')
    curso = models.ForeignKey(Curso,related_name='Curso' )

class ChefiaDoDepartamento(models.Model):
    chefe = models.ForeignKey(Professor, related_name='chefeDeDepartamento',blank=True, null=True)
    suplente = models.ForeignKey(Professor, related_name='suplenteChefe', blank=True, null=True)
    departamentoAcademico = models.ForeignKey(DepartamentoAcademico,related_name='departamentoAcademico' ,blank=True, null=True )


class Integrante(models.Model):
    nome = models.CharField('nome', max_length=255)
    ehCoordenador = models.BooleanField(default=False)
    def __unicode__(self):
        return self.nome

class IntegranteProfessor(Integrante):
    professor=  models.ForeignKey(Professor, related_name='ProfessorIntegrante')

class Artigo(models.Model):
    listadeautores = models.CharField('Lista de Autores', max_length=5000)
    titulo = models.CharField('Titulo do Artigo', max_length=255)
    data = models.CharField('Data do Artigo', max_length=5)
    doi = models.CharField('DOI', max_length=255, null=True, blank=True)
    paginas = models.CharField('Paginas', max_length=10, null=True, blank=True)
    resumo = models.CharField('Resumo', max_length=5000)
    professores= models.ManyToManyField(Professor,related_name="ArtigoProfessor")

    def __unicode__(self):
        return self.titulo

class ArtigoEmPeriodico(Artigo):
    nomejournal = models.CharField('Nome Journal', max_length=255)
    ISSN = models.CharField('Codigo ISSN', max_length=255)
    publisher = models.CharField('Editora', max_length=255)
    numero = models.CharField('Numero', max_length=100)
    volume = models.CharField('Volume', max_length=100)
    integrantes = models.ManyToManyField(Integrante,related_name="integrantes")
    integrantesProfessor = models.ManyToManyField(IntegranteProfessor,related_name="integrantesProfessor")

    def __unicode__(self):
        return self.titulo

class ArtigoEmConferencia(Artigo):#trabalho em congresso
    nomedaConferencia = models.CharField('Nome da Conferencia', max_length=255)
    ISSN = models.CharField('Codigo ISSN', max_length=50)
    ISBN = models.CharField('Codigo ISBN', max_length=50)
    local = models.CharField('Local da Conferencia', max_length=255)
    ano = models.CharField('Ano', max_length=4)



class Projeto(models.Model):
    datainicio = models.CharField('Data Inicio', max_length=5, null=True, blank=True)
    datadefim = models.CharField('Data de Fim', max_length=5, null=True, blank=True)
    agendafinanciadora = models.CharField('Agencia Financiadora', max_length=255, null=True, blank=True)
    nome = models.CharField('Nome do Projeto', max_length=1000)
    resumo = models.CharField('Resumo', max_length=10000)
    situacao = models.CharField('Situacao', max_length=1000, null=True, blank=True)
    natureza = models.CharField('Natureza', max_length=1000, null=True, blank=True)
    integrantes = models.ManyToManyField(Integrante,related_name="integrante", null=True, blank=True)
    integrantesProfessor = models.ManyToManyField(IntegranteProfessor,related_name="integranteProfessor",null=True, blank=True)

    def __unicode__(self):
        return self.nome



class Evento(models.Model):
    doi = models.CharField('DOI', max_length=255)
    autores = models.CharField('Autores', max_length=5000)
    titulo = models.CharField('Titulo', max_length=5000)
    nomeevento = models.CharField('Nome do Evento', max_length=5000, null=True, blank=True)
    ano = models.CharField('Ano', max_length=4)
    volume = models.CharField('Volume', max_length=10)
    paginas = models.CharField('Paginas', max_length=255)
    professoresDoEvento= models.ManyToManyField(Professor,related_name="professoresDoEvento");

    def __unicode__(self):
        return self.titulo


def user_directory_path(instance, filename):
    semestre ="1"
    ano ="2016"
    siglaDoCurso = "BCC"

    diretorio = MEDIA_ROOT+"/"+siglaDoCurso+"/planoDeAula/"+ano+"/"+semestre+"/"
    nomeDoArquivo = "BCC34A_IC4A"
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return diretorio+instance.disciplina.nome


class PlanoDeAula(models.Model):

    upload = models.FileField(upload_to=user_directory_path,null=True, blank=True)
    disciplina= models.ForeignKey(Disciplina, related_name="Disciplina")
    ano = models.CharField('Ano',max_length=4, null=True, blank=True )
    semestre = models.CharField('semestre', max_length=20 ,null=True, blank=True)
    codigodeTurma = models.CharField('codigodaTurma', max_length=15, null=True, blank=True)
    # upload = sigladocursop + plano de aula/ano/semestre
    #nome do arquivo:  codigodadisciplina + codigodeturma


class DiaDaSemana(models.Model):
    Segunda = 'Segunda'
    Terca  = 'Terca'
    Quarta = 'Quarta'
    Quinta = 'Quinta'
    Sexta = 'Sexta'
    Sabado ='Sabado'

    DIAS_DA_SEMANA =(
       (Segunda, "Segunda"),
       (Terca, "Terca"),
       (Quarta, 'Quarta'),
       (Quinta, "Quinta"),
       (Sexta, "Sexta"),
       (Sabado, "Sabado"),
    )
    diaDaSemana =models.CharField(max_length=10, choices=DIAS_DA_SEMANA, default=Segunda)

    def __unicode__(self):
        return self.diaDaSemana

class HorarioDaAula(models.Model):

    M1 = 'M1'
    M2 = 'M2'
    M3 = 'M3'
    M4 = 'M4'
    M5 = 'M5'
    M6 = 'M6'
    T1 = 'T1'
    T2 = 'T2'
    T3 = 'T3'
    T4 = 'T4'
    T5 = 'T5'
    T6 = 'T6'
    N1 = 'N1'
    N2 = 'N2'
    N3 = 'N3'
    N4 = 'N4'
    N5 = 'N5'



    HORARIO_DE_AULA = (
      (M1, "07h30 - 08h20"),
      (M2, "08h20 - 09h10"),
      (M3, "09h10 - 10h00"),
      (M4, "10h20 - 11h10"),
      (M5, "11h10 - 12h00"),
      (M6, "12h00 - 12h50"),
      (T1, "13h00 - 13h50"),
      (T2, "13h50 - 14h40"),
      (T3, "14h40 - 15h30"),
      (T4, "15h50 - 16h40"),
      (T5, "16h40 - 17h30"),
      (T6, "17h30 - 18h20"),
      (N1, "18h40 - 19h30"),
      (N2, "19h30 - 20h20"),
      (N3, "20h20 - 21h10"),
      (N4, "21h20 - 22h10"),
    (N5, "22h10 - 23h00"),
    )


    horarioDeAula = models.CharField(max_length=13, choices=HORARIO_DE_AULA, default=M1)

    def __unicode__(self):
        return self.horarioDeAula.choices

class RelacaoDiaDaSemanaHorarioDeAula(models.Model):
    dia =  models.ForeignKey(DiaDaSemana,  related_name="diadaaula")
    horario = models.ForeignKey(HorarioDaAula, related_name="Horariodaaula")
    def __unicode__(self):
        return u"%s - %s" % (self.dia.diaDaSemana, self.horario.horarioDeAula)

class Oferecimento(models.Model):
    OferecidaPeloProfessor =  models.ManyToManyField(Professor, related_name="Oferecida")
    disciplina = models.ForeignKey(RelacaoDisciplinaCurso, related_name="Disciplinaoferecida")
    turma = models.CharField("Turma", max_length=50)
    sala  = models.CharField("SalaDeAula", max_length=10)
    relacaoDiaHorarioAula = models.ManyToManyField(RelacaoDiaDaSemanaHorarioDeAula,  related_name="relacaoDoDiadaSemanaHorario")
    def __unicode__(self):
        return u"%s - %s - %s - %s " % (self.disciplina, self.turma ,self.OferecidaPeloProfessor.all, self.relacaoDiaHorarioAula.all)

class Comissao(models.Model):
    pass

class Colegiado(Comissao):
    profCoordenador = models.ForeignKey(Professor, related_name='professorCoordenador')
    profResponsavelPeloEstagio = models.ForeignKey(Professor, related_name='professorResponsavelPeloEstagio')
    profResponsavelPeloTCC = models.ForeignKey(Professor, related_name='professorResponsavelPeloTCC')
    profResponsavelPelasAtividadesCompl = models.ForeignKey(Professor, related_name='professorResponsavelPelasAtividadesCompl')

class Aluno(models.Model):
    nome  = models.CharField("nomeDoAluno", max_length=500)
    cursoDoAluno = models.ForeignKey(Curso,related_name="CursodoAluno")
    RA = models.IntegerField(default=000000)
    periodo = models.IntegerField(default=1)

class MembroEleito(models.Model):
    membroEleitos =  models.ForeignKey(Pessoa, related_name='MembroEleito', blank=True, null=True)
    membroSuplentes =  models.ForeignKey(Pessoa, related_name='MembroSuplente', null=True, blank=True)
    observacao = models.CharField("Observacao", max_length=500)
    colegiado = models.ForeignKey(Comissao,related_name="ComissaoDoCurso", null=True, blank=True )
    dataInicio = models.DateTimeField()
    dataFim = models.DateTimeField()
    # aluno ="Al"
    # servidor ="SR"
    #
    # razao = (
    #     (aluno, "Aluno"),
    #     (servidor, "Servidor")
    # )
    #
    # razao = models.CharField(max_length=10, choices=razao, default=servidor)


class NDE (Comissao):
    professorCoordenador = models.ForeignKey(Professor, related_name='ProfessorCoordenador')

class EmpresaJunior(models.Model):
    nome = models.CharField("nomeDaEmpresaJunior", max_length=100)
    departamento =models.ForeignKey(DepartamentoAcademico, related_name="Departamento")
    descricao = models.CharField("descricao", max_length=500)
    linkParaoSite = models.CharField("linkParaoSite", max_length=100, null=True, blank=True)
    linkParaAPage =  models.CharField("linkParaAPage", max_length=100, null=True, blank=True)
    def __unicode__(self):
        return self.nome

class CentroAcademico(models.Model):
    nome =  models.CharField("nome Do CA", max_length=500)
    curso = models.ForeignKey(Curso, max_length=500)
    descricao = models.CharField("descricao", max_length=500)
    linkParaoSite = models.CharField("linkParaoSite", max_length=100, null=True, blank=True)
    linkParaAPage =  models.CharField("linkParaAPage", max_length=100, null=True, blank=True)
    def __unicode__(self):
        return self.nome

class Estagiario(models.Model):
    nome  = models.CharField("nomeDoEstagiario", max_length=500)
    funcao =  models.CharField("Funcao", max_length=500)
    dataInicial =  models.CharField("DataDeAdmissao",max_length=10, blank=True, null=True)
    dataFinal =  models.CharField("DataDeConclusao",max_length=10, blank=True, null=True)

class CalendarioAcademico(models.Model):
    data =  models.CharField("Data", max_length=10, blank=True, null=True)
    evento = models.CharField("evento", max_length=10000)

class InfraEstrutura(models.Model):
    chefiaDeDepartamento = models.CharField(500, max_length=100)
    telefoneDaChefia =  models.CharField("TelefoneDoDepartamento", max_length=20,null=True, blank=True)
    telefoneDaSalaDosProfessores =  models.CharField("TelefoneDaSala", max_length=20,null=True, blank=True)
    salaDeProfessores = models.CharField(500, max_length=100)
    secretaria =models.CharField(500, max_length=100)
    # salas = models.ManyToOneRel(Sala, related_name="salas")


class Sala(models.Model):
    sala  = models.CharField("sala", max_length=100, null=True, blank=True)
    departamento = models.ForeignKey(DepartamentoAcademico, related_name="DepartamerntoAcademico", null=True, blank=True)
    ehLaboratorio = models.BooleanField(default=False)
    infraEstruturaDoDepartamento = models.ForeignKey(InfraEstrutura, related_name="InfraestuturaDoDepartamento", null=True, blank=True)
