from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import patterns

admin.autodiscover()

urlpatterns = patterns('desenvolvimento.views',
                        (r'^$', 'index'),
                       (r'^index', 'index'),
                       (r'^curso', 'curso'),
                       # (r'^detalhesCurso.html', 'detalhesCurso'),
                       (r'^professor', 'professor'),
                       (r'^eventos', 'eventos'),
                       #(r'^detalhesCurso/(0-9]+)/$', 'detalhesCurso'),


)

