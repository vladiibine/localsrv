import django
from django.conf.urls import url, include
from django.contrib import admin
from . import urls

django_version = django.get_version()
if '1.4' <= django_version < '1.7':
    admin.autodiscover()


urlpatterns = [
    # Examples:
    # url(r'^$', 'localsrv.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^serve/', include(urls, namespace='serve')),
]
