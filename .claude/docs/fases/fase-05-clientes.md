# Fase 5 — Gerenciar Clientes (CU 4)

**Pré-requisito:** Fase 2 concluída
**Caso de uso:** CU 4 — Gerenciar Clientes (ator: Funcionário)
**Commit:** `feat: implementa gerenciamento de clientes`

## Objetivo

Cadastro, busca e edição de clientes da imobiliária. Disponível para qualquer
funcionário autenticado (não é restrito ao administrador).

## Ações

### models
`Cliente`
- `nome` — `CharField`
- `cpf_cnpj` — `CharField(max_length=18, unique=True)`
- `telefone` — `CharField`
- `endereco` — `CharField`
- `data_cadastro` — `DateTimeField(auto_now_add=True)`
- `__str__` retornando nome e CPF/CNPJ
- `save()` normalizando nome com `title()`
- `Meta.ordering` por nome

Migration da fase.

### views / urls
- `cliente_lista` — busca por nome ou CPF/CNPJ lida de `request.GET`
- `cliente_novo`
- `cliente_editar`
- `cliente_detalhe` — dados do cliente e histórico de locações (o histórico
  entra na Fase 6)

urls: `clientes/`, `clientes/novo/`, `clientes/<int:id>/`,
`clientes/<int:id>/editar/`.

### forms
- `ClienteForm` — `ModelForm` com `clean_cpf_cnpj` validando formato e
  unicidade

### templates
- `cliente_lista.html`
- `cliente_form.html`
- `cliente_detalhe.html`

### _partials
- `_cliente-linha.html`
- `_busca-cliente.html` — formulário GET de busca, reaproveitado na criação
  de locação (Fase 6)

## Aceite

- Cadastro, busca e edição funcionando.
- CPF/CNPJ duplicado ou mal formatado é recusado com mensagem no campo.
- Busca encontra por parte do nome e por CPF/CNPJ.
