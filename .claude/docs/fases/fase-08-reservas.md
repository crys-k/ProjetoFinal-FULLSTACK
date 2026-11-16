# Fase 8 — Criar e listar reservas (CU 4)

**Pré-requisito:** Fases 5 e 7 concluídas
**Caso de uso:** CU 4 — Criar Reserva de Quarto (ator: Funcionário)
**Commit:** `feat: implementa criacao e listagem de reservas`

## Objetivo

Núcleo do sistema: registrar reservas de clientes em quartos disponíveis, sem
sobreposição de datas.

## Ações

### models
`Reserva`
- `cliente` — `ForeignKey(Cliente, on_delete=models.PROTECT)`
- `quarto` — `ForeignKey(Quarto, on_delete=models.PROTECT)`
- `funcionario` — `ForeignKey(Funcionario, on_delete=models.PROTECT, null=True)`
- `data_entrada` — `DateField`
- `data_saida` — `DateField`
- `status` — `CharField` com `choices`:
  `pendente` / `em_andamento` / `finalizada` / `cancelada`
- `valor_total` — `DecimalField(max_digits=10, decimal_places=2)`
- `criada_em` — `DateTimeField(auto_now_add=True)`
- método `total_diarias()` — diferença entre as datas
- método `calcular_valor_total()` — `total_diarias() * quarto.tipo.valor_diaria`
- `__str__` com cliente, quarto e período
- `Meta.ordering` por `-criada_em`

Migration da fase.

### views / urls
- `reserva_lista` — filtro por status lido de `request.GET`
- `reserva_nova` — seleciona cliente (busca) e quarto disponível, define as datas
  e grava com `status = 'pendente'` e `valor_total` calculado
- `reserva_detalhe` — dados completos da reserva

urls: `reservas/`, `reservas/nova/`, `reservas/<int:id>/`.

### forms
`ReservaForm` — `ModelForm` com:
- `clean()` validando `data_saida > data_entrada`
- `clean()` validando que não existe outra reserva ativa (`pendente` ou
  `em_andamento`) no mesmo quarto com período sobreposto
- queryset de `quarto` excluindo quartos em manutenção/bloqueados (Fase 6)

### templates
- `reserva_lista.html`
- `reserva_form.html`
- `reserva_detalhe.html`

### _partials
- `_reserva-linha.html`
- `_selecao-quarto.html` — lista de quartos disponíveis no período
- reaproveitar `_busca-cliente.html` da Fase 7

Também incluir o histórico de reservas em `cliente_detalhe.html`.

## Aceite

- Reserva é criada apenas para quarto disponível no período.
- Período sobreposto no mesmo quarto é recusado com mensagem clara.
- `data_saida` igual ou anterior à `data_entrada` é recusada.
- `valor_total` corresponde a diárias x tarifa do tipo do quarto.
- Quarto bloqueado não aparece na seleção.
