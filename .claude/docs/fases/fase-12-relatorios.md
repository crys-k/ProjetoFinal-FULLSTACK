# Fase 12 — Relatórios de reservas (CU 9)

**Pré-requisito:** Fase 8 concluída
**Caso de uso:** CU 9 — Gerar Relatórios de Reservas (ator: Administrador)
**Commit:** `feat: implementa relatorio de reservas`

## Objetivo

Relatório de reservas com filtros por período, cliente, status e tipo de quarto,
mais os totais do recorte.

## Ações

### models
Nenhuma alteração.

### views / urls
- `relatorio_reservas` — restrita a administrador. Lê os filtros de `request.GET`
  e monta o queryset com `filter()` encadeado apenas para os filtros preenchidos:
  - período: `data_entrada__gte` e `data_saida__lte`
  - cliente, status, tipo de quarto (`quarto__tipo`)
  - totais com `count()` e `aggregate(Sum('valor_total'))`

urls: `relatorios/reservas/`.

### forms
Opcional: `RelatorioReservasForm` (`forms.Form`) para os campos de filtro, com
`required=False` em todos.

### templates
- `relatorio_reservas.html`

### _partials
- `_filtro-relatorio.html` — formulário GET dos filtros
- `_tabela-relatorio.html` — linhas do relatório e rodapé com totais

## Aceite

- Sem filtros, lista todas as reservas.
- Cada filtro reduz corretamente o resultado e os filtros se combinam.
- Totais (quantidade de reservas e soma de `valor_total`) correspondem às linhas
  exibidas.
- Funcionário não administrador não acessa a tela.
