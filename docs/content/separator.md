---
title: Separator
description: Visually or semantically separates content.
description.pt-br: Separa conteúdo visual ou semanticamente.
description.es: Separa contenido visual o semánticamente.
---

<c-docs.demo-section class="min-h-[350px]">

<div>
              <div class="space-y-1">
                <h4 class="text-sm font-medium leading-none">Django Shadcn</h4>
                <p class="text-sm text-muted-foreground">
                  An open-source UI component library for Django, based on shadcn/ui.
                </p>
              </div>
              <c-separator class="my-4" />
              <div class="flex h-5 items-center space-x-4 text-sm">
                <div>Blog</div>
                <c-separator orientation="vertical" />
                <div>Docs</div>
                <c-separator orientation="vertical" />
                <div>Source</div>
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
<c-separator orientation="vertical" />
```

### Non-decorative (Semantic)

<c-docs.demo-section>
<c-separator decorative="false" />
</c-docs.demo-section>

```html
<c-separator decorative="false" />
```
