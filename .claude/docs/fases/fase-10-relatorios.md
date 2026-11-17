# Fase 10 — Relatórios de Locações (CU 8)

**Pré-requisito:** Fase 6 concluída
**Caso de uso:** CU 8 — Gerar Relatórios de Locações (ator: Administrador)
**Commit:** `feat: implementa relatorio de locacoes`

## Objetivo

Relatório de locações com filtros por período, tipo de imóvel e status da
locação, mais os totais do recorte.

## Ações

### models
Nenhuma alteração.

### views / urls
- `relatorio_locacoes` — restrita a administrador. Lê os filtros de
  `request.GET` e monta o queryset com `filter()` encadeado apenas para os
  filtros preenchidos:
  - período: `data_inicio__gte` e `data_fim_prevista__lte`
  - status, tipo de imóvel (`imovel__tipo`)
  - totais com `count()` e `aggregate(Sum('imovel__valor_aluguel'))`

urls: `relatorios/locacoes/`.

### forms
Opcional: `RelatorioLocacoesForm` (`forms.Form`) para os campos de filtro,
com `required=False` em todos.

### templates
- `relatorio_locacoes.html`

### _partials
- `_filtro-relatorio.html` — formulário GET dos filtros
- `_tabela-relatorio.html` — linhas do relatório e rodapé com totais

## Aceite

- Sem filtros, lista todas as locações.
- Cada filtro reduz corretamente o resultado e os filtros se combinam.
- Totais (quantidade de locações e soma do valor de aluguel) correspondem às
  linhas exibidas.
- Funcionário não administrador não acessa a tela.
