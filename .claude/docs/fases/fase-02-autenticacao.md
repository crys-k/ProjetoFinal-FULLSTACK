# Fase 2 — Autenticação (acesso restrito a funcionários)

**Pré-requisito:** Fase 1 concluída
**Caso de uso:** nenhum (requisito do briefing: sistema usado somente por funcionários)
**Commit:** `feat: implementa login e logout de funcionarios`

## Objetivo

Restringir o sistema a usuários autenticados e preparar a distinção entre
Funcionário e Administrador usada nas fases seguintes.

## Ações

### models
Nenhuma alteração (usa o `User` do `django.contrib.auth`).

### views / urls
- `login_view(request)` — `if request.method == 'POST'`, valida com
  `authenticate()` e entra com `login()`; em erro, usa `messages.error`.
- `logout_view(request)` — `logout()` e redirect para o login.
- `index` passa a usar `@login_required`.
- urls: `login`, `logout`.

Não usar `LoginView` / `LogoutView` (são class-based). Autenticação feita em view
de função com `authenticate` e `login`, conforme `CLAUDE.md`.

### Perfil de administrador
Administrador = `request.user.is_staff`. A verificação é feita com `if` no começo
da view, sem `@permission_required`:

```python
@login_required
def alguma_view_de_admin(request):
    if not request.user.is_staff:
        messages.error(request, 'Acesso restrito ao administrador.')
        return redirect('imobiliaria:index')
    ...
```

### templates
- `login.html` — formulário de acesso (`{% csrf_token %}`), fora do `base.html`
  ou com um bloco sem nav-bar.

### _partials
- `_nav-bar.html` — mostra o usuário logado, o link "Sair" e esconde os itens de
  administrador quando `not user.is_staff`.

## Aceite

- Usuário anônimo acessando `/` é redirecionado para o login.
- Login com credenciais válidas leva à home; credenciais inválidas exibem mensagem.
- Logout encerra a sessão e volta ao login.
