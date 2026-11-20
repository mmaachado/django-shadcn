---
title: Breadcrumb
description: Displays the path to the current resource using a hierarchy of links.
description.pt-br: Mostra o caminho até a página atual como uma hierarquia de links.
description.es: Muestra la ruta hasta la página actual como una jerarquía de enlaces.
---

<c-docs.demo-section class="min-h-[350px]">
<c-breadcrumb>
<c-breadcrumb.list>
<c-breadcrumb.item>
<c-breadcrumb.link href="#">Home</c-breadcrumb.link>
</c-breadcrumb.item>
<c-breadcrumb.separator />
<c-breadcrumb.item>
<c-breadcrumb.link href="#">Components</c-breadcrumb.link>
</c-breadcrumb.item>
<c-breadcrumb.separator />
<c-breadcrumb.item>
<c-breadcrumb.page>Breadcrumb</c-breadcrumb.page>
</c-breadcrumb.item>
</c-breadcrumb.list>
</c-breadcrumb>
</c-docs.demo-section>

<c-docs.cheat-sheet name="breadcrumb">
<c-breadcrumb>
  <c-breadcrumb.list>
    <c-breadcrumb.item>
      <c-breadcrumb.link href="{% url 'home' %}">Home</c-breadcrumb.link>
    </c-breadcrumb.item>
    <c-breadcrumb.separator />
    <c-breadcrumb.item>
      <c-breadcrumb.page>{{ object }}</c-breadcrumb.page>
    </c-breadcrumb.item>
  </c-breadcrumb.list>
</c-breadcrumb>
</c-docs.cheat-sheet>

:::en
## Installation
:::pt-br
## Instalação
:::

```bash
uvx django_shadcn@latest add breadcrumb
```

:::en
## Usage

A breadcrumb is a `<nav>` around an ordered list: links for the levels above,
a separator between them, and the current page last, as text rather than a
link. It is plain markup and needs no JavaScript.

The trail usually comes from the view, so loop over it and leave the last
step out of the loop:
:::pt-br
## Uso

Um breadcrumb é um `<nav>` em volta de uma lista ordenada: links para os níveis
de cima, um separador entre eles, e a página atual por último, como texto e não
como link. É markup simples e não precisa de JavaScript.

A trilha costuma vir da view, então percorra-a e deixe o último passo fora do
laço:
:::

```html
<c-breadcrumb>
  <c-breadcrumb.list>
    {% for title, url in trail %}
      <c-breadcrumb.item>
        <c-breadcrumb.link href="{{ url }}">{{ title }}</c-breadcrumb.link>
      </c-breadcrumb.item>
      <c-breadcrumb.separator />
    {% endfor %}
    <c-breadcrumb.item>
      <c-breadcrumb.page>{{ object }}</c-breadcrumb.page>
    </c-breadcrumb.item>
  </c-breadcrumb.list>
</c-breadcrumb>
```

:::en
## Examples

### Basic
:::pt-br
## Exemplos

### Básico
:::

<c-docs.example>
<c-breadcrumb>
  <c-breadcrumb.list>
    <c-breadcrumb.item>
      <c-breadcrumb.link href="#">Home</c-breadcrumb.link>
    </c-breadcrumb.item>
    <c-breadcrumb.separator />
    <c-breadcrumb.item>
      <c-breadcrumb.link href="#">Settings</c-breadcrumb.link>
    </c-breadcrumb.item>
    <c-breadcrumb.separator />
    <c-breadcrumb.item>
      <c-breadcrumb.page>Billing</c-breadcrumb.page>
    </c-breadcrumb.item>
  </c-breadcrumb.list>
</c-breadcrumb>
</c-docs.example>

:::en
### Custom separator

Whatever you put inside `<c-breadcrumb.separator>` replaces the chevron.
:::pt-br
### Separador personalizado

O que você puser dentro de `<c-breadcrumb.separator>` substitui o chevron.
:::

<c-docs.example>
<c-breadcrumb>
  <c-breadcrumb.list>
    <c-breadcrumb.item>
      <c-breadcrumb.link href="#">Home</c-breadcrumb.link>
    </c-breadcrumb.item>
    <c-breadcrumb.separator>/</c-breadcrumb.separator>
    <c-breadcrumb.item>
      <c-breadcrumb.page>Components</c-breadcrumb.page>
    </c-breadcrumb.item>
  </c-breadcrumb.list>
</c-breadcrumb>
</c-docs.example>

:::en
### Dropdown

A [Dropdown Menu]({% url 'page' slug='dropdown-menu' %}) in an item offers the
levels beside the current one.
:::pt-br
### Dropdown

Um [Dropdown Menu]({% url 'page' slug='dropdown-menu' %}) num item oferece os
níveis ao lado do atual.
:::

<c-docs.example>
<c-breadcrumb>
  <c-breadcrumb.list>
    <c-breadcrumb.item>
      <c-breadcrumb.link href="#">Home</c-breadcrumb.link>
    </c-breadcrumb.item>
    <c-breadcrumb.separator />
    <c-breadcrumb.item>
      <c-dropdown-menu>
        <c-dropdown-menu.trigger>
          <button type="button" class="flex items-center gap-1 hover:text-foreground">
            Components
            <c-icon name="chevron-down" class="size-3.5" />
          </button>
        </c-dropdown-menu.trigger>
        <c-dropdown-menu.content>
          <c-dropdown-menu.item>Documentation</c-dropdown-menu.item>
          <c-dropdown-menu.item>Themes</c-dropdown-menu.item>
          <c-dropdown-menu.item>GitHub</c-dropdown-menu.item>
        </c-dropdown-menu.content>
      </c-dropdown-menu>
    </c-breadcrumb.item>
    <c-breadcrumb.separator />
    <c-breadcrumb.item>
      <c-breadcrumb.page>Breadcrumb</c-breadcrumb.page>
    </c-breadcrumb.item>
  </c-breadcrumb.list>
</c-breadcrumb>
</c-docs.example>

:::en
### Collapsed

`<c-breadcrumb.ellipsis>` stands in for the levels left out of a long trail.
:::pt-br
### Recolhido

O `<c-breadcrumb.ellipsis>` fica no lugar dos níveis deixados de fora de uma
trilha longa.
:::

<c-docs.example>
<c-breadcrumb>
  <c-breadcrumb.list>
    <c-breadcrumb.item>
      <c-breadcrumb.link href="#">Home</c-breadcrumb.link>
    </c-breadcrumb.item>
    <c-breadcrumb.separator />
    <c-breadcrumb.item>
      <c-breadcrumb.ellipsis />
    </c-breadcrumb.item>
    <c-breadcrumb.separator />
    <c-breadcrumb.item>
      <c-breadcrumb.link href="#">Components</c-breadcrumb.link>
    </c-breadcrumb.item>
    <c-breadcrumb.separator />
    <c-breadcrumb.item>
      <c-breadcrumb.page>Breadcrumb</c-breadcrumb.page>
    </c-breadcrumb.item>
  </c-breadcrumb.list>
</c-breadcrumb>
</c-docs.example>

:::en
## RTL

The list runs with the text, so under `dir="rtl"` home is on the right. The
default chevron turns around with it, so it still points towards the current
page.

## Accessibility

The `<nav>` carries `aria-label="breadcrumb"`, and the trail is an `<ol>`, so a
screen reader announces how many levels there are. The current page has
`aria-current="page"` and is not a link. The separators are hidden from
assistive technology, and so is the ellipsis, including its "More" label:
when the collapsed levels matter, make the ellipsis open them, as a dropdown.

## API reference
:::pt-br
## RTL

A lista corre com o texto, então sob `dir="rtl"` o início fica à direita. O
chevron padrão se vira junto, então continua apontando para a página atual.

## Acessibilidade

O `<nav>` leva `aria-label="breadcrumb"` e a trilha é um `<ol>`, então um
leitor de tela anuncia quantos níveis existem. A página atual tem
`aria-current="page"` e não é um link. Os separadores ficam escondidos das
tecnologias assistivas, e a reticência também, inclusive o rótulo "More": quando
os níveis recolhidos importarem, faça a reticência abri-los, como um dropdown.

## Referência da API
:::

<c-docs.api-reference name="breadcrumb" />

:::en
## Notes

Upstream's link component example swaps the anchor for a router's link. A
Django template links with `<a>` and `{% verbatim %}{% url %}{% endverbatim %}`,
so `<c-breadcrumb.link>` already is that.
:::pt-br
## Observações

O exemplo de link component do upstream troca a âncora pelo link de um
roteador. Um template Django cria links com `<a>` e
`{% verbatim %}{% url %}{% endverbatim %}`, então o `<c-breadcrumb.link>` já é
isso.
:::
