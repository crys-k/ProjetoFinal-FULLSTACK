# Fases de desenvolvimento — Sistema de Aluguel de Imóveis (Imobiliária)

Cada arquivo desta pasta é uma fase executável de forma independente: contexto,
pré-requisitos, ações, critério de aceite e mensagem de commit.

Briefing: `.claude/docs/gerenciamento-imobiliaria-descricao.md`
Regras de código: `CLAUDE.md` (raiz do projeto)

App: `imobiliaria` · Projeto: `ProjetoFinal` · Django 6.1.2 · SQLite

| Fase | Arquivo | Entrega | CU |
|---|---|---|---|
| 0 | `fase-00-green-field.md` | Limpeza do app (green field) | — |
| 1 | `fase-01-fundacao-templates.md` | base.html, nav-bar, home | — |
| 2 | `fase-02-autenticacao.md` | Login e logout | — |
| 3 | `fase-03-funcionarios.md` | Gerir Funcionários | 1 |
| 4 | `fase-04-imoveis.md` | Cadastrar/Editar/Remover Imóvel | 2, 3 |
| 5 | `fase-05-clientes.md` | Gerenciar Clientes | 4 |
| 6 | `fase-06-locacoes.md` | Criar Locação | 5 |
| 7 | `fase-07-finalizar-cancelar-locacao.md` | Finalizar / Cancelar Locação | 6, 7 |
| 8 | `fase-08-bloqueio-imovel.md` | Bloquear/Desbloquear Imóvel | 9 |
| 9 | `fase-09-ocorrencias.md` | Ocorrências no Imóvel | 10 |
| 10 | `fase-10-relatorios.md` | Relatórios de Locações | 8 |
| 11 | `fase-11-pesquisa-imoveis.md` | Pesquisar Imóveis Disponíveis | 11 |
| 12 | `fase-12-acabamento.md` | Dashboard e acabamento | — |

## Dependências

```
0 -> 1 -> 2 -> 3
          |
          +-> 4 -> 6 -> 7 -> 10
          +-> 5 -> 6
          4 -> 8
          4 -> 9
          4 -> 11
          tudo -> 12
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
