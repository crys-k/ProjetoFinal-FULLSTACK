# Fase 7 — Gerenciar Clientes (CU 2)

**Pré-requisito:** Fase 2 concluída
**Caso de uso:** CU 2 — Gerenciar Clientes (ator: Funcionário)
**Commit:** `feat: implementa gerenciamento de clientes`

## Objetivo

Cadastro, busca e edição de clientes do hotel. Disponível para qualquer
funcionário autenticado (não é restrito ao administrador).

## Ações

### models
`Cliente`
- `nome` — `CharField`
- `cpf` — `CharField(max_length=14, unique=True)`
- `telefone` — `CharField`
- `email` — `EmailField(blank=True)`
- `endereco` — `CharField`
- `cidade` — `CharField`
- `data_cadastro` — `DateTimeField(auto_now_add=True)`
- `__str__` retornando nome e CPF
- `save()` normalizando nome com `title()` e email com `lower()`
- `Meta.ordering` por nome

Migration da fase.

### views / urls
- `cliente_lista` — busca por nome ou CPF lida de `request.GET`
- `cliente_novo`
- `cliente_editar`
- `cliente_detalhe` — dados do cliente e histórico de reservas (o histórico entra
  na Fase 8)

urls: `clientes/`, `clientes/novo/`, `clientes/<int:id>/`,
`clientes/<int:id>/editar/`.

### forms
- `ClienteForm` — `ModelForm` com `clean_cpf` validando formato e unicidade

### templates
- `cliente_lista.html`
- `cliente_form.html`
- `cliente_detalhe.html`

### _partials
- `_cliente-linha.html`
- `_busca-cliente.html` — formulário GET de busca, reaproveitado na criação de reserva

## Aceite

- Cadastro, busca e edição funcionando.
- CPF duplicado ou mal formatado é recusado com mensagem no campo.
- Busca encontra por parte do nome e por CPF.
