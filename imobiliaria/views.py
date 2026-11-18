from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ClienteForm, FuncionarioForm, ImovelForm, LocacaoForm, OcorrenciaForm, UsuarioForm
from .models import Cliente, Funcionario, Imovel, Locacao, Ocorrencia


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


@login_required
def imovel_lista(request):
    imoveis = Imovel.objects.filter(ativo=True)
    status = request.GET.get('status')
    tipo = request.GET.get('tipo')
    if status:
        imoveis = imoveis.filter(status=status)
    if tipo:
        imoveis = imoveis.filter(tipo=tipo)
    contexto = {
        'imoveis': imoveis,
        'status_opcoes': Imovel.STATUS_CHOICES,
        'tipo_opcoes': Imovel.TIPO_CHOICES,
        'status_selecionado': status,
        'tipo_selecionado': tipo,
    }
    return render(request, 'imobiliaria/imovel_lista.html', contexto)


@login_required
def imovel_novo(request):
    if request.method == 'POST':
        form = ImovelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Imóvel cadastrado com sucesso.')
            return redirect('imobiliaria:imovel_lista')
    else:
        form = ImovelForm()
    return render(request, 'imobiliaria/imovel_form.html', {'form': form})


@login_required
def imovel_editar(request, id):
    imovel = get_object_or_404(Imovel, pk=id)
    if request.method == 'POST':
        form = ImovelForm(request.POST, instance=imovel)
        if form.is_valid():
            form.save()
            messages.success(request, 'Imóvel atualizado com sucesso.')
            return redirect('imobiliaria:imovel_lista')
    else:
        form = ImovelForm(instance=imovel)
    return render(request, 'imobiliaria/imovel_form.html', {'form': form, 'imovel': imovel})


@login_required
def imovel_excluir(request, id):
    imovel = get_object_or_404(Imovel, pk=id)
    if request.method == 'POST':
        # TODO (Fase 6): recusar e avisar via messages.error se houver Locacao ativa.
        imovel.ativo = False
        imovel.save()
        messages.success(request, 'Imóvel excluído com sucesso.')
    return redirect('imobiliaria:imovel_lista')


@login_required
def imovel_bloquear(request, id):
    if not request.user.is_staff:
        messages.error(request, 'Acesso restrito ao administrador.')
        return redirect('imobiliaria:index')
    imovel = get_object_or_404(Imovel, pk=id)
    if request.method == 'POST':
        if not imovel.pode_bloquear:
            messages.error(request, 'Imóvel alugado não pode ser bloqueado.')
        else:
            motivo = request.POST.get('motivo_bloqueio', '')
            imovel.bloquear(motivo)
            messages.success(request, 'Imóvel bloqueado com sucesso.')
    return redirect('imobiliaria:imovel_lista')


@login_required
def imovel_desbloquear(request, id):
    if not request.user.is_staff:
        messages.error(request, 'Acesso restrito ao administrador.')
        return redirect('imobiliaria:index')
    imovel = get_object_or_404(Imovel, pk=id)
    if request.method == 'POST':
        imovel.desbloquear()
        messages.success(request, 'Imóvel desbloqueado com sucesso.')
    return redirect('imobiliaria:imovel_lista')


@login_required
def cliente_lista(request):
    clientes = Cliente.objects.all()
    busca = request.GET.get('busca')
    if busca:
        clientes = clientes.filter(Q(nome__icontains=busca) | Q(cpf_cnpj__icontains=busca))
    contexto = {'clientes': clientes, 'busca': busca}
    return render(request, 'imobiliaria/cliente_lista.html', contexto)


@login_required
def cliente_novo(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente cadastrado com sucesso.')
            return redirect('imobiliaria:cliente_lista')
    else:
        form = ClienteForm()
    return render(request, 'imobiliaria/cliente_form.html', {'form': form})


@login_required
def cliente_editar(request, id):
    cliente = get_object_or_404(Cliente, pk=id)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente atualizado com sucesso.')
            return redirect('imobiliaria:cliente_lista')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'imobiliaria/cliente_form.html', {'form': form, 'cliente': cliente})


@login_required
def cliente_detalhe(request, id):
    cliente = get_object_or_404(Cliente, pk=id)
    locacoes = Locacao.objects.filter(cliente=cliente)
    return render(request, 'imobiliaria/cliente_detalhe.html', {'cliente': cliente, 'locacoes': locacoes})


@login_required
def locacao_lista(request):
    locacoes = Locacao.objects.all()
    status = request.GET.get('status')
    if status:
        locacoes = locacoes.filter(status=status)
    contexto = {
        'locacoes': locacoes,
        'status_opcoes': Locacao.STATUS_CHOICES,
        'status_selecionado': status,
    }
    return render(request, 'imobiliaria/locacao_lista.html', contexto)


@login_required
def locacao_nova(request):
    busca = request.GET.get('busca')
    imoveis_disponiveis = Imovel.objects.filter(status='disponivel', ativo=True)
    if request.method == 'POST':
        form = LocacaoForm(request.POST)
        if form.is_valid():
            locacao = form.save(commit=False)
            locacao.funcionario = Funcionario.objects.filter(usuario=request.user).first()
            locacao.save()
            locacao.imovel.status = 'alugado'
            locacao.imovel.save()
            messages.success(request, 'Locação criada com sucesso.')
            return redirect('imobiliaria:locacao_detalhe', id=locacao.id)
    else:
        form = LocacaoForm(busca=busca)
    contexto = {'form': form, 'busca': busca, 'imoveis_disponiveis': imoveis_disponiveis}
    return render(request, 'imobiliaria/locacao_form.html', contexto)


@login_required
def locacao_detalhe(request, id):
    locacao = get_object_or_404(Locacao, pk=id)
    return render(request, 'imobiliaria/locacao_detalhe.html', {'locacao': locacao})


@login_required
def locacao_finalizar(request, id):
    locacao = get_object_or_404(Locacao, pk=id)
    if not locacao.pode_finalizar:
        messages.error(request, 'Esta locação não pode ser finalizada.')
        return redirect('imobiliaria:locacao_detalhe', id=locacao.id)
    if request.method == 'POST':
        locacao.finalizar()
        messages.success(request, 'Locação finalizada com sucesso.')
        return redirect('imobiliaria:locacao_detalhe', id=locacao.id)
    return render(request, 'imobiliaria/locacao_confirmar_finalizacao.html', {'locacao': locacao})


@login_required
def locacao_cancelar(request, id):
    locacao = get_object_or_404(Locacao, pk=id)
    if not locacao.pode_cancelar:
        messages.error(request, 'Esta locação não pode ser cancelada.')
        return redirect('imobiliaria:locacao_detalhe', id=locacao.id)
    if request.method == 'POST':
        motivo = request.POST.get('motivo_cancelamento', '')
        locacao.cancelar(motivo)
        messages.success(request, 'Locação cancelada com sucesso.')
        return redirect('imobiliaria:locacao_detalhe', id=locacao.id)
    return render(request, 'imobiliaria/locacao_confirmar_cancelamento.html', {'locacao': locacao})


@login_required
def ocorrencia_lista(request):
    ocorrencias = Ocorrencia.objects.all()
    imovel_id = request.GET.get('imovel')
    status = request.GET.get('status')
    if imovel_id:
        ocorrencias = ocorrencias.filter(imovel_id=imovel_id)
    if status == 'pendente':
        ocorrencias = ocorrencias.filter(resolvida=False)
    elif status == 'resolvida':
        ocorrencias = ocorrencias.filter(resolvida=True)
    contexto = {
        'ocorrencias': ocorrencias,
        'imoveis': Imovel.objects.filter(ativo=True),
        'imovel_selecionado': imovel_id,
        'status_selecionado': status,
    }
    return render(request, 'imobiliaria/ocorrencia_lista.html', contexto)


@login_required
def ocorrencia_nova(request):
    if request.method == 'POST':
        form = OcorrenciaForm(request.POST)
        if form.is_valid():
            ocorrencia = form.save(commit=False)
            ocorrencia.funcionario = Funcionario.objects.filter(usuario=request.user).first()
            ocorrencia.save()
            messages.success(request, 'Ocorrência registrada com sucesso.')
            return redirect('imobiliaria:ocorrencia_lista')
    else:
        form = OcorrenciaForm()
    return render(request, 'imobiliaria/ocorrencia_form.html', {'form': form})


@login_required
def ocorrencia_resolver(request, id):
    ocorrencia = get_object_or_404(Ocorrencia, pk=id)
    if request.method == 'POST':
        ocorrencia.resolver()
        messages.success(request, 'Ocorrência marcada como resolvida.')
    return redirect('imobiliaria:ocorrencia_lista')
