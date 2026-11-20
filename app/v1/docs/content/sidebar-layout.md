---
title: Sidebar Layout
description: The application shell, a sidebar, a header with a breadcrumb and an account menu, and the area a page fills.
description.pt-br: A casca da aplicação, uma sidebar, um cabeçalho com breadcrumb e menu de conta, e a área que uma página preenche.
description.es: El armazón de la aplicación, una sidebar, una cabecera con breadcrumb y menú de cuenta, y el área que llena una página.
---

<c-docs.block-preview name="sidebar-layout" />

:::en
## Installation
:::pt-br
## Instalação
:::

```bash
uvx django_shadcn@latest add sidebar_layout
```

:::en
This is a block, not a component. It installs
`templates/blocks/sidebar_layout/page.html`, and the components it uses to
`templates/cotton/`.

## Usage

Unlike the other blocks, this one is meant to be extended. Copy it to where
your layouts live, then let each page extend it and fill
`{% verbatim %}{% block main %}{% endverbatim %}`:
:::pt-br
Isto é um bloco, não um componente. Ele instala
`templates/blocks/sidebar_layout/page.html`, e os componentes que ele usa em
`templates/cotton/`.

## Uso

Diferente dos outros blocos, este foi feito para ser estendido. Copie-o para
onde ficam os seus layouts, e deixe cada página estendê-lo e preencher o
`{% verbatim %}{% block main %}{% endverbatim %}`:
:::

```bash
cp templates/blocks/sidebar_layout/page.html templates/layouts/app.html
```

```django
{% extends "layouts/app.html" %}

{% block main %}
    <h1 class="text-2xl font-semibold">Projects</h1>
{% endblock %}
```

:::en
The layout itself extends your `base.html` and fills its
`{% verbatim %}{% block content %}{% endverbatim %}`, so the stylesheet and
Alpine still come from there. Until `main` is filled, it shows placeholder
tiles.

## Making it yours

The navigation, the breadcrumb and the account menu are sample data. In a real
layout they come from the request: mark the current page with
`is_active="true"`, build the breadcrumb from the view, and put the user's name
and email in the menu.

The sidebar's open state survives a reload once the view reads the
`sidebar_state` cookie, as the [Sidebar]({% url 'page' slug='sidebar' %}) page
describes. For a different side, a floating panel or a rail of icons, the
props on `<c-sidebar>` are the ones that page documents.

## Made of

[Sidebar]({% url 'page' slug='sidebar' %}),
[Breadcrumb]({% url 'page' slug='breadcrumb' %}),
[Dropdown Menu]({% url 'page' slug='dropdown-menu' %}),
[Avatar]({% url 'page' slug='avatar' %}),
[Button]({% url 'page' slug='button' %}) and
[Separator]({% url 'page' slug='separator' %}).
:::pt-br
O próprio layout estende o seu `base.html` e preenche o
`{% verbatim %}{% block content %}{% endverbatim %}` dele, então a folha de
estilo e o Alpine continuam vindo de lá. Enquanto `main` não for preenchido,
ele mostra blocos de exemplo.

## Deixando com a sua cara

A navegação, o breadcrumb e o menu da conta são dados de exemplo. Num layout de
verdade eles vêm da requisição: marque a página atual com `is_active="true"`,
monte o breadcrumb a partir da view e ponha o nome e o e-mail do usuário no
menu.

O estado de aberta da sidebar sobrevive a um recarregamento quando a view lê o
cookie `sidebar_state`, como descreve a página da
[Sidebar]({% url 'page' slug='sidebar' %}). Para outro lado, um painel
flutuante ou uma faixa de ícones, as props do `<c-sidebar>` são as que aquela
página documenta.

## Feito de

[Sidebar]({% url 'page' slug='sidebar' %}),
[Breadcrumb]({% url 'page' slug='breadcrumb' %}),
[Dropdown Menu]({% url 'page' slug='dropdown-menu' %}),
[Avatar]({% url 'page' slug='avatar' %}),
[Button]({% url 'page' slug='button' %}) e
[Separator]({% url 'page' slug='separator' %}).
:::
