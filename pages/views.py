# Create your views here.
from django.template import loader, RequestContext
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.utils.safestring import mark_safe

from seaside.pages.models import SeasidePage

DEFAULT_TEMPLATE = 'seaside/default.html'

def seaside(request, url):
    """Seaside page view."""
    if not url.startswith('/'):
        url = "/" + url
    if not url.endswith('/') and settings.APPEND_SLASH:
        return HttpResponseRedirect("%s/" % request.path)

    s = get_object_or_404(SeasidePage, url__exact=url)
    s.title = mark_safe(s.title)
    s.content = mark_safe(s.content)
    c = RequestContext(request, {
        'seaside': s,
    })
    t = loader.get_template(DEFAULT_TEMPLATE)
    return HttpResponse(t.render(c))
