from django.urls import path
from ProjetoFinal import views


app_name = 'imobiliaria'

urlpatterns = [
    path('', views.index, name='index'),
    
]
