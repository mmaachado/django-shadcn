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
<c-breadcrumb.link href="/">Home</c-breadcrumb.link>
</c-breadcrumb.item>
<c-breadcrumb.separator />
<c-breadcrumb.item>
<c-breadcrumb.link href="/introduction">Docs</c-breadcrumb.link>
</c-breadcrumb.item>
<c-breadcrumb.separator />
<c-breadcrumb.item>
<c-breadcrumb.page>Breadcrumb</c-breadcrumb.page>
</c-breadcrumb.item>
</c-breadcrumb.list>
</c-breadcrumb>
</c-docs.demo-section>

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
:::pt-br
## Uso
:::

```html
<c-breadcrumb>
  <c-breadcrumb.list>
    <c-breadcrumb.item>
      <c-breadcrumb.link href="/">Home</c-breadcrumb.link>
    </c-breadcrumb.item>
    <c-breadcrumb.separator />
    <c-breadcrumb.item>
      <c-breadcrumb.page>Current</c-breadcrumb.page>
    </c-breadcrumb.item>
  </c-breadcrumb.list>
</c-breadcrumb>
```

:::en
The last crumb is a `page`, not a link: it carries `aria-current="page"` and
is not focusable.

## Examples

### Custom separator
:::pt-br
O último item é uma `page`, não um link: ele leva `aria-current="page"` e não
recebe foco.

## Exemplos

### Separador personalizado
:::

<c-docs.example>
<c-breadcrumb>
  <c-breadcrumb.list>
    <c-breadcrumb.item>
      <c-breadcrumb.link href="/">Home</c-breadcrumb.link>
    </c-breadcrumb.item>
    <c-breadcrumb.separator>/</c-breadcrumb.separator>
    <c-breadcrumb.item>
      <c-breadcrumb.page>Components</c-breadcrumb.page>
    </c-breadcrumb.item>
  </c-breadcrumb.list>
</c-breadcrumb>
</c-docs.example>

:::en
### Collapsed
:::pt-br
### Recolhido
:::

<c-docs.example>
<c-breadcrumb>
  <c-breadcrumb.list>
    <c-breadcrumb.item>
      <c-breadcrumb.link href="/">Home</c-breadcrumb.link>
    </c-breadcrumb.item>
    <c-breadcrumb.separator />
    <c-breadcrumb.item>
      <c-breadcrumb.ellipsis />
    </c-breadcrumb.item>
    <c-breadcrumb.separator />
    <c-breadcrumb.item>
      <c-breadcrumb.page>Breadcrumb</c-breadcrumb.page>
    </c-breadcrumb.item>
  </c-breadcrumb.list>
</c-breadcrumb>
</c-docs.example>

:::en
## API reference
:::pt-br
## Referência da API
:::

<c-docs.api-reference name="breadcrumb" />
