from django.shortcuts import render
from .models import produtos, categoria


def index(request):
    produtos = produtos.objects.all()
    return render(request, 'index.html', {'produtos': produtos})

def produtos_view(request):
    categoria = categoria.objects.all()
    return render(request, 'produtos.html', {'categoria': categoria})

def contato(request):
    return render(request, 'contato.html')

