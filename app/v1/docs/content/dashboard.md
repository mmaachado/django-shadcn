---
title: Dashboard
description: An application page with a sidebar, four metrics, a revenue chart and a table of recent orders.
description.pt-br: Uma página de aplicação com sidebar, quatro métricas, um gráfico de receita e uma tabela de pedidos recentes.
description.es: Una página de aplicación con sidebar, cuatro métricas, un gráfico de ingresos y una tabla de pedidos recientes.
---

<c-docs.block-preview name="dashboard" />

:::en
## Installation
:::pt-br
## Instalação
:::

```bash
uvx django_shadcn@latest add dashboard
```

:::en
This is a block, not a component. It installs the page to
`templates/blocks/dashboard/page.html`, and `sidebar`, `metric`, `chart`,
`table` and the rest of what it uses to `templates/cotton/`.

## Usage

Render the page from a view:
:::pt-br
Isto é um bloco, não um componente. Ele instala a página em
`templates/blocks/dashboard/page.html`, e o `sidebar`, o `metric`, o `chart`,
o `table` e o resto do que ele usa em `templates/cotton/`.

## Uso

Renderize a página a partir de uma view:
:::

```python
from django.shortcuts import render


def dashboard(request):
    return render(request, "blocks/dashboard/page.html")
```

:::en
The page extends your `base.html` and fills its
`{% verbatim %}{% block content %}{% endverbatim %}`, the same contract the
`allauth` templates use. To put it inside another layout, pass the template
name as `base_template`:
:::pt-br
A página estende o seu `base.html` e preenche o
`{% verbatim %}{% block content %}{% endverbatim %}` dele, o mesmo contrato que
os templates do `allauth` usam. Para colocá-la dentro de outro layout, passe o
nome do template como `base_template`:
:::

```python
return render(
    request,
    "blocks/dashboard/page.html",
    {"base_template": "layouts/app.html"},
)
```

:::en
## Making it yours

Every number, row and link on the page is sample data written into the markup.
It is a starting point to edit, the way a copied component is: replace the
metrics with your view's figures, loop over your orders in the table body, and
send the chart its rows as JSON from the view, as the
[Chart]({% url 'page' slug='chart' %}) page shows. Keep the escaping: the
chart's `data` must not be marked safe.

The sidebar is `collapsible="icon"`, so it folds to a rail of icons rather than
sliding away. Its open state survives a reload once the view reads the
`sidebar_state` cookie, as the [Sidebar]({% url 'page' slug='sidebar' %}) page
describes.

## Made of

[Sidebar]({% url 'page' slug='sidebar' %}),
[Breadcrumb]({% url 'page' slug='breadcrumb' %}),
[Metric]({% url 'page' slug='metric' %}),
[Chart]({% url 'page' slug='chart' %}),
[Card]({% url 'page' slug='card' %}),
[Table]({% url 'page' slug='table' %}),
[Badge]({% url 'page' slug='badge' %}) and
[Separator]({% url 'page' slug='separator' %}). Nothing in the block is a
component of its own.
:::pt-br
## Deixando com a sua cara

Todo número, linha e link da página é um dado de exemplo escrito no markup. É
um ponto de partida para editar, como um componente copiado: troque as métricas
pelos números da sua view, percorra os seus pedidos no corpo da tabela e envie
ao gráfico as linhas dele em JSON a partir da view, como mostra a página do
[Chart]({% url 'page' slug='chart' %}). Mantenha o escape: o `data` do gráfico
não pode ser marcado como seguro.

A sidebar é `collapsible="icon"`, então ela se recolhe numa faixa de ícones em
vez de deslizar para fora. O estado de aberta sobrevive a um recarregamento
quando a view lê o cookie `sidebar_state`, como descreve a página da
[Sidebar]({% url 'page' slug='sidebar' %}).

## Feito de

[Sidebar]({% url 'page' slug='sidebar' %}),
[Breadcrumb]({% url 'page' slug='breadcrumb' %}),
[Metric]({% url 'page' slug='metric' %}),
[Chart]({% url 'page' slug='chart' %}),
[Card]({% url 'page' slug='card' %}),
[Table]({% url 'page' slug='table' %}),
[Badge]({% url 'page' slug='badge' %}) e
[Separator]({% url 'page' slug='separator' %}). Nada no bloco é um componente
próprio.
:::
