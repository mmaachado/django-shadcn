---
title: Aspect Ratio
description: Displays content within a desired ratio.
description.pt-br: Mantém o conteúdo dentro da proporção que você escolher.
description.es: Mantiene el contenido dentro de la proporción que elijas.
---

<c-docs.demo-section class="min-h-[350px]">
<div class="w-[450px]">
            <c-aspect-ratio ratio="16/9" class="overflow-hidden rounded-lg bg-muted">
                <div class="flex size-full items-center justify-center text-sm text-muted-foreground">
                    16 / 9
                </div>
            </c-aspect-ratio>
        </div>
</c-docs.demo-section>

## Installation

```bash
uvx django_shadcn@latest add aspect_ratio
```

## Usage

<c-docs.demo-section>
    <div class="w-[300px]">
        <c-aspect-ratio ratio="16/9" class="overflow-hidden rounded-lg bg-muted">
            <div class="flex size-full items-center justify-center text-sm text-muted-foreground">
                16 / 9
            </div>
        </c-aspect-ratio>
    </div>
</c-docs.demo-section>

```html
<c-aspect-ratio ratio='16/9' class='overflow-hidden rounded-lg'>
    <img src='/cover.jpg' alt='' class='size-full object-cover' />
</c-aspect-ratio>
```

Radix reserves the space with a padding hack. Here it is the native `aspect-
ratio` CSS property, so `ratio` takes anything the property accepts: `16/9`,
`4/3`, `1.85`. The default is `1/1`.

## Examples

### Square

<c-docs.demo-section>
<div class="w-[200px]">
    <c-aspect-ratio class="overflow-hidden rounded-lg bg-muted">
        <div class="flex size-full items-center justify-center text-sm text-muted-foreground">
            1 / 1
        </div>
    </c-aspect-ratio>
</div>
</c-docs.demo-section>

```html
<c-aspect-ratio class='overflow-hidden rounded-lg bg-muted'>...</c-aspect-ratio>
```

### Portrait

<c-docs.demo-section>
<div class="w-[200px]">
    <c-aspect-ratio ratio="3/4" class="overflow-hidden rounded-lg bg-muted">
        <div class="flex size-full items-center justify-center text-sm text-muted-foreground">
            3 / 4
        </div>
    </c-aspect-ratio>
</div>
</c-docs.demo-section>

```html
<c-aspect-ratio ratio='3/4' class='overflow-hidden rounded-lg bg-muted'>...</c-aspect-ratio>
```
