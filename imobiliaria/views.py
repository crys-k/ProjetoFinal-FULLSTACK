from django.shortcuts import render


def index(request):
    return render(request, 'imobiliaria/index.html')
