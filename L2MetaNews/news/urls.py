from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('Download', views.download, name="downloads"),
    path('Discord', views.discord, name="discord"),
    path('Log-in', views.login, name="login"),
    
]