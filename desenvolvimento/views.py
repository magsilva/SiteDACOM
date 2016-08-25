from django.core.paginator import PageNotAnInteger, Paginator, EmptyPage

from .models import *
# from django
from itertools import chain

from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import Context, loader


def index(request):
    listadeProjetos = Projeto.objects.distinct().order_by('-datadefim', 'dataDeImportacao')
    listadeArtigos1 = ArtigoEmConferencia.objects.distinct().order_by('-data')
    listadeArtigos2 = ArtigoEmPeriodico.objects.distinct().order_by('-data')
    listaDeEventos =  Evento.objects.distinct().filter(ano='2016').order_by('-ano')

    integrantes = Integrante.objects.distinct().all()
    integrantesProfessor = IntegranteProfessor.objects.distinct().all()
    resultList = list(chain(listadeProjetos, listadeArtigos1, listadeArtigos2, listaDeEventos))
    projects =resultList

    return render_to_response('index.html', {'projects': projects, 'integrantes': integrantes, 'integrantesProfessor': integrantesProfessor})

def curso(request):
    listaDeCursos = Curso.objects.all().order_by('-nome')
    listaDeCoordenacao = Coordenacao.objects.all().order_by('-coordenador')
    listaDeColegiado = Colegiado.objects.all()
    empresaJunior = EmpresaJunior.objects.all()
    ca = CentroAcademico.objects.all()
    t = loader.get_template('curso.html')
    c = RequestContext(request, {
        'listaDeCursos': listaDeCursos,'listaDeCoordenacao':listaDeCoordenacao, 'listaDeColegiado':listaDeColegiado,
        'empresaJunior':empresaJunior, 'ca':ca
    })
    return HttpResponse(t.render(c))

def professor(request):

    listadeProf = Professor.objects.all().order_by('nome')
    paginator = Paginator(listadeProf, 10)
    page = request.GET.get('page')
    try:
        professores = paginator.page(page)
    except PageNotAnInteger:
    # If page is not an integer, deliver first page.
        professores = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
       professores= paginator.page(paginator.num_pages)
    return render_to_response('professor.html', {"professores": professores})


def projetos(request):

    listadeProjetos = Projeto.objects.distinct().all().order_by('-datadefim')
    paginator = Paginator(listadeProjetos, 10)
    page =  request.GET.get('page')
    try:
        projects = paginator.page(page)
    except PageNotAnInteger:
    # If page is not an integer, deliver first page.
        projects = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
       projects= paginator.page(paginator.num_pages)

    return render_to_response('projetos.html', {"projects": projects})



def publicacao(request):

    lista1 = ArtigoEmConferencia.objects.all().order_by('titulo')
    lista2 = ArtigoEmPeriodico.objects.all().order_by('titulo')
    t = loader.get_template('publicacoes.html')
    c = RequestContext(request, {
        'listadeArtigoEmPeriodico': lista2, 'listaDeArtigoEmConferencia': lista1
    })
    return HttpResponse(t.render(c))


def eventos(request):

    listadeEventos = Evento.objects.all().order_by('titulo')
    paginator = Paginator(listadeEventos, 10)
    page = request.GET.get('page')
    try:
        eventos = paginator.page(page)
    except PageNotAnInteger:
    # If page is not an integer, deliver first page.
        eventos = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
       eventos= paginator.page(paginator.num_pages)
    return render_to_response('eventos.html', {"eventos": eventos})



def detailCurso(request, sigla_curso):
     try:
        curso =  Curso.objects.get(sigla=sigla_curso)
        detailCurso = RelacaoDisciplinaCurso.objects.distinct().filter(cursoRelacao=curso.id).order_by('periodo')
        listaDeColegiado = Colegiado.objects.all()
        empresaJunior = EmpresaJunior.objects.all()
        ca = CentroAcademico.objects.all()
        curso = Curso.objects.all()
     except RelacaoDisciplinaCurso.DoesNotExist:
         raise Http404("CursoNaoExiste")
     return render(request, 'detailCurso.html', {'detailCurso': detailCurso, "curso":curso, 'listaDeColegiado':listaDeColegiado,
        'empresaJunior':empresaJunior, 'ca':ca
                                                 })


def detailCursoEmenta(request, sigla_curso, ementa):
     try:

        detailEmenta = Disciplina.objects.filter(nome=ementa)[0]
        detailRelacao = RelacaoDisciplinaCurso.objects.filter(disciplina__nome=detailEmenta.nome)[0]
        detailPlanoDeAula =  PlanoDeAula.objects.filter(codigodeTurma=detailEmenta.sigla).distinct()
        detailOferecimento = Oferecimento.objects.filter(disciplina__disciplina__nome=detailEmenta.nome)
     except Disciplina.DoesNotExist:
         raise Http404("ProjetoNaoExiste")
     return render(request, 'detailEmenta.html', {'detailRelacao':detailRelacao, 'detailEmenta': detailEmenta, 'detailPlanoDeAula':detailPlanoDeAula, 'detailOferecimento':detailOferecimento})



def detailsProfessor(request, professor_nome):
     try:
        detailsProf = Professor.objects.get(nome=professor_nome)
        detailsDado = DadosDeProfessor.objects.distinct().filter(professorDados=detailsProf.id)[0:5]
        proj = Projeto.objects.filter(integrantesProfessor__nome=professor_nome)
     except Projeto.DoesNotExist:
         raise Http404("ProjetoNaoExiste")
     return render(request, 'detailsProfessor.html', {'detailsProf': detailsProf, 'detailsDado':detailsDado, 'proj':proj})


def detailsProjeto(request, projeto_nome):
    try:
        detailsProjeto = Projeto.objects.filter(nome=projeto_nome)
    except Projeto.DoesNotExist:
        raise Http404("Professor does not exist")
    return render(request, 'detailsProjeto.html', {'detailsProjeto': detailsProjeto})




from django.shortcuts import ( render_to_response)
from django.template import RequestContext

#


def bad_request(request):
      return render_to_response('400.html')

def permission_denied(request):
      return render_to_response('403.html')

def page_not_found(request):
      return render_to_response('404.html')

def server_error(request):
      return render_to_response('500.html')
