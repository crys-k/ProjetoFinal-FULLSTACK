# Fase 11 — Pesquisar Imóveis Disponíveis (CU 11)

**Pré-requisito:** Fase 4 concluída
**Caso de uso:** CU 11 — Pesquisar Imóveis Disponíveis (ator: Funcionário)
**Commit:** `feat: implementa pesquisa de imoveis disponiveis`

## Objetivo

Permitir que o funcionário busque imóveis disponíveis para locação a partir
de critérios combinados, para apoiar o atendimento ao cliente.

## Ações

### models
Nenhuma alteração.

### views / urls
- `imovel_pesquisa` — lê os critérios de `request.GET` (endereço/localização,
  tipo, número mínimo de quartos, faixa de `valor_aluguel`) e monta o
  queryset com `filter()` encadeado apenas para os campos preenchidos, sempre
  restrito a `status='disponivel'`
- `imovel_detalhe` — dados completos de um imóvel específico

urls: `imoveis/pesquisa/`, `imoveis/<int:id>/`.

### forms
- `PesquisaImovelForm` (`forms.Form`) — campos de busca, todos
  `required=False`

### templates
- `imovel_pesquisa.html` — formulário de busca e lista de resultados
- `imovel_detalhe.html`

### _partials
- `_filtro-imoveis.html` — formulário GET de busca
- reaproveitar `_imovel-card.html` (Fase 4) na lista de resultados

## Aceite

- Sem critérios, lista todos os imóveis disponíveis.
- Cada critério reduz corretamente o resultado e os critérios se combinam.
- Imóvel alugado ou indisponível nunca aparece nos resultados.
- O funcionário consegue abrir o detalhe de um imóvel a partir do resultado.
