# Fase 3 — Gerir Funcionários (CU 1)

**Pré-requisito:** Fase 2 concluída
**Caso de uso:** CU 1 — Gerir Funcionários (ator: Administrador)
**Commit:** `feat: implementa gerenciamento de funcionarios`

## Objetivo

Permitir que o administrador cadastre, edite e desative funcionários, incluindo as
credenciais de acesso ao sistema.

## Ações

### models
`Funcionario`
- `usuario` — `OneToOneField(User, on_delete=models.PROTECT)`
- `cargo` — `CharField` com `choices` (ex.: corretor, gerente, administração)
- `telefone` — `CharField`
- `ativo` — `BooleanField(default=True)`
- `data_cadastro` — `DateTimeField(auto_now_add=True)`
- `__str__` retornando o nome do funcionário
- `Meta.ordering` por nome

Migration da fase: `makemigrations imobiliaria`.

### views / urls
Todas restritas a administrador (`if not request.user.is_staff`):
- `funcionario_lista` — lista cadastrados, com indicação de inativo
- `funcionario_novo` — cria `User` (via `UserCreationForm`) + `Funcionario`
- `funcionario_editar` — `get_object_or_404`, atualiza dados cadastrais
- `funcionario_desativar` — marca `ativo = False` e `usuario.is_active = False`

urls: `funcionarios/`, `funcionarios/novo/`, `funcionarios/<int:id>/editar/`,
`funcionarios/<int:id>/desativar/`.

### forms
- `FuncionarioForm` — `ModelForm` dos campos de `Funcionario`
- `UserCreationForm` (do Django) para usuário e senha no cadastro

### templates
- `funcionario_lista.html`
- `funcionario_form.html`

### _partials
- `_funcionario-linha.html` — linha da tabela com dados e ações

## Aceite

- Administrador cadastra funcionário com credenciais e ele consegue logar.
- Edição atualiza os dados cadastrais.
- Funcionário desativado não consegue mais logar.
- Funcionário comum (`is_staff = False`) não acessa nenhuma dessas telas.
