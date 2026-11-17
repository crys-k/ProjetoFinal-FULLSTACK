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
]
