from django.core.paginator import PageNotAnInteger, Paginator, EmptyPage
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import RequestContext
from django.shortcuts import render_to_response
# from django.views.generic import CreateView
# from desenvolvimento.forms import Projet  oForm
from .models import *
# from django
from itertools import chain
from functools import reduce
from operator import and_, or_, attrgetter


def index(request):
    listadeProjetos = Projeto.objects.distinct().all().order_by('-datadefim')
    listadeArtigos = ArtigoEmPeriodico.objects.distinct().all().order_by('-data')

    integrantes = Integrante.objects.distinct().all()
    integrantesProfessor = IntegranteProfessor.objects.distinct().all()
    resultList = list(chain(listadeProjetos, listadeArtigos))
    projects =resultList

    return render_to_response('index.html', {'projects': projects, 'integrantes': integrantes, 'integrantesProfessor': integrantesProfessor})

def curso(request):
    listaDeCursos = Curso.objects.all().order_by('-nome')
    listaDeCoordenacao = Coordenacao.objects.all().order_by('-coordenador')
    t = loader.get_template('curso.html')
    c = RequestContext(request, {
        'listaDeCursos': listaDeCursos,'listaDeCoordenacao':listaDeCoordenacao,
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
        detailCurso = RelacaoDisciplinaCurso.objects.filter(cursoRelacao=curso.id)
        curso = Curso.objects.all()
     except RelacaoDisciplinaCurso.DoesNotExist:
         raise Http404("CursoNaoExiste")
     return render(request, 'detailCurso.html', {'detailCurso': detailCurso, "curso":curso})


def detailCursoEmenta(request, sigla_curso, ementa):
     try:
        detailEmenta = Disciplina.objects.filter(nome=ementa)[0]
        detailPlanoDeAula =  PlanoDeAula.objects.filter(codigodeTurma=detailEmenta.sigla)
     except Disciplina.DoesNotExist:
         raise Http404("ProjetoNaoExiste")
     return render(request, 'detailEmenta.html', {'detailEmenta': detailEmenta, 'detailPlanoDeAula':detailPlanoDeAula})



def detailsProfessor(request, professor_nome):
     try:
        detailsProf = Professor.objects.get(nome=professor_nome)
        detailsDado = DadosDeProfessor.objects.distinct().filter(professorDados=detailsProf.id)[0:5]
     except Projeto.DoesNotExist:
         raise Http404("ProjetoNaoExiste")
     return render(request, 'detailsProfessor.html', {'detailsProf': detailsProf, 'detailsDado':detailsDado})


def detailsProjeto(request, projeto_nome):
    try:
        detailsProjeto = Projeto.objects.filter(nome=projeto_nome)
    except Projeto.DoesNotExist:
        raise Http404("Professor does not exist")
    return render(request, 'detailsProjeto.html', {'detailsProjeto': detailsProjeto})
