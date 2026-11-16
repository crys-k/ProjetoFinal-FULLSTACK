# Fases de desenvolvimento — Sistema de Gerenciamento de Hotel

Cada arquivo desta pasta é uma fase executável de forma independente: contexto,
pré-requisitos, ações, critério de aceite e mensagem de commit.

Briefing: `.claude/docs/gerenciamento-hotel-descricao.md`
Regras de código: `CLAUDE.md` (raiz do projeto)

App: `imobiliaria` · Projeto: `ProjetoFinal` · Django 6.1.2 · SQLite

| Fase | Arquivo | Entrega | CU |
|---|---|---|---|
| 0 | `fase-00-green-field.md` | Limpeza do app (green field) | — |
| 1 | `fase-01-fundacao-templates.md` | base.html, nav-bar, home | — |
| 2 | `fase-02-autenticacao.md` | Login e logout | — |
| 3 | `fase-03-funcionarios.md` | Gerenciar Funcionários | 3 |
| 4 | `fase-04-tipos-quarto-tarifas.md` | Tipos de quarto e tarifas | 11 |
| 5 | `fase-05-quartos.md` | Gerenciar Quartos | 1 |
| 6 | `fase-06-bloqueio-quartos.md` | Bloquear/desbloquear quarto | 8 |
| 7 | `fase-07-clientes.md` | Gerenciar Clientes | 2 |
| 8 | `fase-08-reservas.md` | Criar e listar Reservas | 4 |
| 9 | `fase-09-check-in-check-out.md` | Check-in e Check-out | 5, 6 |
| 10 | `fase-10-cancelar-reserva.md` | Cancelar Reserva | 7 |
| 11 | `fase-11-ocorrencias.md` | Ocorrências em quartos | 10 |
| 12 | `fase-12-relatorios.md` | Relatórios de reservas | 9 |
| 13 | `fase-13-acabamento.md` | Dashboard e acabamento | — |

## Dependências

```
0 -> 1 -> 2 -> 3
          |
          +-> 4 -> 5 -> 6
          +-> 7
                 5 e 7 -> 8 -> 9 -> 10
                          8 -> 12
                 5 -> 11
          tudo -> 13
```

## Regras válidas para todas as fases

- Ordem de implementação dentro da fase: `models -> views (+urls) -> template -> _partials`.
- Cada fase termina com o sistema rodando (`manage.py check` passa e servidor sobe)
  e rende **um commit**.
- Toda view protegida usa `@login_required`, o único decorator do projeto.
  Perfil de usuário (admin) e método HTTP são tratados com `if` dentro da view.
- Partials começam com underline (`_nav-bar.html`) e ficam em
  `imobiliaria/templates/imobiliaria/_partials/`.
- Nenhum comando git é executado sem pedido explícito do programador.
- Nenhuma biblioteca é instalada sem aprovação: só Django puro.
- `makemigrations` / `migrate` são gerados por fase que mexe em `models.py`, mas
  só executados quando solicitado.
