# Fase 5 — Gerenciar Quartos (CU 1)

**Pré-requisito:** Fase 4 concluída
**Caso de uso:** CU 1 — Gerenciar Quartos (ator: Administrador)
**Commit:** `feat: implementa gerenciamento de quartos`

## Objetivo

CRUD de quartos do hotel, com tipo, capacidade herdada do tipo e status de
disponibilidade.

## Ações

### models
`Quarto`
- `numero` — `CharField(unique=True)`
- `tipo` — `ForeignKey(TipoQuarto, on_delete=models.PROTECT)`
- `andar` — `PositiveSmallIntegerField`
- `status` — `CharField` com `choices`:
  `disponivel` / `ocupado` / `manutencao`
- `__str__` retornando `Quarto <numero>`
- `Meta.ordering` por número

Migration da fase.

### views / urls
Restritas a administrador:
- `quarto_lista` — com filtro por status e por tipo, lido de `request.GET`
- `quarto_novo`
- `quarto_editar`
- `quarto_remover` — só permite se o quarto não estiver ocupado; confirmação em
  página própria antes do `delete()`

urls: `quartos/`, `quartos/novo/`, `quartos/<int:id>/editar/`,
`quartos/<int:id>/remover/`.

### forms
- `QuartoForm` — `ModelForm`

### templates
- `quarto_lista.html`
- `quarto_form.html`
- `quarto_confirmar_remocao.html`

### _partials
- `_quarto-card.html` — número, tipo, status e ações
- `_filtro-quartos.html` — formulário GET de filtro

## Aceite

- CRUD completo funcionando.
- Número de quarto duplicado é recusado.
- Remoção de quarto ocupado é bloqueada com mensagem.
- Filtros por status e tipo retornam o subconjunto correto.
