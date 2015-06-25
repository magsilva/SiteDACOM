from django.conf.urls import include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    url(r'^desenvolvimento/', include('desenvolvimento.urls', namespace="desenvolvimento")),
    url(r'^search/', include('haystack.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
