# Create your views here.

from django.template import Context, loader
from desenvolvimento.models import Curso, Professor, Coordenacao
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import get_object_or_404, render_to_response


def index(request):  
    return render_to_response('index.html', {})

def jquery1(request):
    return render_to_reponse('/static/desenvolvimento/novapasta/js/init.js', {})

def jquery2(request):
    return render_to_reponse('/static/desenvolvimento/novapasta/js/jquery.min.js',{})

def jquery3(request):
    return render_to_reponse('/static/desenvolvimento/novapasta/js/skel.min.js',{})

def jquery4(request):
    return render_to_reponse('/static/desenvolvimento/novapasta/js/ijquery.dropotron.min.js',{})

def jquery5(request):
    return render_to_reponse('/static/desenvolvimento/novapasta/js/skel-layers.min.js',{})

def curso(request):
    listaDeCursos = Curso.objects.all().order_by('-nome')
    t = loader.get_template('curso.html')
    c = RequestContext(request, {
        'listaDeCursos': listaDeCursos,
    })
    return HttpResponse(t.render(c))


#def professor(request):
 #   listaDeProfessores = Professor.objects.all().order_by('-nome')
  #  t = loader.get_template('professor.html')
   # c = RequestContext(request, {
    #  'listaDeProfessores': listaDeProfessores,
    #})
    #return HttpResponse(t.render(c))
    
def professor(request):  
    return render_to_response('professor.html', {})
    
def eventos(request):  
    return render_to_response('eventos.html', {})

      
