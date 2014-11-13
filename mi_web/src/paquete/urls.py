from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'api.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'interfaz.views.home', name='home'),
    url(r'^login/', 'interfaz.views.login', name='login'),
    url(r'^logout/$', 'interfaz.views.logout', name='logout'),
    url(r'^sistema/$', 'interfaz.views.redirect', name='redirect'),
    url(r'^sistema/(?P<slug>[-\w]+)/$', 'interfaz.views.sistema', name='sistema'),    
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/1.0/pollo/', include('api_pollo.urls')),
)

