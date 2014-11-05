from django.conf.urls.defaults import *
from django.conf.urls import url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
	(r'^desenvolvimento/', include('desenvolvimento.urls')),
	(r'^admin/', admin.site.urls),
)
