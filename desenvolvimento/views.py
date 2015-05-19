from django.shortcuts import render


from django.template import loader
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response

from desenvolvimento.models import *


def index(request):
    listadeProjetos = Projeto.objects.all().order_by('-dataInicio')[:5]
    t = loader.get_template('index.html')


def index(request):
    listadeProjetos = Projeto.objects.all().order_by('-dataInicio')
    t =loader.get_template('index.html')
    c = RequestContext(request, {
        'listadeProjetos': listadeProjetos,
    })
    return HttpResponse(t.render(c))
def curso(request):
    listaDeCursos = Curso.objects.all().order_by('-nome')
    t = loader.get_template('curso.html')
    c = RequestContext(request, {
        'listaDeCursos': listaDeCursos,
    })
    return HttpResponse(t.render(c))
def professor(request):
    listasdeFunc = Professor.objects.all().order_by('nome')

    t = loader.get_template('professor.html')
    c = RequestContext(request, {
        'listasdeProf': listasdeFunc,
    })
    return HttpResponse(t.render(c))

def eventos(request):
    return render_to_response('eventos.html', {})

