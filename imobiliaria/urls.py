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
]
