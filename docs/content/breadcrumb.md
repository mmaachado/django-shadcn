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

## Installation

```bash
uvx django_shadcn@latest add breadcrumb
```

## Usage

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

The last crumb is a `page`, not a link: it carries `aria-current="page"` and
is not focusable.

## Examples

### Custom separator

<c-docs.demo-section>
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
</c-docs.demo-section>

```html
<c-breadcrumb.separator>/</c-breadcrumb.separator>
```

### Collapsed

<c-docs.demo-section>
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
</c-docs.demo-section>

```html
<c-breadcrumb.item>
  <c-breadcrumb.ellipsis />
</c-breadcrumb.item>
```
