# Fase 9 — Check-in e Check-out (CU 5 e 6)

**Pré-requisito:** Fase 8 concluída
**Casos de uso:** CU 5 — Realizar Check-in; CU 6 — Realizar Check-out (ator: Funcionário)
**Commit:** `feat: implementa check-in e check-out de reservas`

## Objetivo

Registrar a entrada e a saída do cliente, mantendo o status da reserva e a
disponibilidade do quarto sincronizados.

## Ações

### models
Em `Reserva`:
- `check_in` — `DateTimeField(null=True, blank=True)`
- `check_out` — `DateTimeField(null=True, blank=True)`
- método `realizar_check_in()` — só se `status == 'pendente'`; grava `check_in`
  com `timezone.now()`, muda para `em_andamento` e marca o quarto como `ocupado`
- método `realizar_check_out()` — só se `status == 'em_andamento'`; grava
  `check_out`, muda para `finalizada` e devolve o quarto para `disponivel`

Migration da fase.

### views / urls
- `reserva_check_in` — busca a reserva, confirma os dados e chama
  `realizar_check_in()`; recusa com mensagem se o status não permitir
- `reserva_check_out` — idem para `realizar_check_out()`
- `check_in_lista` (opcional) — reservas pendentes com entrada prevista para hoje

urls: `reservas/<int:id>/check-in/`, `reservas/<int:id>/check-out/`.

### templates
- `check_in.html` — confirmação dos dados antes de efetivar
- `check_out.html` — confirmação e verificação do estado do quarto

### _partials
- `_resumo-reserva.html` — cliente, quarto, período e valor; reaproveitado nas
  duas telas e no detalhe da reserva

## Aceite

- Check-in muda a reserva para `em_andamento` e o quarto para `ocupado`.
- Check-out muda a reserva para `finalizada` e libera o quarto.
- Check-in em reserva cancelada ou já em andamento é recusado com mensagem.
- Check-out em reserva que não passou pelo check-in é recusado.
- Quarto liberado volta a aparecer como disponível para novas reservas.
