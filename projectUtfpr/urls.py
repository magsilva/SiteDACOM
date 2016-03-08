from django.conf.urls import include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    url(r'^desenvolvimento/', include('desenvolvimento.urls', namespace="desenvolvimento")),
    url(r'^search/', include('haystack.urls', namespace="haystack")),
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^admincms/', include('cms.urls')),
]