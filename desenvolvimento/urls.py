from django.contrib import admin
from django.conf.urls import url, include
from django.conf.urls.static import static

from projectUtfpr import settings
from . import views
from django.conf.urls.static import static
from django.conf.urls import handler404
from django.conf.urls import patterns, include, url
from desenvolvimento import views

admin.autodiscover()

urlpatterns = [
      url(r'^$', views.index, name='index'),
      url(r'^/curso$', views.curso, name='curso'),
      url(r'^/professor$', views.professor, name='professor'),
      url(r'^/projeto$', views.projetos, name='projetos'),
      url(r'^/evento$', views.eventos, name='eventos'),
      url(r'^/curso/(?P<sigla_curso>.+)/$', views.detailCurso, name='detailCurso'),
      url(r'^/curso/(?P<sigla_curso>.+)/(?P<ementa>.+)$', views.detailCursoEmenta, name='detailCursoEmenta'),
      url(r'^/professor/(?P<professor_nome>.+)$', views.detailsProfessor, name='details'),
      url(r'^/projeto/(?P<projeto_nome>.+)$', views.detailsProjeto, name='detailsProjeto'),


      #modificar

]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


handler400 = 'desenvolvimento.views.page_not_found'
handler403 = 'desenvolvimento.views.permission_denied'
# handler404 = 'desenvolvimento.views.page_not_found'
handler500 = 'desenvolvimento.views.server_error'