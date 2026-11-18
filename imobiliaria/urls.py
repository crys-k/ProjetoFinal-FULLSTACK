from django.urls import path

from . import views

app_name = 'imobiliaria'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('funcionarios/', views.funcionario_lista, name='funcionario_lista'),
    path('funcionarios/novo/', views.funcionario_novo, name='funcionario_novo'),
    path('funcionarios/<int:id>/editar/', views.funcionario_editar, name='funcionario_editar'),
    path('funcionarios/<int:id>/desativar/', views.funcionario_desativar, name='funcionario_desativar'),
    path('imoveis/', views.imovel_lista, name='imovel_lista'),
    path('imoveis/novo/', views.imovel_novo, name='imovel_novo'),
    path('imoveis/<int:id>/editar/', views.imovel_editar, name='imovel_editar'),
    path('imoveis/<int:id>/excluir/', views.imovel_excluir, name='imovel_excluir'),
    path('clientes/', views.cliente_lista, name='cliente_lista'),
    path('clientes/novo/', views.cliente_novo, name='cliente_novo'),
    path('clientes/<int:id>/', views.cliente_detalhe, name='cliente_detalhe'),
    path('clientes/<int:id>/editar/', views.cliente_editar, name='cliente_editar'),
    path('locacoes/', views.locacao_lista, name='locacao_lista'),
    path('locacoes/nova/', views.locacao_nova, name='locacao_nova'),
    path('locacoes/<int:id>/', views.locacao_detalhe, name='locacao_detalhe'),
    path('locacoes/<int:id>/finalizar/', views.locacao_finalizar, name='locacao_finalizar'),
    path('locacoes/<int:id>/cancelar/', views.locacao_cancelar, name='locacao_cancelar'),
]
