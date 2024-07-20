from django.contrib import admin
from django.urls import path, include, re_path
from django.http import HttpResponsePermanentRedirect

def redirect_to_www(request):
    return HttpResponsePermanentRedirect(f'http://www.{request.get_host()}{request.get_full_path()}')

urlpatterns = [
    re_path(r'^(?i)(?!www\.).*$', redirect_to_www),  # redirigir lo que no empiece con 'www'
    path('', include("news.urls")),
    path('admin/', admin.site.urls),
]
