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

    listadeIntegrantes = Integrante.objects.distinct().all().order_by('-datadefim')
    listadeIntegrantesProfessor = IntegranteProfessor.objects.distinct().all().order_by('-datadefim')
    resultList = list(chain(listadeProjetos, listadeArtigos))
    projects =resultList
    # resultList = listadeProjetos | listadeArtigos
    # resultList = sorted(chain(listadeProjetos, listadeArtigos))
    # resultList = listadeProjetos. listadeArtigos
    # paginator = Paginator(resultList, 10)
    # page =  request.GET.get('page')
    # try:
    #   projects = paginator.page(page)
    # except PageNotAnInteger:
    #     # If page is not an integer, deliver first page.
    #     projects = paginator.page(1)
    # except EmptyPage:
    #         # If page is out of range (e.g. 9999), deliver last page of results.
    #     projects= paginator.page(paginator.num_pages)
    # return render_to_response('index.html', {'projects': projects})
    return render_to_response('index.html', {'projects': projects, 'integrantes': listadeIntegrantes, 'integrantesProfessor': listadeIntegrantesProfessor})

def curso(request):
    listaDeCursos = Curso.objects.all().order_by('-nome')
    t = loader.get_template('curso.html')
    c = RequestContext(request, {
        'listaDeCursos': listaDeCursos,
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


def details(request, projeto_professor):
    try:
        details = Projeto.objects.filter(professor=projeto_professor)
    except Projeto.DoesNotExist:
        raise Http404("Professor does not exist")
    return render(request, 'detailsProjeto.html', {'details': details})


def detailsProjeto(request, projeto_projeto):
    try:
        detailsProjeto = Projeto.objects.filter(nome=projeto_projeto)
    except Projeto.DoesNotExist:
        raise Http404("Professor does not exist")
    return render(request, 'detailsProfessor.html', {'detailsProjeto': detailsProjeto})

