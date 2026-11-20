---
title: Scroll Area
description: A scrolling region with a scrollbar that matches the theme.
description.pt-br: Uma área rolável com barra de rolagem no tema da biblioteca.
description.es: Un área desplazable con barra de desplazamiento acorde al tema.
---

<c-docs.demo-section class="min-h-[350px]">
<c-scroll-area class="h-56 w-[320px] rounded-md border">
<div class="p-4 text-start">
<h4 class="mb-3 text-sm font-semibold">Components</h4>
<div class="space-y-2 text-sm text-muted-foreground">
<div>Accordion</div><div>Alert</div><div>Avatar</div><div>Badge</div>
<div>Breadcrumb</div><div>Button</div><div>Card</div><div>Checkbox</div>
<div>Command</div><div>Dialog</div><div>Field</div><div>Input</div>
<div>Popover</div><div>Select</div><div>Table</div><div>Tabs</div>
</div>
</div>
</c-scroll-area>
</c-docs.demo-section>

:::en
## Installation
:::pt-br
## Instalação
:::

```bash
uvx django_shadcn@latest add scroll_area
```

:::en
## Usage
:::pt-br
## Uso
:::

<c-docs.example>
<c-scroll-area class="h-32 w-[320px] rounded-md border">
  <p class="p-4 text-start text-sm text-muted-foreground">
    Give the scroll area a height and let the content run past it. The scrollbar
    picks up the border colour from the palette, so it stops looking like a piece
    of the operating system that wandered in.
  </p>
</c-scroll-area>
</c-docs.example>

:::en
The size goes on the component; the content inside is free to be taller.

## Examples

### Horizontal
:::pt-br
O tamanho vai no componente; o conteúdo dentro dele pode ser mais alto à
vontade.

## Exemplos

### Horizontal
:::

<c-docs.example>
<c-scroll-area class="w-[320px] rounded-md border">
  <div class="flex w-max gap-4 p-4">
    <div class="flex size-24 shrink-0 items-center justify-center rounded-md bg-muted text-sm">One</div>
    <div class="flex size-24 shrink-0 items-center justify-center rounded-md bg-muted text-sm">Two</div>
    <div class="flex size-24 shrink-0 items-center justify-center rounded-md bg-muted text-sm">Three</div>
    <div class="flex size-24 shrink-0 items-center justify-center rounded-md bg-muted text-sm">Four</div>
  </div>
</c-scroll-area>
</c-docs.example>

:::en
## Notes

Radix hides the native scrollbar and draws its own with JavaScript, which is
how it gets the same thin bar everywhere. Here the native scrollbar is styled
instead: momentum scrolling and the platform behaviour stay intact, and the
trade is that Firefox only honours the width and the colour, not the rounded
thumb.
:::pt-br
## Observações

O Radix esconde a barra de rolagem nativa e desenha a dele com JavaScript, que é
como consegue a mesma barra fina em todo lugar. Aqui a barra nativa é
estilizada: a rolagem com embalo e o comportamento da plataforma continuam
intactos, e a troca é que o Firefox só respeita a largura e a cor, não o
puxador arredondado.
:::
