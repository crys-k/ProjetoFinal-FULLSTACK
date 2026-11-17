# Regras de geração de código — ProjetoFinal (Django)

Projeto: Sistema de Aluguel de Imóveis (Imobiliária) (ver `.claude/docs/gerenciamento-imobiliaria-descricao.md`).
App principal: `imobiliaria`. Projeto: `ProjetoFinal`. Django 6.1.2 + SQLite.

## 1. Escopo da linguagem usada

Use **somente construções apresentadas em aula**. Na dúvida entre uma solução
"mais elegante" e uma solução simples já vista na disciplina, escolha a simples.

- Views **baseadas em função** (FBV). Não usar Class-Based Views (`ListView`, `CreateView`, etc.).
- Formulários com `forms.ModelForm` / `forms.Form`.
- ORM padrão: `objects.all()`, `filter()`, `get()`, `order_by()`, `exclude()`.
- Nada de `signals`, `middleware` próprio, `mixins`, `context processors` próprios,
  managers customizados ou metaprogramação sem pedido explícito.

## 2. Decorators

- O **único** decorator permitido em views é o de autenticação do próprio Django:
  `@login_required` (de `django.contrib.auth.decorators`).
- **Nenhum outro decorator**: não usar `@require_POST`, `@require_http_methods`,
  `@csrf_exempt`, `@permission_required`, `@transaction.atomic`, nem decorators
  escritos à mão.
- Restrição de método HTTP se resolve com `if` dentro da view:

```python
@login_required
def cliente_novo(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('imobiliaria:cliente_lista')
    else:
        form = ClienteForm()
    return render(request, 'imobiliaria/cliente_form.html', {'form': form})
```

## 3. Ordem de implementação

Sempre que possível, respeitar esta ordem ao desenvolver uma funcionalidade:

1. **models.py** — entidades, campos, `choices`, `__str__`, `Meta` se necessário
2. **views.py** — lógica da funcionalidade (e `urls.py` junto da view)
3. **templates** — a página
4. **_partials** — componentes extraídos do template

Não pular etapas: não criar template de algo que ainda não tem view, nem view de
model que ainda não existe. Depois de alterar `models.py`, lembrar das migrations
(`makemigrations` / `migrate`) — mas só executá-las quando solicitado.

## 4. Templates e partials

- Templates ficam em `imobiliaria/templates/imobiliaria/`.
- Partials (componentes reutilizáveis) ficam em
  `imobiliaria/templates/imobiliaria/_partials/` e o **nome do arquivo começa com
  underline**: `_nav-bar.html`, `_form-campos.html`, `_cliente-card.html`.
- O underline identifica componente; arquivos sem underline são páginas.
- Páginas estendem `base.html` e usam `{% include %}` para os partials.
- Todo `<form>` com POST precisa de `{% csrf_token %}`.

## 5. Nomenclatura

- Models: singular, PascalCase (`Cliente`, `Imovel`, `Locacao`).
- Campos, funções e variáveis: `snake_case` em português (`data_inicio`, `imovel_lista`).
- Forms: PascalCase terminando em `Form` (`ClienteForm`) — não `clienteForm`.
- URLs nomeadas por recurso + ação: `cliente_lista`, `cliente_novo`, `cliente_editar`.
- Sempre usar `app_name = 'imobiliaria'` e referenciar como `{% url 'imobiliaria:cliente_lista' %}`.

## 6. Comentários

- Evitar comentários extensos. Se o código é autoexplicativo pelos nomes de
  métodos, variáveis e campos, **não comentar**.
- Comentar apenas regra de negócio não óbvia (ex.: por que uma data é validada
  de determinada forma).
- Não gerar docstrings em toda função nem comentários do tipo `# salva o form`.

## 7. Boas práticas Django mantidas

- Lógica de dados no model (`__str__`, `save()`, métodos de apoio); view fica
  responsável por requisição/resposta.
- Validação em `forms.py` (`clean_<campo>`, `clean`), não no template.
- `redirect()` depois de POST bem-sucedido (nunca `render` direto).
- `get_object_or_404` para buscar registro por id.
- `django.contrib.messages` para feedback ao usuário.
- Nada de SQL cru nem de dados sensíveis fixos no código.

## 8. Comandos e dependências

- **Não executar comandos git** (`commit`, `push`, `pull`, `merge`, `add`, `checkout`...)
  a menos que explicitamente solicitado.
- **Não instalar bibliotecas** por conta própria. Se alguma dependência externa
  parecer necessária, pedir aprovação do programador antes — preferência sempre
  pelo que já vem no Django.
- `requirements.txt` só muda com aprovação.

## 9. Conclusão de fase

Ao concluir uma fase do desenvolvimento, deixar no final da resposta uma lista
de commits sugeridos, agrupando os arquivos que devem ser comitados juntos em
cada commit.

- Cada commit sugerido traz: os arquivos envolvidos e a mensagem de commit.
- Mensagem de commit segue a estrutura `[flag]: [mensagem]`.
- Flags possíveis: `feat`, `docs`, `fix`, `chore`.
