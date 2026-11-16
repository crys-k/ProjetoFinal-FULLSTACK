# Fase 1 — Fundação de templates e home

**Pré-requisito:** Fase 0 concluída
**Caso de uso:** nenhum
**Commit:** `feat: adiciona base de templates, nav-bar e home`

## Objetivo

Montar o esqueleto visual do sistema antes de qualquer regra de negócio: template
base, navegação, área de mensagens e página inicial.

## Ações

### models
Nenhuma alteração.

### views / urls
- `index(request)` — renderiza a home do sistema.
- `urls.py`: `path('', views.index, name='index')`.

### templates
`imobiliaria/templates/imobiliaria/`
- `base.html` — `{% load static %}`, blocos `title` e `conteudo`, inclui os partials
  de navegação e mensagens.
- `index.html` — estende `base.html`, apresenta o sistema e os atalhos principais.

### _partials
`imobiliaria/templates/imobiliaria/_partials/`
- `_nav-bar.html` — navegação do sistema.
- `_messages.html` — exibe `django.contrib.messages`.

### settings
Em `ProjetoFinal/settings.py`:
- `LOGIN_URL`, `LOGIN_REDIRECT_URL`, `LOGOUT_REDIRECT_URL` (usados na Fase 2).
- `STATICFILES_DIRS` apontando para a pasta de estáticos do projeto, se houver CSS próprio.

## Aceite

- `/` abre renderizando `base.html` com a nav-bar.
- A área de mensagens aparece quando há mensagem na requisição.
- Nenhum link da nav-bar aponta para rota inexistente.
