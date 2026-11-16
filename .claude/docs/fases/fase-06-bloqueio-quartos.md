# Fase 6 — Bloquear / desbloquear quarto (CU 8)

**Pré-requisito:** Fase 5 concluída
**Caso de uso:** CU 8 — Bloquear/Desbloquear Quartos (ator: Administrador)
**Commit:** `feat: permite bloquear e desbloquear quartos`

## Objetivo

Permitir que o administrador marque um quarto como indisponível (manutenção ou
outro motivo), impedindo novas reservas, e depois o libere.

## Ações

### models
Em `Quarto`:
- `motivo_bloqueio` — `CharField(blank=True)`
- método `bloquear(motivo)` — define `status = 'manutencao'` e guarda o motivo
- método `desbloquear()` — volta `status = 'disponivel'` e limpa o motivo

Migration da fase.

### views / urls
Restritas a administrador:
- `quarto_bloquear` — recebe o motivo por POST, chama `bloquear()`; recusa se o
  quarto estiver ocupado
- `quarto_desbloquear` — chama `desbloquear()`

urls: `quartos/<int:id>/bloquear/`, `quartos/<int:id>/desbloquear/`.

### templates
Reaproveita `quarto_lista.html` (ações no card). Se o motivo exigir tela própria,
usar `quarto_bloquear.html`.

### _partials
- `_quarto-card.html` — ganha o selo de bloqueado com o motivo e os botões de
  bloquear/desbloquear conforme o status

## Aceite

- Quarto bloqueado exibe o selo e o motivo na listagem.
- Quarto ocupado não pode ser bloqueado.
- Desbloqueio devolve o quarto para disponível.
- A seleção de quartos da criação de reserva (Fase 8) ignora quartos bloqueados.
