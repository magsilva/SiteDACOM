<<<<<<< HEAD
from django.shortcuts import render

=======
>>>>>>> e75cb122e700f2a2f1b538f220809e0b1802c041
# Create your views here.

from django.template import loader
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
<<<<<<< HEAD
from desenvolvimento.models import *


def index(request):
    listadeProjetos = Projeto.objects.all().order_by('-dataInicio')[:5]
    t = loader.get_template('index.html')
=======
from models import *


def index(request):
    listadeProjetos = Projeto.objects.all().order_by('-dataInicio')
    t =loader.get_template('index.html')
>>>>>>> e75cb122e700f2a2f1b538f220809e0b1802c041
    c = RequestContext(request, {
        'listadeProjetos': listadeProjetos,
    })
    return HttpResponse(t.render(c))

<<<<<<< HEAD

=======
>>>>>>> e75cb122e700f2a2f1b538f220809e0b1802c041
def curso(request):
    listaDeCursos = Curso.objects.all().order_by('-nome')
    t = loader.get_template('curso.html')
    c = RequestContext(request, {
        'listaDeCursos': listaDeCursos,
    })
    return HttpResponse(t.render(c))

<<<<<<< HEAD

=======
>>>>>>> e75cb122e700f2a2f1b538f220809e0b1802c041
def professor(request):
    listasdeFunc = Professor.objects.all().order_by('nome')

    t = loader.get_template('professor.html')
    c = RequestContext(request, {
        'listasdeProf': listasdeFunc,
    })
    return HttpResponse(t.render(c))

<<<<<<< HEAD

=======
>>>>>>> e75cb122e700f2a2f1b538f220809e0b1802c041
def eventos(request):
    return render_to_response('eventos.html', {})

