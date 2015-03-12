from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'weblattes.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'proxy.views.index', name='index'),
    url(r'^status/(?P<lid>\S+)/(?P<categoria>\S+)/', 'proxy.views.processando', name='status'),

    url(r'^admin/', include(admin.site.urls)),
)
