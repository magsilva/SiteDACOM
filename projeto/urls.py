from django.conf.urls.defaults  import  *
from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'desenvolvimento.views.index', name='index'),
    # url(r'^projeto/', include('projeto.foo.urls')),
    # (r'^DepartamentoAcademico/$', 'desenvolvimento.DepartamentoAcademico.views.index', name='index'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # (r'^$', 'index'),
    # Uncomment the next line to enable the admin:
    # url(r'^$', 'desenvolvimento.DepartamentoAcademico.views.index', name='index'),
	url(r'^Curso/', include('Curso.urls', namespace="Curso")),
	url(r'^admin/', include(admin.site.urls)),
)
