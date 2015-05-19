from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import patterns
<<<<<<< HEAD
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
=======

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
>>>>>>> e75cb122e700f2a2f1b538f220809e0b1802c041

