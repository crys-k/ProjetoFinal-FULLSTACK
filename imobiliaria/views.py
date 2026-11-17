from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render


def login_view(request):
    if request.method == 'POST':
        usuario = request.POST.get('username')
        senha = request.POST.get('password')
        user = authenticate(request, username=usuario, password=senha)
        if user is not None:
            login(request, user)
            return redirect('imobiliaria:index')
        messages.error(request, 'Usuário ou senha inválidos.')
    return render(request, 'imobiliaria/login.html')


def logout_view(request):
    logout(request)
    return redirect('imobiliaria:login')


@login_required
def index(request):
    return render(request, 'imobiliaria/index.html')
