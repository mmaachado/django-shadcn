---
title: Scroll Area
description: A scrolling region with a scrollbar that matches the theme.
description.pt-br: Uma área rolável com barra de rolagem no tema da biblioteca.
description.es: Un área desplazable con barra de desplazamiento acorde al tema.
---

<c-docs.demo-section class="min-h-[350px]">
<c-scroll-area class="h-56 w-[320px] rounded-md border">
<div class="p-4 text-left">
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

## Installation

```bash
uvx django_shadcn@latest add scroll_area
```

## Usage

<c-docs.demo-section>
<c-scroll-area class="h-32 w-[320px] rounded-md border">
<p class="p-4 text-left text-sm text-muted-foreground">
Give the scroll area a height and let the content run past it. The scrollbar
picks up the border colour from the palette, so it stops looking like a piece
of the operating system that wandered in.
</p>
</c-scroll-area>
</c-docs.demo-section>

```html
<c-scroll-area class="h-32 w-[320px] rounded-md border">
    <p class="p-4">...</p>
</c-scroll-area>
```

The size goes on the component; the content inside is free to be taller.

## Examples

### Horizontal

<c-docs.demo-section>
<c-scroll-area class="w-[320px] rounded-md border">
<div class="flex w-max gap-4 p-4">
<div class="flex size-24 shrink-0 items-center justify-center rounded-md bg-muted text-sm">One</div>
<div class="flex size-24 shrink-0 items-center justify-center rounded-md bg-muted text-sm">Two</div>
<div class="flex size-24 shrink-0 items-center justify-center rounded-md bg-muted text-sm">Three</div>
<div class="flex size-24 shrink-0 items-center justify-center rounded-md bg-muted text-sm">Four</div>
</div>
</c-scroll-area>
</c-docs.demo-section>

```html
<c-scroll-area class="w-[320px] rounded-md border">
    <div class="flex w-max gap-4 p-4">
        <div class="size-24 shrink-0 rounded-md bg-muted"></div>
    </div>
</c-scroll-area>
```

## Notes

Radix hides the native scrollbar and draws its own with JavaScript, which is
how it gets the same thin bar everywhere. Here the native scrollbar is styled
instead: momentum scrolling and the platform behaviour stay intact, and the
trade is that Firefox only honours the width and the colour, not the rounded
thumb.
