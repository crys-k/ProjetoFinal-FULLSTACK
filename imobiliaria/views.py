from decimal import Decimal, InvalidOperation

from django.shortcuts import get_object_or_404, render

from .models import Imovel


def lista_imoveis(request):
    imoveis = Imovel.objects.filter(ativo=True)
    finalidade = request.GET.get('finalidade', '')
    tipo = request.GET.get('tipo', '')
    cidade = request.GET.get('cidade', '').strip()
    preco_maximo = request.GET.get('preco_maximo', '').strip()

    if finalidade in Imovel.Finalidade.values:
        imoveis = imoveis.filter(finalidade=finalidade)
    if tipo in Imovel.Tipo.values:
        imoveis = imoveis.filter(tipo=tipo)
    if cidade:
        imoveis = imoveis.filter(cidade__icontains=cidade)
    if preco_maximo:
        try:
            valor = Decimal(preco_maximo)
            if valor.is_finite() and valor > 0:
                imoveis = imoveis.filter(preco__lte=valor)
        except InvalidOperation:
            pass

    return render(request, 'imobiliaria/inicio.html', {
        'imoveis': imoveis,
        'finalidades': Imovel.Finalidade.choices,
        'tipos': Imovel.Tipo.choices,
        'filtros': {
            'finalidade': finalidade,
            'tipo': tipo,
            'cidade': cidade,
            'preco_maximo': preco_maximo,
        },
    })


def detalhe_imovel(request, slug):
    imovel = get_object_or_404(Imovel, slug=slug, ativo=True)
    return render(request, 'imobiliaria/detalhe.html', {'imovel': imovel})
