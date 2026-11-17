# Fase 7 — Finalizar e Cancelar Locação (CU 6 e 7)

**Pré-requisito:** Fase 6 concluída
**Casos de uso:** CU 6 — Finalizar Locação; CU 7 — Cancelar Locação Antes da
Entrada (ator: Funcionário)
**Commit:** `feat: implementa finalizacao e cancelamento de locacoes`

## Objetivo

Encerrar um contrato de aluguel em andamento, ou cancelar uma locação antes do
cliente ocupar o imóvel, liberando o imóvel para novas locações em ambos os
casos.

## Ações

### models
Em `Locacao`:
- `motivo_cancelamento` — `CharField(blank=True)`
- método `finalizar()` — só se `status == 'ativa'`; grava
  `data_fim_real = timezone.now().date()`, muda para `finalizada` e devolve o
  imóvel para `disponivel`
- método `cancelar(motivo)` — só se `status == 'ativa'` e `data_inicio` ainda
  não chegou (`data_inicio > timezone.now().date()`); muda para `cancelada`,
  registra o motivo e devolve o imóvel para `disponivel`

Migration da fase.

### views / urls
- `locacao_finalizar` — `if request.method == 'POST'` efetiva a finalização;
  no GET mostra a confirmação. Recusa com mensagem se o status não permitir.
- `locacao_cancelar` — idem, chamando `cancelar()`; recusa com mensagem se a
  locação já tiver iniciado ou não estiver `ativa`.

urls: `locacoes/<int:id>/finalizar/`, `locacoes/<int:id>/cancelar/`.

### templates
- `locacao_confirmar_finalizacao.html`
- `locacao_confirmar_cancelamento.html` — resumo da locação e campo de motivo

### _partials
- `_locacao-linha.html` — ganha os botões de finalizar/cancelar conforme o
  status e a data de início

## Aceite

- Locação `ativa` já iniciada pode ser finalizada; o imóvel volta a
  `disponivel`.
- Locação `ativa` ainda não iniciada pode ser cancelada; o imóvel volta a
  `disponivel`.
- Locação `ativa` já iniciada não pode ser cancelada (só finalizada).
- Locação `finalizada` ou `cancelada` não aceita nenhuma das duas ações.
- O motivo do cancelamento aparece no detalhe da locação.
