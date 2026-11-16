# Fase 4 — Tipos de quarto e tarifas (CU 11)

**Pré-requisito:** Fase 2 concluída (Fase 3 não é bloqueante)
**Caso de uso:** CU 11 — Configurar Tipos de Quartos e Tarifas (ator: Administrador)
**Commit:** `feat: implementa tipos de quarto e tarifas`

## Objetivo

Cadastrar os tipos de quarto (simples, duplo, suíte) e suas tarifas. Vem antes da
Fase 5 porque `Quarto` referencia `TipoQuarto` por chave estrangeira.

## Ações

### models
`TipoQuarto`
- `nome` — `CharField(unique=True)`
- `capacidade` — `PositiveSmallIntegerField`
- `valor_diaria` — `DecimalField(max_digits=10, decimal_places=2)`
- `descricao` — `TextField(blank=True)`
- `__str__` retornando o nome
- `Meta.ordering` por nome

Migration da fase.

### views / urls
Restritas a administrador:
- `tipo_quarto_lista` — tabela de tipos com as tarifas atuais
- `tipo_quarto_novo`
- `tipo_quarto_editar` — ajuste de tarifa e demais dados

urls: `tipos-quarto/`, `tipos-quarto/novo/`, `tipos-quarto/<int:id>/editar/`.

### forms
- `TipoQuartoForm` — `ModelForm`, com `clean_valor_diaria` recusando valor menor
  ou igual a zero

### templates
- `tipo_quarto_lista.html`
- `tipo_quarto_form.html`

### _partials
- `_tabela-tarifas.html` — tabela de tipos e valores, reaproveitável no relatório

## Aceite

- Administrador cria e edita tipos de quarto.
- Tarifa zerada ou negativa é recusada pelo form.
- Nome de tipo duplicado é recusado.
