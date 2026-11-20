---
title: Toggle
description: A two-state button that can be on or off.
description.pt-br: Um botão de dois estados, ligado ou desligado.
description.es: Un botón de dos estados, encendido o apagado.
---

<c-docs.demo-section class="min-h-[350px]">
<c-toggle variant="outline" aria-label="Toggle bold">
<span class="font-bold">B</span>
</c-toggle>
</c-docs.demo-section>

:::en
## Installation
:::pt-br
## Instalação
:::

```bash
uvx django_shadcn@latest add toggle
```

:::en
## Usage
:::pt-br
## Uso
:::

<c-docs.example>
<c-toggle aria-label="Toggle italic"><span class="italic">I</span></c-toggle>
</c-docs.example>

:::en
The pressed state lives in Alpine and is published as `data-state="on"` and
`aria-pressed`, so the styling and assistive technology read the same source.
Start it pressed with `pressed="true"`.

## Examples

### Variants
:::pt-br
O estado de pressionado mora no Alpine e é publicado como `data-state="on"` e
`aria-pressed`, então o estilo e as tecnologias assistivas leem a mesma fonte.
Comece pressionado com `pressed="true"`.

## Exemplos

### Variantes
:::

<c-docs.example>
<div class="flex items-center gap-3">
  <c-toggle>Default</c-toggle>
  <c-toggle variant="outline">Outline</c-toggle>
</div>
</c-docs.example>

:::en
### Sizes
:::pt-br
### Tamanhos
:::

<c-docs.example>
<div class="flex items-center gap-3">
  <c-toggle variant="outline" size="sm">Small</c-toggle>
  <c-toggle variant="outline">Default</c-toggle>
  <c-toggle variant="outline" size="lg">Large</c-toggle>
</div>
</c-docs.example>

:::en
### Pressed by default
:::pt-br
### Pressionado por padrão
:::

<c-docs.example>
<c-toggle variant="outline" pressed="true">Pressed</c-toggle>
</c-docs.example>

:::en
### Disabled
:::pt-br
### Desabilitado
:::

<c-docs.example>
<c-toggle variant="outline" disabled>Disabled</c-toggle>
</c-docs.example>
