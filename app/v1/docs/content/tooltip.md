---
title: Tooltip
description: A short label that appears on hover or focus.
description.pt-br: Um rótulo curto que aparece ao passar o mouse ou focar.
description.es: Una etiqueta breve que aparece al pasar el ratón o enfocar.
---

<c-docs.demo-section class="min-h-[350px]">
<c-tooltip>
<c-tooltip.trigger>
<c-button variant="outline">Hover me</c-button>
</c-tooltip.trigger>
<c-tooltip.content>Add to library</c-tooltip.content>
</c-tooltip>
</c-docs.demo-section>

<c-docs.cheat-sheet name="tooltip">
<c-tooltip>
  <c-tooltip.trigger>
    <c-button variant="outline">Hover me</c-button>
  </c-tooltip.trigger>
  <c-tooltip.content>Add to library</c-tooltip.content>
</c-tooltip>
</c-docs.cheat-sheet>

:::en
## Installation
:::pt-br
## Instalação
:::

```bash
uvx django_shadcn@latest add tooltip
```

:::en
## Usage
:::pt-br
## Uso
:::

<c-docs.example>
<c-tooltip>
  <c-tooltip.trigger>
    <c-button variant="outline">Hover me</c-button>
  </c-tooltip.trigger>
  <c-tooltip.content>Add to library</c-tooltip.content>
</c-tooltip>
</c-docs.example>

:::en
The trigger reacts to `mouseenter` and to `focusin`, so the tooltip shows for
the keyboard as well as the pointer.

## Examples

### Sides
:::pt-br
O trigger reage a `mouseenter` e a `focusin`, então o tooltip aparece para o
teclado assim como para o ponteiro.

## Exemplos

### Lados
:::

<c-docs.example>
<div class="flex items-center gap-4">
  <c-tooltip>
    <c-tooltip.trigger><c-button variant="outline" size="sm">Top</c-button></c-tooltip.trigger>
    <c-tooltip.content side="top">On top</c-tooltip.content>
  </c-tooltip>
  <c-tooltip>
    <c-tooltip.trigger><c-button variant="outline" size="sm">Right</c-button></c-tooltip.trigger>
    <c-tooltip.content side="right">To the right</c-tooltip.content>
  </c-tooltip>
  <c-tooltip>
    <c-tooltip.trigger><c-button variant="outline" size="sm">Bottom</c-button></c-tooltip.trigger>
    <c-tooltip.content side="bottom">Below</c-tooltip.content>
  </c-tooltip>
  <c-tooltip>
    <c-tooltip.trigger><c-button variant="outline" size="sm">Left</c-button></c-tooltip.trigger>
    <c-tooltip.content side="left">To the left</c-tooltip.content>
  </c-tooltip>
</div>
</c-docs.example>

:::en
## Notes

Radix puts the tooltip in a portal and measures the viewport to flip the side
when there is no room. Here the content is positioned against the trigger with
utility classes, so `side` is a choice you make rather than something worked
out at runtime. Near the edge of the screen, pick the side that fits.
:::pt-br
## Observações

O Radix põe o tooltip num portal e mede a viewport para virar o lado quando não
há espaço. Aqui o conteúdo é posicionado em relação ao trigger com classes
utilitárias, então `side` é uma escolha sua e não algo calculado em tempo de
execução. Perto da borda da tela, escolha o lado que cabe.
:::

:::en
## API reference
:::pt-br
## Referência da API
:::

<c-docs.api-reference name="tooltip" />
