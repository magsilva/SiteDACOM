from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import patterns
admin.autodiscover()

urlpatterns = patterns('desenvolvimento.views',
                      url(r'^$', 'views.index', name='index'),
                      url(r'^index/$', 'views.index', name='index'),
                      url(r'^curso/$', 'views.curso', name='curso'),
                       # (r'^detalhesCurso.html', 'detalhesCurso'),
                      url(r'^professor/$', 'views.professor', name='professor'),
                      url(r'^eventos/$', 'views.eventos', name='eventos'),
                       # (r'^detalhesCurso/(0-9]+)/$', 'detalhesCurso'),
                       )

