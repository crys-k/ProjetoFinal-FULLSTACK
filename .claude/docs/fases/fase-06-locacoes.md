# Fase 6 — Criar Locação (CU 5)

**Pré-requisito:** Fases 4 e 5 concluídas
**Caso de uso:** CU 5 — Criar Locação (ator: Funcionário)
**Commit:** `feat: implementa criacao e listagem de locacoes`

## Objetivo

Núcleo do sistema: registrar a locação de um imóvel disponível para um
cliente, por um período definido.

## Ações

### models
`Locacao`
- `cliente` — `ForeignKey(Cliente, on_delete=models.PROTECT)`
- `imovel` — `ForeignKey(Imovel, on_delete=models.PROTECT)`
- `funcionario` — `ForeignKey(Funcionario, on_delete=models.PROTECT, null=True)`
- `data_inicio` — `DateField`
- `data_fim_prevista` — `DateField`
- `data_fim_real` — `DateField(null=True, blank=True)`
- `status` — `CharField` com `choices`: `ativa` / `finalizada` / `cancelada`
- `criada_em` — `DateTimeField(auto_now_add=True)`
- `__str__` com cliente, imóvel e período
- `Meta.ordering` por `-criada_em`

Migration da fase.

### views / urls
- `locacao_lista` — filtro por status lido de `request.GET`
- `locacao_nova` — seleciona cliente (busca) e imóvel com `status='disponivel'`,
  define `data_inicio`/`data_fim_prevista` e, ao confirmar, grava a `Locacao`
  com `status='ativa'` e atualiza `Imovel.status = 'alugado'`
- `locacao_detalhe` — dados completos da locação

urls: `locacoes/`, `locacoes/nova/`, `locacoes/<int:id>/`.

### forms
`LocacaoForm` — `ModelForm` com:
- `clean()` validando `data_fim_prevista > data_inicio`
- queryset de `imovel` restrito a `status='disponivel'`

### templates
- `locacao_lista.html`
- `locacao_form.html`
- `locacao_detalhe.html`

### _partials
- `_locacao-linha.html`
- reaproveitar `_imovel-card.html` (Fase 4) e `_busca-cliente.html` (Fase 5)

Também incluir o histórico de locações em `cliente_detalhe.html`.

## Aceite

- Locação é criada apenas para imóvel disponível.
- `data_fim_prevista` igual ou anterior à `data_inicio` é recusada.
- Ao confirmar, o imóvel passa para `alugado` e a locação para `ativa`.
- Imóvel indisponível ou já alugado não aparece na seleção.
