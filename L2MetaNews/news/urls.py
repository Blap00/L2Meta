from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('Download', views.download, name="downloads"),
    path('Discord', views.discord, name="discord"),
    path('Registrarse', views.login, name="login"),
    path('news/<int:news_id><int:category_id>/', views.news_list_by_category, name='news_detail'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)