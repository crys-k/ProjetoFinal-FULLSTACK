# Fase 0 — Green field (limpeza do app)

**Pré-requisito:** nenhum (primeira fase)
**Caso de uso:** nenhum
**Commit:** `chore: limpa app imobiliaria para iniciar o sistema de hotel`

## Objetivo

Zerar o app `imobiliaria` para iniciar o Sistema de Gerenciamento de Hotel sem
resíduos da versão anterior (imobiliária e model `Funcionario` experimental).

## Situação encontrada

- `imobiliaria/models.py` — model `Funcionario` e `SEXO_CHOICES` (código de teste).
- `imobiliaria/forms.py` — `funcionarioForm` (nome fora do padrão).
- `imobiliaria/views.py` — nenhuma view, mas imports quebrados; em especial
  `from django.db.models import queue`, que não existe e derruba a app.
- `imobiliaria/urls.py` — importa `from ProjetoFinal import views` (deveria ser
  `from . import views`) e registra `path('', views.index)` para uma view inexistente.
- `imobiliaria/migrations/0001_initial.py` — cria um model `Imovel` que já não existe.
- `db.sqlite3` — dessincronizado: contém as tabelas `imobiliaria_funcionario` e
  `imobiliaria_cliente` e registra a migration `imobiliaria.0002_cliente`, que não
  existe na pasta de migrations. A base não é recuperável por migration.

## Ações

1. `imobiliaria/models.py` — remover `Funcionario` e `SEXO_CHOICES`, deixando apenas:
   ```python
   from django.db import models
   ```
2. `imobiliaria/forms.py` — remover `funcionarioForm`, deixando apenas:
   ```python
   from django import forms
   ```
3. `imobiliaria/views.py` — remover todos os imports quebrados, deixando apenas:
   ```python
   from django.shortcuts import render
   ```
4. `imobiliaria/urls.py` — corrigir o import e zerar as rotas:
   ```python
   from django.urls import path

   from . import views

   app_name = 'imobiliaria'

   urlpatterns = [
   ]
   ```
5. `imobiliaria/admin.py` — manter sem registros.
6. Apagar `imobiliaria/migrations/0001_initial.py`, mantendo `__init__.py`.
7. Apagar `db.sqlite3`.
8. Recriar a base limpa (executado pelo programador):
   ```
   python manage.py makemigrations
   python manage.py migrate
   python manage.py createsuperuser
   ```

## Aceite

- `python manage.py check` não acusa erros e o servidor sobe.
- Nenhuma ocorrência de `Funcionario`, `SEXO_CHOICES` ou `Imovel` no app.
- `imobiliaria/migrations/` só contém `__init__.py`.
- Base recriada contendo apenas as tabelas do Django e o superusuário.
