import django.views.defaults
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls import handler400, handler403, handler404, handler500
admin.autodiscover()
from django.views.generic.base import TemplateView
urlpatterns = [
    url(r'^dacom', include('desenvolvimento.urls', namespace="desenvolvimento")),
    url(r'^dacom/search', include('haystack.urls', namespace="search")),
    url(r'^admin', include(admin.site.urls)),
]
handler400 = 'desenvolvimento.views.bad_request'
handler403 = 'desenvolvimento.views.permission_denied'
handler404 = 'desenvolvimento.views.page_not_found'
handler500 = 'desenvolvimento.views.server_error'