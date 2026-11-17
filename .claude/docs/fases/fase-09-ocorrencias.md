# Fase 9 — Registrar Ocorrências no Imóvel (CU 10)

**Pré-requisito:** Fase 4 concluída (Fase 3 se a ocorrência registrar o funcionário)
**Caso de uso:** CU 10 — Registrar Ocorrências no Imóvel (ator: Funcionário)
**Commit:** `feat: implementa registro de ocorrencias em imoveis`

## Objetivo

Registrar problemas identificados nos imóveis (necessidade de manutenção) e
acompanhar a resolução.

## Ações

### models
`Ocorrencia`
- `imovel` — `ForeignKey(Imovel, on_delete=models.CASCADE, related_name='ocorrencias')`
- `funcionario` — `ForeignKey(Funcionario, on_delete=models.PROTECT, null=True)`
- `descricao` — `TextField`
- `resolvida` — `BooleanField(default=False)`
- `registrada_em` — `DateTimeField(auto_now_add=True)`
- `resolvida_em` — `DateTimeField(null=True, blank=True)`
- método `resolver()` — marca `resolvida = True` e grava `resolvida_em`
- `Meta.ordering` por `-registrada_em`

Migration da fase.

### views / urls
- `ocorrencia_lista` — filtro por imóvel e por pendente/resolvida
- `ocorrencia_nova` — escolhe o imóvel e descreve o problema; o funcionário
  vem de `request.user`
- `ocorrencia_resolver` — chama `resolver()`

urls: `ocorrencias/`, `ocorrencias/nova/`, `ocorrencias/<int:id>/resolver/`.

### forms
- `OcorrenciaForm` — `ModelForm` com `imovel` e `descricao`

### templates
- `ocorrencia_lista.html`
- `ocorrencia_form.html`

### _partials
- `_ocorrencia-linha.html`
- `_imovel-card.html` — pode exibir a contagem de ocorrências pendentes do
  imóvel

## Aceite

- Ocorrência registrada aparece vinculada ao imóvel e ao funcionário que
  registrou.
- Resolver a ocorrência grava a data e tira do filtro de pendentes.
- Imóveis com ocorrência pendente ficam visíveis para o administrador na
  listagem de imóveis.
