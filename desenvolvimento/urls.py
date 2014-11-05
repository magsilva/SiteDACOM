from django.conf.urls.defaults import *
from django.conf.urls import url
from django.conf import settings

from django.contrib import admin
admin.autodiscover()




urlpatterns = patterns('desenvolvimento.views',
    (r'^$', 'index'),
    (r'^index.html', 'index'),
    (r'^curso.html', 'cursos'),
   # (r'^detalhesCurso.html', 'detalhesCurso'),
    (r'^professor.html', 'professores'),
    (r'^eventos.html', 'eventos'),
    (r'^detalhesCurso/(0-9]+)/$', 'detalhesCurso'),
   
    	
)

