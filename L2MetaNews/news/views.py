from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.

def index(request ):
    context = {'hello': 'Hello world'}
    return render(request, 'newsSite/index.html', {'contexto':context})

def download(request):
    return render(request, 'newsSite/download.html')

def discord(request):
    return redirect("https://discord.com/invite/jUkzwFNxDd")