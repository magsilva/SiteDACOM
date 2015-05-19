from django.conf.urls import include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'projectUtfpr.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^desenvolvimento/', include('desenvolvimento.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
