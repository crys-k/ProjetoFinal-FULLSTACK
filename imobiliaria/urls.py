from django.urls import path

from . import views

app_name = 'imobiliaria'

urlpatterns = [
    path('', views.lista_imoveis, name='inicio'),
    path('imovel/<slug:slug>/', views.detalhe_imovel, name='detalhe'),
]
