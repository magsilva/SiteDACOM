from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import patterns
admin.autodiscover()

urlpatterns = patterns('desenvolvimento.views',
                      url(r'^', 'index', name='index'),
                      url(r'^index', 'index', name='index'),
                      url(r'^curso', 'curso', name='curso'),
                       # (r'^detalhesCurso.html', 'detalhesCurso'),
                      url(r'^professor', 'professor', name='professor'),
                      url(r'^eventos', 'eventos', name='eventos'),
                       # (r'^detalhesCurso/(0-9]+)/$', 'detalhesCurso'),
                       )

