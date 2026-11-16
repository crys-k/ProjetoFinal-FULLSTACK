# Fase 13 — Dashboard e acabamento

**Pré-requisito:** todas as fases anteriores concluídas
**Caso de uso:** nenhum
**Commit:** `refactor: acabamento de navegacao e dashboard`

## Objetivo

Fechar o sistema: visão geral na home, navegação coerente e revisão final contra
as regras do projeto.

## Ações

### models
Nenhuma alteração.

### views / urls
- `index` passa a montar o dashboard:
  - quartos disponíveis / ocupados / em manutenção
  - check-ins previstos para hoje
  - reservas em andamento
  - ocorrências pendentes

### templates
- `index.html` — dashboard com os indicadores

### _partials
- `_indicador.html` — card de indicador reaproveitado para cada número
- `_nav-bar.html` — revisão dos links e da separação entre itens de funcionário e
  de administrador

### admin.py
Registrar os models (`TipoQuarto`, `Quarto`, `Cliente`, `Funcionario`, `Reserva`,
`Ocorrencia`) para apoio durante a apresentação.

### Revisão final contra o `CLAUDE.md`
- nenhum decorator além de `@login_required`
- nenhuma view class-based
- todos os partials com underline no nome e dentro de `_partials/`
- sem comentários desnecessários
- forms com nome em PascalCase terminando em `Form`
- todas as rotas com `app_name` e referenciadas como `imobiliaria:<nome>`

## Aceite

- Home mostra os indicadores com números coerentes com o banco.
- Toda funcionalidade do briefing é alcançável pela navegação.
- `python manage.py check` sem erros e todos os fluxos navegáveis sem erro 500.
