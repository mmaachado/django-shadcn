---
title: Link
description: An anchor styled like the link variant of a button.
description.pt-br: Uma âncora com o estilo da variante link do botão.
description.es: Un ancla con el estilo de la variante link del botón.
---

<c-docs.demo-section class="min-h-[350px]">
<c-a href="#">Link</c-a>
</c-docs.demo-section>

## Installation

```bash
uvx django_shadcn@latest add a
```

## Usage

<c-docs.demo-section>
<c-a href="#">Link</c-a>
</c-docs.demo-section>

```html
<c-a href='/docs'>Link</c-a>
```

The tag is `<c-a>`, after the element it renders. It takes the button sizes and
nothing else — upstream this is the `link` variant of the button applied to an
anchor, so there is no `variant` to pass. For a link that looks like a solid
button, use `<c-button>` with an `href`.

Every attribute you set reaches the `<a>`, so `target`, `rel` and `download`
work as usual, and `href` takes Django's `url` tag like any other template.

## Examples

### Sizes

<c-docs.demo-section>
<div class="flex flex-wrap items-center gap-4">
    <c-a href="#" size="xs">Extra small</c-a>
    <c-a href="#" size="sm">Small</c-a>
    <c-a href="#">Default</c-a>
    <c-a href="#" size="lg">Large</c-a>
</div>
</c-docs.demo-section>

```html
<c-a href='#' size='xs'>Extra small</c-a>
<c-a href='#' size='sm'>Small</c-a>
<c-a href='#'>Default</c-a>
<c-a href='#' size='lg'>Large</c-a>
```

### With an icon

<c-docs.demo-section>
<c-a href="#">
    Documentation
    <c-icon name="chevron-right" />
</c-a>
</c-docs.demo-section>

```html
<c-a href='#'>
    Documentation
    <c-icon name='chevron-right' />
</c-a>
```

### External

<c-docs.demo-section>
<c-a href="https://ui.shadcn.com" target="_blank" rel="noopener noreferrer">
    shadcn/ui
</c-a>
</c-docs.demo-section>

```html
<c-a href='https://ui.shadcn.com' target='_blank' rel='noopener noreferrer'>
    shadcn/ui
</c-a>
```
