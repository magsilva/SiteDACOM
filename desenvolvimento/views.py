# Create your views here.

from django.template import Context, loader
from desenvolvimento.models import Curso, Professor
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import get_object_or_404, render_to_response


def index(request):  
    return render_to_response('index.html', {})


def cursos(request):
    listaDeCursos = Curso.objects.all().order_by('-nome')
    t = loader.get_template('curso.html')
    c = RequestContext(request, {
      'listaDeCursos': listaDeCursos ,
    })
    return HttpResponse(t.render(c))


def professores(request):
    listaDeProfessores = Professor.objects.all().order_by('-nome')
    t = loader.get_template('professor.html')
    c = RequestContext(request, {
      'listaDeProfessores': listaDeProfessores,
    })
    return HttpResponse(t.render(c))
    
    
def eventos(request):  
    return render_to_response('eventos.html', {})
    #ultimosEventos = Eventos.objects.order_by('-nome')[:5]
    #template = loader.get_template('eventos.html')
    #context = RequestContext(request, {
    # 	'ultimosEventos': ultimosEventos,
    #})
    #return HttpResponse(template.render(context))
    
    
#def detalhes(request):  
 #   detailCurso = get_object_or_404(Curso, pk=curso_id)
  #  return render_to_response('detalhes.html', {'detailCurso': detailCurso})
  
  
      
def detalhesCurso(request, curso_id):
    p = get_object_or_404(Curso, pk=curso_id)
    return render_to_response('detalhesCurso.html', {'curso': p})

      
      
      
