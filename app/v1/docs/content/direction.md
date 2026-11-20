---
title: Direction
description: Right-to-left layouts, set with one attribute on the html element from the active language.
description.pt-br: Layouts da direita para a esquerda, definidos por um atributo no elemento html a partir do idioma ativo.
description.es: Diseños de derecha a izquierda, definidos con un atributo en el elemento html a partir del idioma activo.
---

<c-docs.demo-section class="min-h-[350px]">
<div class="grid w-full gap-10 md:grid-cols-2">
<div dir="ltr" class="flex flex-col items-start gap-4">
<span class="font-mono text-sm text-muted-foreground">dir="ltr"</span>
<c-button-group>
<c-button variant="outline">Day</c-button>
<c-button variant="outline">Week</c-button>
<c-button variant="outline">Month</c-button>
</c-button-group>
<c-input-group class="w-full max-w-[280px]">
<c-input-group.addon>
<c-icon name="search" />
</c-input-group.addon>
<c-input-group.input placeholder="Search" />
</c-input-group>
</div>
<div dir="rtl" class="flex flex-col items-start gap-4">
<span dir="ltr" class="font-mono text-sm text-muted-foreground">dir="rtl"</span>
<c-button-group>
<c-button variant="outline">Day</c-button>
<c-button variant="outline">Week</c-button>
<c-button variant="outline">Month</c-button>
</c-button-group>
<c-input-group class="w-full max-w-[280px]">
<c-input-group.addon>
<c-icon name="search" />
</c-input-group.addon>
<c-input-group.input placeholder="Search" />
</c-input-group>
</div>
</div>
</c-docs.demo-section>

## Not a component

There is nothing to install. shadcn/ui ships a `Direction` provider, a React
context that tells Radix which way the text runs. It does not port, and nothing
here replaces it: Django already knows the direction of the active language,
and the browser needs a single attribute to know it too.

## Usage

Set `dir` on the `<html>` element of your base template:

```html
<html lang="{{ LANGUAGE_CODE }}" dir="{% if LANGUAGE_BIDI %}rtl{% else %}ltr{% endif %}">
```

`LANGUAGE_BIDI` is `True` when the active language is written right to left,
such as Arabic, Hebrew or Persian. It comes from the
`django.template.context_processors.i18n` context processor, which
`startproject` turns on. With `LocaleMiddleware`, every response gets the
direction of the language it was rendered in.

For one part of a page, put `dir` on that element instead. The demo above does
this, with the same markup on both sides.

## What mirrors

The components use logical utilities: `ms-` and `me-` for margins, `ps-` and
`pe-` for padding, `start-` and `end-` for position, `text-start`, `border-s`
and `rounded-s`. Under `dir="rtl"` each of them moves to the other side, so
spacing, borders and rounded ends follow the text. A button group keeps its
rounded ends on the outside, a submenu opens on the left, and `align="start"`
on a menu lines up with the start of the line.

A few things keep their side on purpose:

- A side you name. `side="left"` on `sheet`, `sidebar`, `tooltip` and
  `hover_card`, and `direction="left"` on `drawer`, mean the left of the
  screen. For a sidebar at the start of an RTL page, pass `side="right"`.
- `carousel`, which scrolls in physical coordinates, so its previous button
  stays on the left.
- The value axis of `chart`. A plot does not mirror because the language does.

## What does not mirror

Icons. Lucide has no RTL variants, so an arrow or a chevron points the same way
in both directions. Whether one should flip depends on what it means: a "next"
chevron usually should, a play button or a download arrow should not. That is
your call, and Tailwind's `rtl:` variant makes it one class:

```html
<c-icon name="chevron-right" class="rtl:rotate-180" />
```
