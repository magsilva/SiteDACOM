from django.core.paginator import PageNotAnInteger, Paginator, EmptyPage
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
    listadeProjetos = Projeto.objects.all().order_by('-datadeFim')
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

    return render_to_response('index.html', {"projects": projects})
    #
    # t =loader.get_template('index.html')
    # c = RequestContext(request, {
    #     'listadeProjetos': listadeProjetos,
    # })
    # return HttpResponse(t.render(c))


# contact_list = Contacts.objects.all()
#     paginator = Paginator(contact_list, 25) # Show 25 contacts per page
#
#     page = request.GET.get('page')
#     try:
#         contacts = paginator.page(page)
#     except PageNotAnInteger:

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

