from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import FuncionarioForm, UsuarioForm
from .models import Funcionario


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


@login_required
def funcionario_lista(request):
    if not request.user.is_staff:
        messages.error(request, 'Acesso restrito ao administrador.')
        return redirect('imobiliaria:index')
    funcionarios = Funcionario.objects.all()
    return render(request, 'imobiliaria/funcionario_lista.html', {'funcionarios': funcionarios})


@login_required
def funcionario_novo(request):
    if not request.user.is_staff:
        messages.error(request, 'Acesso restrito ao administrador.')
        return redirect('imobiliaria:index')
    if request.method == 'POST':
        usuario_form = UsuarioForm(request.POST)
        funcionario_form = FuncionarioForm(request.POST)
        if usuario_form.is_valid() and funcionario_form.is_valid():
            usuario = usuario_form.save()
            funcionario = funcionario_form.save(commit=False)
            funcionario.usuario = usuario
            funcionario.save()
            messages.success(request, 'Funcionário cadastrado com sucesso.')
            return redirect('imobiliaria:funcionario_lista')
    else:
        usuario_form = UsuarioForm()
        funcionario_form = FuncionarioForm()
    contexto = {'usuario_form': usuario_form, 'funcionario_form': funcionario_form}
    return render(request, 'imobiliaria/funcionario_form.html', contexto)


@login_required
def funcionario_editar(request, id):
    if not request.user.is_staff:
        messages.error(request, 'Acesso restrito ao administrador.')
        return redirect('imobiliaria:index')
    funcionario = get_object_or_404(Funcionario, pk=id)
    if request.method == 'POST':
        funcionario_form = FuncionarioForm(request.POST, instance=funcionario)
        if funcionario_form.is_valid():
            funcionario_form.save()
            messages.success(request, 'Funcionário atualizado com sucesso.')
            return redirect('imobiliaria:funcionario_lista')
    else:
        funcionario_form = FuncionarioForm(instance=funcionario)
    contexto = {'funcionario_form': funcionario_form, 'funcionario': funcionario}
    return render(request, 'imobiliaria/funcionario_form.html', contexto)


@login_required
def funcionario_desativar(request, id):
    if not request.user.is_staff:
        messages.error(request, 'Acesso restrito ao administrador.')
        return redirect('imobiliaria:index')
    funcionario = get_object_or_404(Funcionario, pk=id)
    if request.method == 'POST':
        funcionario.ativo = False
        funcionario.usuario.is_active = False
        funcionario.usuario.save()
        funcionario.save()
        messages.success(request, 'Funcionário desativado com sucesso.')
    return redirect('imobiliaria:funcionario_lista')
