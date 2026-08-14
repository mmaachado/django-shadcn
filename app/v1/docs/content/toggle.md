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

## Installation

```bash
uvx django_shadcn@latest add toggle
```

## Usage

<c-docs.demo-section>
<c-toggle aria-label="Toggle italic"><span class="italic">I</span></c-toggle>
</c-docs.demo-section>

```html
<c-toggle aria-label="Toggle italic">
    <span class="italic">I</span>
</c-toggle>
```

The pressed state lives in Alpine and is published as `data-state="on"` and
`aria-pressed`, so the styling and assistive technology read the same source.
Start it pressed with `pressed="true"`.

## Examples

### Variants

<c-docs.demo-section>
<div class="flex items-center gap-3">
<c-toggle>Default</c-toggle>
<c-toggle variant="outline">Outline</c-toggle>
</div>
</c-docs.demo-section>

```html
<c-toggle>Default</c-toggle>
<c-toggle variant="outline">Outline</c-toggle>
```

### Sizes

<c-docs.demo-section>
<div class="flex items-center gap-3">
<c-toggle variant="outline" size="sm">Small</c-toggle>
<c-toggle variant="outline">Default</c-toggle>
<c-toggle variant="outline" size="lg">Large</c-toggle>
</div>
</c-docs.demo-section>

```html
<c-toggle size="sm">Small</c-toggle>
<c-toggle>Default</c-toggle>
<c-toggle size="lg">Large</c-toggle>
```

### Pressed by default

<c-docs.demo-section>
<c-toggle variant="outline" pressed="true">Pressed</c-toggle>
</c-docs.demo-section>

```html
<c-toggle variant="outline" pressed="true">Pressed</c-toggle>
```

### Disabled

<c-docs.demo-section>
<c-toggle variant="outline" disabled>Disabled</c-toggle>
</c-docs.demo-section>

```html
<c-toggle variant="outline" disabled>Disabled</c-toggle>
```
