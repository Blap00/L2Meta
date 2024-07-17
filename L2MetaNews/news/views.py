from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import NewsCategory,News

# Create your views here.

def index(request):

    category = NewsCategory.objects.all()  # Ejecutar el método
    recent_news_list = News.objects.all().order_by('-fechaSubida')[:10]  # Obtener noticias recientes
    news_list = News.objects.filter(category__in=category)  # Filtrar noticias por categorías
    
    return render(request, 'newsSite/index.html', {
        'category': category,
        'news_list': news_list,
        'recent_news_list': recent_news_list
    })

def download(request):
    return render(request, 'newsSite/download.html')

def discord(request):
    return redirect("https://discord.com/invite/jUkzwFNxDd")

def login(request):
    return redirect("https://l2meta.cl/")

def news_list_by_category(request, news_id, category_id):
    recent_news_list = News.objects.all().order_by('-fechaSubida')[:5]  # Obtenemos las 5 noticias más recientes

    category = NewsCategory.objects.get(pk=category_id)
    news = News.objects.filter(category=news_id)
    return render(request, 'newsSite/detail.html', {'category': category, 'actualNew': news, 'recent_news_list': recent_news_list})