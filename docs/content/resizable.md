---
title: Resizable
description: Panels the reader can resize by dragging the divider.
description.pt-br: Painéis que o leitor redimensiona arrastando a divisa.
description.es: Paneles que se redimensionan arrastrando el divisor.
---

<c-docs.demo-section class="min-h-[350px]">
<div class="h-[220px] w-[420px] rounded-lg border">
<c-resizable>
<c-resizable.panel default_size="1">
<div class="flex h-full items-center justify-center p-6 text-sm font-medium">One</div>
</c-resizable.panel>
<c-resizable.handle with_handle="true" />
<c-resizable.panel default_size="1">
<div class="flex h-full items-center justify-center p-6 text-sm font-medium">Two</div>
</c-resizable.panel>
</c-resizable>
</div>
</c-docs.demo-section>

## Installation

```bash
uvx django_shadcn@latest add resizable
```

## Usage

<c-docs.demo-section>
<div class="h-[180px] w-[420px] rounded-lg border">
<c-resizable>
<c-resizable.panel>
<div class="flex h-full items-center justify-center p-6 text-sm font-medium">Sidebar</div>
</c-resizable.panel>
<c-resizable.handle />
<c-resizable.panel default_size="2">
<div class="flex h-full items-center justify-center p-6 text-sm font-medium">Content</div>
</c-resizable.panel>
</c-resizable>
</div>
</c-docs.demo-section>

```html
<div class="h-[180px] w-[420px] rounded-lg border">
<c-resizable>
    <c-resizable.panel>
        <div class="p-6">Sidebar</div>
    </c-resizable.panel>
    <c-resizable.handle />
    <c-resizable.panel default_size="2">
        <div class="p-6">Content</div>
    </c-resizable.panel>
</c-resizable>
</div>
```

`default_size` is a share, not a percentage: two panels at `1` and `2` split
the space one third to two thirds. Dragging the handle moves that share between
the two panels either side of it and leaves the rest alone.

The group carries `h-full w-full` from the registry, so a `h-*` or `w-*` of
your own passed as `class` loses to it — two utilities for the same property
are settled by the compiled stylesheet. Size the wrapper and let the group
fill it.

## Examples

### Vertical

<c-docs.demo-section>
<div class="h-[260px] w-[420px] rounded-lg border">
<c-resizable orientation="vertical">
<c-resizable.panel>
<div class="flex h-full items-center justify-center p-6 text-sm font-medium">Top</div>
</c-resizable.panel>
<c-resizable.handle with_handle="true" />
<c-resizable.panel>
<div class="flex h-full items-center justify-center p-6 text-sm font-medium">Bottom</div>
</c-resizable.panel>
</c-resizable>
</div>
</c-docs.demo-section>

```html
<div class="h-[260px]">
<c-resizable orientation="vertical">
    <c-resizable.panel>...</c-resizable.panel>
    <c-resizable.handle with_handle="true" />
    <c-resizable.panel>...</c-resizable.panel>
</c-resizable>
</div>
```

### Three panels

<c-docs.demo-section>
<div class="h-[200px] w-[520px] rounded-lg border">
<c-resizable>
<c-resizable.panel>
<div class="flex h-full items-center justify-center p-4 text-sm font-medium">One</div>
</c-resizable.panel>
<c-resizable.handle />
<c-resizable.panel default_size="2">
<div class="flex h-full items-center justify-center p-4 text-sm font-medium">Two</div>
</c-resizable.panel>
<c-resizable.handle />
<c-resizable.panel>
<div class="flex h-full items-center justify-center p-4 text-sm font-medium">Three</div>
</c-resizable.panel>
</c-resizable>
</div>
</c-docs.demo-section>

```html
<c-resizable>
    <c-resizable.panel>...</c-resizable.panel>
    <c-resizable.handle />
    <c-resizable.panel default_size="2">...</c-resizable.panel>
    <c-resizable.handle />
    <c-resizable.panel>...</c-resizable.panel>
</c-resizable>
</div>
```

### Nested

<c-docs.demo-section>
<div class="h-[240px] w-[480px] rounded-lg border">
<c-resizable>
<c-resizable.panel>
<div class="flex h-full items-center justify-center p-4 text-sm font-medium">Left</div>
</c-resizable.panel>
<c-resizable.handle with_handle="true" />
<c-resizable.panel default_size="2">
<div class="h-full">
<c-resizable orientation="vertical">
<c-resizable.panel>
<div class="flex h-full items-center justify-center p-4 text-sm font-medium">Top right</div>
</c-resizable.panel>
<c-resizable.handle with_handle="true" />
<c-resizable.panel>
<div class="flex h-full items-center justify-center p-4 text-sm font-medium">Bottom right</div>
</c-resizable.panel>
</c-resizable>
</div>
</c-resizable.panel>
</c-resizable>
</div>
</c-docs.demo-section>

```html
<c-resizable>
    <c-resizable.panel>...</c-resizable.panel>
    <c-resizable.handle with_handle="true" />
    <c-resizable.panel default_size="2">
        <div class="h-full">
<c-resizable orientation="vertical">
            <c-resizable.panel>...</c-resizable.panel>
            <c-resizable.handle with_handle="true" />
            <c-resizable.panel>...</c-resizable.panel>
        </c-resizable>
    </c-resizable.panel>
</c-resizable>
</div>
```

## Notes

The handle takes the pointer, not the keyboard: upstream lets you nudge a
divider with the arrow keys, and that is not here yet. It is focusable and
shows a focus ring, so the gap is visible rather than hidden.

Sizes are not remembered between visits. `react-resizable-panels` can persist a
layout by id; here a reload starts from `default_size` again.

Nothing enforces a minimum: a panel can be dragged shut. Give the content
inside it a `min-w-*` if that matters.
