from django.shortcuts import render, redirect, get_object_or_404
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
    return redirect("https://discord.gg/Zh4jjj86")

def login(request):
    return redirect("https://l2meta.cl/")

def news_list_by_category(request, news_id, category_id):
    recent_news_list = News.objects.all().order_by('-fechaSubida')[:5]  # Obtenemos las 5 noticias más recientes
    category = get_object_or_404(NewsCategory, pk=category_id)

    actualNew = get_object_or_404(News, pk=news_id)
    
    return render(request, 'newsSite/detail.html', {'category': category, 'actualNew': actualNew, 'recent_news_list': recent_news_list})

def donaciones(request):
    return render(request, 'newsSite/donaciones.html')

def rates(request):
    return render(request, 'newsSite/rates.html')
