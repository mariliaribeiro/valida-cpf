from django.conf.urls import patterns, include, url
#from django.conf.urls.defaults import *

#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'agenda.views.index')
    # Examples:
    # url(r'^$', 'gerenciador.views.home', name='home'),
    # url(r'^$', 'gerenciador.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
)