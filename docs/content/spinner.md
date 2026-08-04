---
title: Spinner
description: An indicator that something is in progress.
description.pt-br: Um indicador de que algo está em andamento.
description.es: Un indicador de que algo está en marcha.
---

<c-docs.demo-section class="min-h-[350px]">
<c-spinner />
</c-docs.demo-section>

## Installation

```bash
uvx django_shadcn@latest add spinner
```

## Usage

<c-docs.demo-section>
<c-spinner />
</c-docs.demo-section>

```html
<c-spinner />
```

It is the lucide `loader-circle` icon with `animate-spin`, already carrying
`role="status"` and an accessible label.

## Examples

### Sizes

<c-docs.demo-section>

<div class="flex items-center gap-4">
    <c-spinner class="size-3" />
    <c-spinner />
    <c-spinner class="size-6" />
    <c-spinner class="size-8" />
</div>
</c-docs.demo-section>

```html
<c-spinner class="size-3" />
<c-spinner />
<c-spinner class="size-6" />
```

### Inside a button

<c-docs.demo-section>

<div class="flex items-center gap-3">
    <c-button disabled>
        <c-spinner />
        Saving
    </c-button>
    <c-button variant="outline" disabled>
        <c-spinner />
        Please wait
    </c-button>
</div>
</c-docs.demo-section>

```html
<c-button disabled>
  <c-spinner />
  Saving
</c-button>
```

### Color

<c-docs.demo-section>

<div class="flex items-center gap-4">
    <c-spinner class="size-6 text-muted-foreground" />
    <c-spinner class="size-6 text-primary" />
    <c-spinner class="size-6 text-destructive" />
</div>
</c-docs.demo-section>

```html
<c-spinner class="size-6 text-primary" />
```
