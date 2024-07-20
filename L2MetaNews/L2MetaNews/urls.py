from django.contrib import admin
from django.urls import path, include, re_path
from django.http import HttpResponsePermanentRedirect

def redirect_to_www(request):
    return HttpResponsePermanentRedirect(f'http://www.l2meta.cl{request.get_full_path()}')

urlpatterns = [
    re_path(r'^(?!www\.).*$', redirect_to_www),  # Redirigir cualquier cosa que no empiece con 'www'
    path('', include("news.urls")),
    path('admin/', admin.site.urls),
]
