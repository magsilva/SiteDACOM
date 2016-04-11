from django.contrib import admin
from django.conf.urls import url
from django.conf.urls.static import static

from projectUtfpr import settings
from . import views
admin.autodiscover()

urlpatterns = [
      url(r'^$', views.index, name='index'),
      url(r'^index', views.index,  name='index'),
      url(r'^curso', views.curso, name='curso'),
      url(r'^(?P<curso_id>.+)/$', views.detailCurso, name='detailCurso'),
      url(r'^(?P<curso_id>.+)/(?P<ementa>.+)$', views.detailCursoEmenta, name='detailCursoEmenta'),
      url(r'^professor', views.professor, name='professor'),
      url(r'^projetos', views.projetos, name='projetos'),
      url(r'^eventos', views.eventos, name='eventos'),
      url(r'^(?P<projeto_professor>[0-9]+)/$', views.details, name='details'),
      url(r'^(?P<projeto_projeto>.+)/$', views.detailsProjeto, name='detailsProjeto'),
      #modificar 
      # url(r'^(?P<projeto_projeto>[0-9]+)/projetos/$', views.detailsProjeto, name='detailsProjeto'),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
