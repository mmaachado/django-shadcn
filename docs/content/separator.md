---
title: Separator
description: Visually or semantically separates content.
description.pt-br: Separa conteúdo visual ou semanticamente.
description.es: Separa contenido visual o semánticamente.
---

<c-docs.demo-section>
<div class="w-full max-w-md">
<div class="space-y-1">
<h4 class="text-sm leading-none font-medium">Django Shadcn</h4>
<p class="text-sm text-muted-foreground">An open-source UI component library for Django, based on shadcn/ui.</p>
</div>
<c-separator class="my-4" />
<div class="flex h-5 items-center space-x-4 text-sm">
<div>Blog</div>
<c-separator orientation="vertical" />
<div>Docs</div>
<c-separator orientation="vertical" />
<div>Source</div>
</div>
</div>
</c-docs.demo-section>

## Installation

```bash
uvx django_shadcn@latest add separator
```

## Usage

```html
<c-separator />
```

## Examples

### Vertical

A vertical separator takes its height from the row around it, so give that row
a height.

<c-docs.demo-section>
<div class="flex h-5 items-center space-x-4 text-sm">
<div>Blog</div>
<c-separator orientation="vertical" />
<div>Docs</div>
<c-separator orientation="vertical" />
<div>Source</div>
</div>
</c-docs.demo-section>

```html
<div class="flex h-5 items-center space-x-4 text-sm">
    <div>Blog</div>
    <c-separator orientation="vertical" />
    <div>Docs</div>
</div>
```

### Semantic

A separator is decorative by default: it gets `role="none"` and a screen reader
skips it. When the line is the only thing telling two groups apart, say so and
it becomes a real `separator` with an `aria-orientation`.

<c-docs.demo-section>
<div class="w-full max-w-md">
<p class="pb-4 text-sm text-muted-foreground">Account</p>
<c-separator decorative="false" />
<p class="pt-4 text-sm text-muted-foreground">Billing</p>
</div>
</c-docs.demo-section>

```html
<c-separator decorative="false" />
```
