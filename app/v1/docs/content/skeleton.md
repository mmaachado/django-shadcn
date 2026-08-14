---
title: Skeleton
description: Use to show a placeholder while content is loading.
description.pt-br: Um espaço reservado enquanto o conteúdo carrega.
description.es: Un espacio reservado mientras el contenido carga.
---

<c-docs.demo-section class="min-h-[350px]">

<div class="flex items-center gap-4">
            <c-skeleton class="size-12 rounded-full" />
            <div class="space-y-2">
                <c-skeleton class="h-4 w-[250px]" />
                <c-skeleton class="h-4 w-[200px]" />
            </div>
        </div>
</c-docs.demo-section>

## Installation

```bash
uvx django_shadcn@latest add skeleton
```

## Usage

<c-docs.demo-section background="bg-background">
<c-skeleton class="h-4 w-[250px]" />
</c-docs.demo-section>

```html
<c-skeleton class="h-4 w-[250px]" />
```

The component ships no dimensions of its own. Give it the size and shape of
whatever it stands in for.

It fills with `bg-accent`, which is the same value as `bg-muted` in the
default palette. The demos below sit on the page background so the shapes
stay visible.

## Examples

### Card

<c-docs.demo-section background="bg-background">

<div class="flex flex-col gap-3">
    <c-skeleton class="h-[125px] w-[250px] rounded-xl" />
    <div class="space-y-2">
        <c-skeleton class="h-4 w-[250px]" />
        <c-skeleton class="h-4 w-[200px]" />
    </div>
</div>
</c-docs.demo-section>

```html
<div class="flex flex-col gap-3">
  <c-skeleton class="h-[125px] w-[250px] rounded-xl" />
  <div class="space-y-2">
    <c-skeleton class="h-4 w-[250px]" />
    <c-skeleton class="h-4 w-[200px]" />
  </div>
</div>
```

### Avatar and text

<c-docs.demo-section background="bg-background">

<div class="flex items-center gap-4">
    <c-skeleton class="size-12 rounded-full" />
    <div class="space-y-2">
        <c-skeleton class="h-4 w-[250px]" />
        <c-skeleton class="h-4 w-[200px]" />
    </div>
</div>
</c-docs.demo-section>

```html
<div class="flex items-center gap-4">
  <c-skeleton class="size-12 rounded-full" />
  <div class="space-y-2">
    <c-skeleton class="h-4 w-[250px]" />
    <c-skeleton class="h-4 w-[200px]" />
  </div>
</div>
```

### Standing in for a card

<c-docs.demo-section background="bg-background">
<c-card class="w-[320px]">
<c-card.header>
<c-skeleton class="h-5 w-[160px]" />
<c-skeleton class="h-4 w-[220px]" />
</c-card.header>
<c-card.content class="space-y-2">
<c-skeleton class="h-4 w-full" />
<c-skeleton class="h-4 w-[80%]" />
</c-card.content>
<c-card.footer>
<c-skeleton class="h-9 w-[100px] rounded-md" />
</c-card.footer>
</c-card>
</c-docs.demo-section>

```html
<c-card>
  <c-card.header>
    <c-skeleton class="h-5 w-[160px]" />
    <c-skeleton class="h-4 w-[220px]" />
  </c-card.header>
  <c-card.content class="space-y-2">
    <c-skeleton class="h-4 w-full" />
    <c-skeleton class="h-4 w-[80%]" />
  </c-card.content>
</c-card>
```
