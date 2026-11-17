# Fase 4 — Cadastrar / Editar / Remover Imóvel (CU 2 e 3)

**Pré-requisito:** Fase 2 concluída (Fase 3 não é bloqueante)
**Casos de uso:** CU 2 — Cadastrar Imóvel; CU 3 — Editar/Remover Imóvel (ator: Funcionário)
**Commit:** `feat: implementa cadastro, edicao e remocao de imoveis`

## Objetivo

CRUD de imóveis disponíveis para locação: endereço, tipo, características e
status de disponibilidade.

## Ações

### models
`Imovel`
- `endereco` — `CharField`
- `tipo` — `CharField` com `choices`: `apartamento` / `casa` / `sala_comercial`
- `quartos` — `PositiveSmallIntegerField`
- `metragem` — `DecimalField(max_digits=6, decimal_places=2)`
- `valor_aluguel` — `DecimalField(max_digits=10, decimal_places=2)`
- `foto` — `CharField(blank=True)` guardando o nome do arquivo em
  `imobiliaria/static/imobiliaria/img/imoveis/` (asset fixo do projeto, sem
  upload de usuário — nenhuma dependência nova é necessária)
- `status` — `CharField` com `choices`: `disponivel` / `alugado` / `indisponivel`
  (default `disponivel`)
- `ativo` — `BooleanField(default=True)`
- `criado_em` — `DateTimeField(auto_now_add=True)`
- `__str__` retornando endereço e tipo
- `Meta.ordering` por `-criado_em`

Migration da fase.

### views / urls
- `imovel_lista` — filtro por status e tipo lido de `request.GET`
- `imovel_novo`
- `imovel_editar`
- `imovel_excluir` — só permite remover se não houver `Locacao` com
  `status='ativa'` apontando para o imóvel; caso contrário, `messages.error`
  e mantém o registro

urls: `imoveis/`, `imoveis/novo/`, `imoveis/<int:id>/editar/`,
`imoveis/<int:id>/excluir/`.

### forms
- `ImovelForm` — `ModelForm` com `clean_valor_aluguel` recusando valor menor
  ou igual a zero

### templates
- `imovel_lista.html`
- `imovel_form.html`

### _partials
- `_imovel-card.html` — endereço, tipo, características, status e ações;
  reaproveitado nas Fases 6, 8, 9 e 11

## Aceite

- CRUD completo funcionando.
- Valor de aluguel zerado ou negativo é recusado pelo form.
- Remoção de imóvel com locação ativa é bloqueada com mensagem.
- Filtros por status e tipo retornam o subconjunto correto.
