from django.conf.urls import include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    url(r'^dacom', include('desenvolvimento.urls', namespace="desenvolvimento")),
    url(r'^dacom/search', include('haystack.urls', namespace="haystack")),
    url(r'^admin', include(admin.site.urls)),
    url(r'^cms', include('cms.urls')),
    url(r'^tinymce/', include('tinymce.urls')),
    # url(r'^admincms/', include('cms.urls')),
]