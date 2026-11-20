---
title: Button Group
description: Groups related buttons together, sharing a single outline.
description.pt-br: Agrupa botões relacionados sob um contorno só.
description.es: Agrupa botones relacionados bajo un solo contorno.
---

<c-docs.demo-section class="min-h-[350px]">
<c-button-group>
<c-button variant="outline">Day</c-button>
<c-button variant="outline">Week</c-button>
<c-button variant="outline">Month</c-button>
</c-button-group>
</c-docs.demo-section>

:::en
## Installation
:::pt-br
## Instalação
:::

```bash
uvx django_shadcn@latest add button_group
```

:::en
## Usage
:::pt-br
## Uso
:::

<c-docs.demo-section>
<c-button-group>
<c-button variant="outline">Day</c-button>
<c-button variant="outline">Week</c-button>
</c-button-group>
</c-docs.demo-section>

```html
<c-button-group>
  <c-button variant="outline">Day</c-button>
  <c-button variant="outline">Week</c-button>
</c-button-group>
```

:::en
The group flattens the inner corners and drops the duplicated borders
through descendant selectors, so the buttons need nothing special.

## Examples

### Vertical
:::pt-br
O grupo achata os cantos internos e tira as bordas duplicadas por seletores de
descendente, então os botões não precisam de nada especial.

## Exemplos

### Vertical
:::

<c-docs.demo-section>
<c-button-group orientation="vertical">
<c-button variant="outline">Top</c-button>
<c-button variant="outline">Middle</c-button>
<c-button variant="outline">Bottom</c-button>
</c-button-group>
</c-docs.demo-section>

```html
<c-button-group orientation="vertical">
  <c-button variant="outline">Top</c-button>
  <c-button variant="outline">Bottom</c-button>
</c-button-group>
```

:::en
### With text
:::pt-br
### Com texto
:::

<c-docs.demo-section>
<c-button-group>
<c-button-group.text>https://</c-button-group.text>
<c-input placeholder="example.com" class="w-[220px]" />
<c-button variant="outline">Go</c-button>
</c-button-group>
</c-docs.demo-section>

```html
<c-button-group>
  <c-button-group.text>https://</c-button-group.text>
  <c-input placeholder="example.com" />
  <c-button variant="outline">Go</c-button>
</c-button-group>
```

:::en
### With a separator
:::pt-br
### Com separador
:::

<c-docs.demo-section>
<c-button-group>
<c-button>Save</c-button>
<c-button-group.separator />
<c-button size="icon">
<c-icon name="chevron-down" />
</c-button>
</c-button-group>
</c-docs.demo-section>

```html
<c-button-group>
  <c-button>Save</c-button>
  <c-button-group.separator />
  <c-button size="icon">
    <c-icon name="chevron-down" />
  </c-button>
</c-button-group>
```

:::en
### Nested groups
:::pt-br
### Grupos aninhados
:::

<c-docs.demo-section>
<c-button-group>
<c-button-group>
<c-button variant="outline">Undo</c-button>
<c-button variant="outline">Redo</c-button>
</c-button-group>
<c-button-group>
<c-button variant="outline">Cut</c-button>
<c-button variant="outline">Paste</c-button>
</c-button-group>
</c-button-group>
</c-docs.demo-section>

```html
<c-button-group>
  <c-button-group>...</c-button-group>
  <c-button-group>...</c-button-group>
</c-button-group>
```
