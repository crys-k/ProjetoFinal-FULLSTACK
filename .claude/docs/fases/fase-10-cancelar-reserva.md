# Fase 10 — Cancelar reserva (CU 7)

**Pré-requisito:** Fase 9 concluída
**Caso de uso:** CU 7 — Cancelar Reserva (ator: Funcionário)
**Commit:** `feat: permite cancelar reservas`

## Objetivo

Cancelar uma reserva antes do check-in, liberando o quarto para novas reservas.

## Ações

### models
Em `Reserva`:
- `cancelada_em` — `DateTimeField(null=True, blank=True)`
- `motivo_cancelamento` — `CharField(blank=True)`
- método `cancelar(motivo)` — só se `status == 'pendente'`; muda para `cancelada`,
  registra data e motivo e devolve o quarto para `disponivel`

Migration da fase.

### views / urls
- `reserva_cancelar` — `if request.method == 'POST'` efetiva o cancelamento;
  no GET mostra a confirmação. Recusa com mensagem quando o status não permite.

urls: `reservas/<int:id>/cancelar/`.

### templates
- `reserva_confirmar_cancelamento.html` — resumo da reserva e campo de motivo

### _partials
- reaproveita `_resumo-reserva.html`
- `_reserva-linha.html` — exibe o status `cancelada` e esconde a ação de cancelar
  para reservas que não são pendentes

## Aceite

- Reserva pendente é cancelada e o quarto volta a disponível.
- Reserva `em_andamento`, `finalizada` ou já `cancelada` não pode ser cancelada.
- O motivo do cancelamento aparece no detalhe da reserva.
