---
title: Collapsible
description: An interactive panel that expands and collapses.
description.pt-br: Um painel que expande e recolhe.
description.es: Un panel que se expande y se contrae.
---

<c-docs.demo-section class="min-h-[350px]">
<c-collapsible class="w-[350px] text-left">
<div class="flex items-center justify-between gap-4 px-1">
<h4 class="text-sm font-semibold">@mmaachado starred 3 repositories</h4>
<c-collapsible.trigger class="inline-flex size-8 items-center justify-center rounded-md hover:bg-accent">
<c-icon name="chevrons-up-down" class="size-4" />
<span class="sr-only">Toggle</span>
</c-collapsible.trigger>
</div>
<div class="mt-2 rounded-md border px-4 py-3 font-mono text-sm">django-shadcn</div>
<c-collapsible.content class="space-y-2">
<div class="mt-2 rounded-md border px-4 py-3 font-mono text-sm">django-cotton</div>
<div class="rounded-md border px-4 py-3 font-mono text-sm">tailwindcss</div>
</c-collapsible.content>
</c-collapsible>
</c-docs.demo-section>

## Installation

```bash
uvx django_shadcn@latest add collapsible
```

## Usage

<c-docs.demo-section>
<c-collapsible class="w-[350px] text-left">
<c-collapsible.trigger class="inline-flex h-9 items-center rounded-md border px-4 text-sm font-medium hover:bg-accent">
Show details
</c-collapsible.trigger>
<c-collapsible.content>
<p class="mt-2 rounded-md border px-4 py-3 text-sm text-muted-foreground">
Everything you were not looking at a moment ago.
</p>
</c-collapsible.content>
</c-collapsible>
</c-docs.demo-section>

```html
<c-collapsible>
    <c-collapsible.trigger>Show details</c-collapsible.trigger>
    <c-collapsible.content>
        <p>Everything you were not looking at a moment ago.</p>
    </c-collapsible.content>
</c-collapsible>
```

`open` is Alpine state on the root, so the trigger and the content both see it
without being told about each other. Start it expanded with
`default_open="true"`.

## Examples

### Open by default

<c-docs.demo-section>
<c-collapsible default_open="true" class="w-[350px] text-left">
<c-collapsible.trigger class="inline-flex h-9 items-center rounded-md border px-4 text-sm font-medium hover:bg-accent">
Already open
</c-collapsible.trigger>
<c-collapsible.content>
<p class="mt-2 rounded-md border px-4 py-3 text-sm text-muted-foreground">
Visible from the first paint.
</p>
</c-collapsible.content>
</c-collapsible>
</c-docs.demo-section>

```html
<c-collapsible default_open="true">
    <c-collapsible.trigger>Already open</c-collapsible.trigger>
    <c-collapsible.content>...</c-collapsible.content>
</c-collapsible>
```

## Notes

The height animation comes from Alpine's `collapse` plugin, the same one the
accordion uses. Without it the panel still opens and closes, just instantly.
