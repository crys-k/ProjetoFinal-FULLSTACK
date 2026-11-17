# Fase 8 — Bloquear / Desbloquear Imóvel (CU 9)

**Pré-requisito:** Fase 4 concluída
**Caso de uso:** CU 9 — Bloquear/Desbloquear Imóvel (ator: Administrador)
**Commit:** `feat: permite bloquear e desbloquear imoveis`

## Objetivo

Permitir que o administrador marque um imóvel como indisponível (manutenção
ou outro motivo), impedindo novas locações, e depois o libere.

## Ações

### models
Em `Imovel`:
- `motivo_bloqueio` — `CharField(blank=True)`
- método `bloquear(motivo)` — define `status = 'indisponivel'` e guarda o
  motivo; só se não houver `Locacao` com `status='ativa'` para o imóvel
- método `desbloquear()` — volta `status = 'disponivel'` e limpa o motivo

Migration da fase.

### views / urls
Restritas a administrador (`if not request.user.is_staff`):
- `imovel_bloquear` — recebe o motivo por POST, chama `bloquear()`; recusa se
  o imóvel estiver alugado
- `imovel_desbloquear` — chama `desbloquear()`

urls: `imoveis/<int:id>/bloquear/`, `imoveis/<int:id>/desbloquear/`.

### templates
Reaproveita `imovel_lista.html` (ações no card).

### _partials
- `_imovel-card.html` — ganha o selo de bloqueado com o motivo e os botões de
  bloquear/desbloquear conforme o status

## Aceite

- Imóvel bloqueado exibe o selo e o motivo na listagem.
- Imóvel alugado não pode ser bloqueado.
- Desbloqueio devolve o imóvel para disponível.
- A seleção de imóveis da criação de locação (Fase 6) ignora imóveis
  bloqueados.
- Funcionário comum (`is_staff = False`) não acessa essas ações.
