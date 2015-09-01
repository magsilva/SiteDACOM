from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
# from django.views.generic import CreateView
# from desenvolvimento.forms import Projet  oForm
from .models import *

#
# def index(request):
#      return render_to_response('index.html', {})


def index(request):
    listadeProjetos = Projeto.objects.all().order_by('-datadeFim')[:5]
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




# class ProjetoView(CreateView):
#  #template_name = 'form.html'
#  template_name = 'index.html'
#  model = Projeto
#  form_class = ProjetoForm
#  # success_url = '/envie/?sucesso=1#sucesso'
#
#
# #
# # def pesquisa(request):
#      if request.method=='POST':
#          form = searchform(request.get)
#          if form.is_valid():
#              form.save()
#              return render_to_response('pessoa/concluido.html',
# context_instance = RequestContext(request))
#      else:
#          form = PessoaForm()
#      return render_to_response('pessoa/cadastro.html', {'form': form,},
# context_instance = RequestContext(request))
# # def search(request):


#
# def buscar(request):
#     pass

#
# def view_generica(request, *args, **kwargs):
#     if request.GET['search']:
#         view_certa = buscar(request)
#     else:
#         return HttpResponse("Erro")
#
#     return view_certa(request, *args, **kwargs)

