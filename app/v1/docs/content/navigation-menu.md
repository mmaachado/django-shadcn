---
title: Navigation Menu
description: A collection of links for navigating websites.
description.pt-br: Um conjunto de links para navegar pelo site.
description.es: Un conjunto de enlaces para navegar por el sitio.
---

<c-docs.demo-section class="min-h-[350px]">
<c-navigation-menu>
<c-navigation-menu.list>
<c-navigation-menu.item>
<c-navigation-menu.trigger index="0">Getting started</c-navigation-menu.trigger>
<c-navigation-menu.content index="0">
<div class="md:w-[220px]">
<c-navigation-menu.link href="#">Introduction<c-navigation-menu.link_details>What the library is.</c-navigation-menu.link_details></c-navigation-menu.link>
<c-navigation-menu.link href="#">Installation<c-navigation-menu.link_details>Set up your project.</c-navigation-menu.link_details></c-navigation-menu.link>
</div>
</c-navigation-menu.content>
</c-navigation-menu.item>
<c-navigation-menu.item>
<c-navigation-menu.link href="#">Documentation</c-navigation-menu.link>
</c-navigation-menu.item>
</c-navigation-menu.list>
</c-navigation-menu>
</c-docs.demo-section>

<c-docs.cheat-sheet name="navigation-menu">
<c-navigation-menu>
  <c-navigation-menu.list>
    <c-navigation-menu.item>
      <c-navigation-menu.trigger index="0">Products</c-navigation-menu.trigger>
      <c-navigation-menu.content index="0">
        <c-navigation-menu.link href="{% url 'pricing' %}">Pricing</c-navigation-menu.link>
      </c-navigation-menu.content>
    </c-navigation-menu.item>
  </c-navigation-menu.list>
</c-navigation-menu>
</c-docs.cheat-sheet>

:::en
## Installation
:::pt-br
## Instalação
:::

```bash
uvx django_shadcn@latest add navigation_menu
```

:::en
## Usage

A row of links for a site's header, where a trigger opens a panel of more
links on hover or click. Each trigger and its content share an `index`, which
is how the trigger finds its panel. An item without a trigger is a plain link.

The links are `<a>`s, so `href` takes Django's `url` tag. The panels open
through Alpine; without JavaScript the triggers do nothing and the panels stay
closed, so keep every page reachable from a plain link too.
:::pt-br
## Uso

Uma fileira de links para o cabeçalho de um site, em que um trigger abre um
painel com mais links no hover ou no clique. Cada trigger e o conteúdo dele
dividem um `index`, que é como o trigger encontra o painel. Um item sem trigger
é um link simples.

Os links são `<a>`s, então o `href` aceita a tag `url` do Django. Os painéis
abrem pelo Alpine; sem JavaScript os triggers não fazem nada e os painéis ficam
fechados, então mantenha toda página alcançável também por um link simples.
:::

```html
<c-navigation-menu>
  <c-navigation-menu.list>
    {% for section in sections %}
      <c-navigation-menu.item>
        <c-navigation-menu.trigger index="{{ forloop.counter0 }}">{{ section.title }}</c-navigation-menu.trigger>
        <c-navigation-menu.content index="{{ forloop.counter0 }}">
          {% for page in section.pages %}
            <c-navigation-menu.link href="{{ page.url }}">{{ page.title }}</c-navigation-menu.link>
          {% endfor %}
        </c-navigation-menu.content>
      </c-navigation-menu.item>
    {% endfor %}
  </c-navigation-menu.list>
</c-navigation-menu>
```

:::en
## Examples

### With details

`link_details` adds a line under a link's title.
:::pt-br
## Exemplos

### Com detalhes

O `link_details` acrescenta uma linha embaixo do título de um link.
:::

<c-docs.example>
<c-navigation-menu>
  <c-navigation-menu.list>
    <c-navigation-menu.item>
      <c-navigation-menu.trigger index="0">Components</c-navigation-menu.trigger>
      <c-navigation-menu.content index="0">
        <div class="md:w-[240px]">
          <c-navigation-menu.link href="#">
            Button
            <c-navigation-menu.link_details>A button, or something that looks like one.</c-navigation-menu.link_details>
          </c-navigation-menu.link>
          <c-navigation-menu.link href="#">
            Dialog
            <c-navigation-menu.link_details>A window over the page.</c-navigation-menu.link_details>
          </c-navigation-menu.link>
        </div>
      </c-navigation-menu.content>
    </c-navigation-menu.item>
  </c-navigation-menu.list>
</c-navigation-menu>
</c-docs.example>

:::en
## RTL

The list runs with the text, so under `dir="rtl"` the first item is on the
right, and a panel opens from the start of its trigger.

## Accessibility

The menu is a `<nav>` around a list, and each trigger is a `<button>` that
reports `aria-expanded`. Escape closes the open panel. The panels open on
hover as well as on click, and there is no arrow-key navigation between the
triggers: Tab moves through them and into an open panel.

## API reference
:::pt-br
## RTL

A lista corre com o texto, então sob `dir="rtl"` o primeiro item fica à
direita, e um painel abre a partir do início do trigger.

## Acessibilidade

O menu é um `<nav>` em volta de uma lista, e cada trigger é um `<button>` que
informa `aria-expanded`. O Escape fecha o painel aberto. Os painéis abrem no
hover além do clique, e não há navegação pelas setas entre os triggers: o Tab
passa por eles e entra num painel aberto.

## Referência da API
:::

<c-docs.api-reference name="navigation-menu" />

:::en
## Notes

Upstream's link component example hands the link to a router. A Django
template links with `<a>`, which `navigation-menu.link` already renders.
:::pt-br
## Observações

O exemplo de link component do upstream entrega o link a um roteador. Um
template Django cria links com `<a>`, que o `navigation-menu.link` já
renderiza.
:::
