from django.contrib import admin
from django.conf.urls import url

from . import views
admin.autodiscover()

urlpatterns = [
      url(r'^$', views.index, name='index'),
      url(r'^index', views.index,  name='index'),
      url(r'^curso', views.curso, name='curso'),
      url(r'^professor', views.professor, name='professor'),
      url(r'^projetos', views.projetos, name='projetos'),
      url(r'^eventos', views.eventos, name='eventos'),
      url(r'^(?P<projeto_professor>[0-9]+)/$', views.details, name='details'),
      # url(r'^(?P<projeto_professor>[0-9]+)/projetos/$', views.detailsProjeto, name='detailsProjeto'),
]

