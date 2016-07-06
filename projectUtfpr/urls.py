from django.conf.urls import include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    url(r'^dacom', include('desenvolvimento.urls', namespace="desenvolvimento")),
    url(r'^dacom/search', include('haystack.urls', namespace="search")),
    url(r'^admin', include(admin.site.urls)),
]
