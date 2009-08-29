from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib import admin
from seaside.pages.views import seaside

admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    import os.path

    media = {'document_root': os.path.join(settings.PROJECT_BASE, 'media')}
    static = {'document_root': os.path.join(settings.PROJECT_BASE, 'static')}
    urlpatterns += patterns('django.views.static',
        (r'^media/(?P<path>.*)$', 'serve', media),
        (r'^static/(?P<path>.*)$', 'serve', static), 
    )
    
urlpatterns += patterns('',
    (r'^(?P<url>.*)$', seaside),
)