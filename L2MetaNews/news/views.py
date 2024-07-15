from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request ):
    context = {'hello': 'Hello world'}
    return render(request, 'newsSite/index.html', {'contexto':context})