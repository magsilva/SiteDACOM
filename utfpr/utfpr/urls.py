from django.conf.urls.defaults import *
from django.conf.urls import url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^desenvolvimento/$', 'desenvolvimento.views.index'),
    #(r'^desenvolvimento/curso.html$', 'desenvolvimento.views.cursos'),   
    #(r'^desenvolvimento/professor.html', 'desenvolvimento.professores'),
    #(r'^desenvolvimento/(?P<desenvolvimento_id>\d+)/$', 'desenvolvimento.views.detail'),
    #(r'^desenvolvimento/(?P<desenvolvimento_id>\d+)/results/$', 'desenvolvimento.views.results'),
    #(r'^desenvolvimento/(?P<desenvolvimento_id>\d+)/vote/$', 'desenvolvimento.views.vote'),
    (r'^admin/', admin.site.urls),
)
