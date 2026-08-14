---
title: Popover
description: Displays rich content in a portal, triggered by a button.
description.pt-br: Exibe conteúdo rico sobre a página, aberto por um botão.
description.es: Muestra contenido enriquecido sobre la página, abierto por un botón.
---

<c-docs.demo-section class="min-h-[350px]">
<c-popover>
<c-popover.trigger>
<c-button variant="outline">Open Popover</c-button>
</c-popover.trigger>
<c-popover.content>
<div class="grid gap-4">
<div class="space-y-2">
<h4 class="font-medium leading-none">Dimensions</h4>
<p class="text-sm text-muted-foreground">Set the dimensions for the layer.</p>
</div>
<div class="grid gap-2">
<div class="grid grid-cols-3 items-center gap-4">
<c-label for="width">Width</c-label>
<c-input id="width" value="100%" class="col-span-2" />
</div>
<div class="grid grid-cols-3 items-center gap-4">
<c-label for="height">Height</c-label>
<c-input id="height" value="25px" class="col-span-2" />
</div>
</div>
</div>
</c-popover.content>
</c-popover>
</c-docs.demo-section>

## Installation

```bash
uvx django_shadcn@latest add popover
```

## Usage

```html
<c-popover>
  <c-popover.trigger>
    <c-button variant="outline">Open Popover</c-button>
  </c-popover.trigger>
  <c-popover.content> Place content for popover here. </c-popover.content>
</c-popover>
```
