from django.conf import settings
from django.conf.urls.defaults import *
from django.conf.urls.static import static
from django.contrib import admin
from seaside.pages.views import seaside


admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^(?P<url>.*)$', seaside),
) 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
